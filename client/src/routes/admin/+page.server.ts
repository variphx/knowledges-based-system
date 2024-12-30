import type { Actions } from '@sveltejs/kit';
import type { Reaction } from '$lib/schema';

const reactions: Reaction[] = [
	{
		_id: 1,
		reactants: [
			{ formula: 'H2', coefficient: 2 },
			{ formula: 'O2', coefficient: 1 }
		],
		products: [{ formula: 'H2O', coefficient: 2 }],
		conditions: ['heat']
	}
];

const get = async () => {
	return {
		status: 200,
		body: reactions
	};
};

const post = async () => {
	return {
		status: 201,
		body: {
			message: 'Reaction created'
		}
	};
};

const put = async () => {
	return {
		status: 200,
		body: {
			message: 'Reaction updated'
		}
	};
};

const del = async () => {
	return {
		status: 200,
		body: {
			message: 'Reaction deleted'
		}
	};
};

export const actions: Actions = {
	read: get,
	create: post,
	update: put,
	delete: del
};
