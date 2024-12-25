from pydantic import BaseModel, PositiveInt
import re


class Element(BaseModel):
    _id: int
    symbol: str


class Chemical(BaseModel):
    _id: int | None
    formula: str
    _parsed_formula: tuple[Element]
    coefficient: PositiveInt | None  # Ensure coefficient is a positive integer

    def __init__(self, **data):
        super().__init__(**data)
        self._parsed_formula = self.parse_formula()

    def parse_formula(self):
        elements = []
        pattern = re.compile(r"([A-Z][a-z]?)(\d*)")

        for match in pattern.findall(self.formula):
            symbol, coeff = match
            coefficient = int(coeff) if coeff else 1
            elements.append(Element(symbol=symbol, coefficient=coefficient))

        self.formula = "".join(
            f'{el.symbol}{el.coefficient if el.coefficient > 1 else ""}'
            for el in elements
        )

        return tuple(elements)

    def __eq__(self, other):
        return self._parsed_formula == other._parsed_formula

    def __lt__(self, other):
        return self._parsed_formula < other._parsed_formula

    def __gt__(self, other):
        return self._parsed_formula > other._parsed_formula

    def __le__(self, other):
        return self._parsed_formula <= other._parsed_formula

    def __ge__(self, other):
        return self._parsed_formula >= other._parsed_formula

    def __hash__(self):
        return self._parsed_formula.__hash__()


class Reactant(Chemical):
    pass


class Product(Chemical):
    pass


class Reaction(BaseModel):
    _id: int | None
    reactants: list[Reactant]
    conditions: list[str] | None
    products: list[Product]

    def __init__(self, **data):
        super().__init__(**data)
        self.reactants.sort()
        self.products.sort()

        if self.conditions:
            self.conditions.sort()
