from fastapi import FastAPI, HTTPException
from typing import List, Dict
from schema.reaction import Reaction, Reactant, Product
from supabase import create_client, Client
import os
from dotenv import load_dotenv

app = FastAPI()

# Initialize Supabase client
# Load environment variables from .env file
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


@app.get("/reactions", response_model=List[Reaction])
def get_reactions():
    response = supabase.table("reactions").select("*").execute()
    return response.data


@app.post("/reactions", response_model=Reaction)
def create_reaction(reaction: Reaction):
    response = supabase.table("reactions").insert(reaction.model_dump()).execute()
    return response.data[0]


@app.put("/reactions/{reaction_id}", response_model=Reaction)
def update_reaction(reaction_id: int, updated_reaction: Reaction):
    response = (
        supabase.table("reactions")
        .update(updated_reaction.model_dump())
        .eq("_id", reaction_id)
        .execute()
    )
    if not response.data:
        raise HTTPException(status_code=404, detail="Reaction not found")
    return response.data[0]


@app.delete("/reactions/{reaction_id}")
def delete_reaction(reaction_id: int):
    response = supabase.table("reactions").delete().eq("_id", reaction_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Reaction not found")
    return {"message": "Reaction deleted successfully"}


@app.post("/reactions/complete", response_model=Reaction)
def complete_reaction(reaction: Reaction):
    batch_size = 100
    offset = 0

    while True:
        response = (
            supabase.table("reactions")
            .select("*")
            .range(offset, offset + batch_size - 1)
            .execute()
        )
        if not response.data:
            break

        for stored_reaction in response.data:
            if (
                stored_reaction["reactants"] == reaction.reactants
                and stored_reaction["products"] == reaction.products
            ):
                return stored_reaction

        offset += batch_size

    raise HTTPException(status_code=404, detail="Matching reaction not found")


@app.post("/reactions/pathway", response_model=List[List[Reaction]])
def reaction_pathway_planning(
    starting_materials: List[Reactant], target_molecule: Product
):
    batch_size = 100
    pathways = []
    queue = [(starting_materials, [])]

    while queue:
        current_materials, current_pathway = queue.pop(0)
        offset = 0

        while True:
            response = (
                supabase.table("reactions")
                .select("*")
                .range(offset, offset + batch_size - 1)
                .execute()
            )
            if not response.data:
                break

            for stored_reaction in response.data:
                if set(stored_reaction["reactants"]).issubset(set(current_materials)):
                    new_pathway = current_pathway + [stored_reaction]
                    new_materials = list(
                        set(current_materials)
                        - set(stored_reaction["reactants"])
                        + set(stored_reaction["products"])
                    )

                    if target_molecule in new_materials:
                        pathways.append(new_pathway)
                    else:
                        queue.append((new_materials, new_pathway))

            offset += batch_size

    if not pathways:
        raise HTTPException(
            status_code=404, detail="Pathway to target molecule not found"
        )

    return pathways


@app.post("/reactions/find_by_reactants", response_model=List[Reaction])
def find_reactions_by_inputs(reactants: List[Reactant]):
    batch_size = 100
    offset = 0
    matching_reactions = []

    while True:
        response = (
            supabase.table("reactions")
            .select("*")
            .range(offset, offset + batch_size - 1)
            .execute()
        )
        if not response.data:
            break

        for stored_reaction in response.data:
            if set(stored_reaction["reactants"]).issubset(set(reactants)):
                matching_reactions.append(stored_reaction)

        offset += batch_size

    if not matching_reactions:
        raise HTTPException(status_code=404, detail="No matching reactions found")

    return matching_reactions


@app.post("/reactions/find_by_products", response_model=List[Reaction])
def find_reactions_by_outputs(products: List[Product]):
    batch_size = 100
    offset = 0
    matching_reactions = []

    while True:
        response = (
            supabase.table("reactions")
            .select("*")
            .range(offset, offset + batch_size - 1)
            .execute()
        )
        if not response.data:
            break

        for stored_reaction in response.data:
            if set(stored_reaction["outputs"]).issubset(set(products)):
                matching_reactions.append(stored_reaction)

        offset += batch_size

    if not matching_reactions:
        raise HTTPException(status_code=404, detail="No matching reactions found")

    return matching_reactions


@app.post("/reactions/calculate_missing_input", response_model=Dict[str, float])
def calculate_missing_input(reaction_id: int, input_moles: Dict[str, float]):
    response = supabase.table("reactions").select("*").eq("_id", reaction_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Reaction not found")

    reaction = response.data[0]
    total_coefficient = sum(input_moles.values())
    missing_input = None

    for input_chemical in reaction["reactants"]:
        if input_chemical["formula"] not in input_moles:
            if missing_input is not None:
                raise HTTPException(
                    status_code=400,
                    detail="More than one input chemical is missing",
                )
            missing_input = input_chemical

    if missing_input is None:
        raise HTTPException(status_code=400, detail="No input chemical is missing")

    missing_coefficient = missing_input["coefficient"]
    missing_moles = total_coefficient / missing_coefficient

    return {missing_input["formula"]: missing_moles}
