export interface Element {
	_id?: number;
	symbol: string;
}

export interface Chemical {
	_id?: number;
	formula: string;
	coefficient: number | null;
}

export interface Reaction {
	_id?: number;
	reactants: Chemical[];
	products: Chemical[];
	conditions: string[] | null;
}
