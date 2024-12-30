import { fail, type Actions } from '@sveltejs/kit';

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const reactant_formulas = formData.get('reactant_formulas');
		const product_formulas = formData.get('product_formulas');

		if (
			(!reactant_formulas || reactant_formulas === '') &&
			(!product_formulas || product_formulas === '')
		) {
			return fail(400, {
				message: 'Ít nhất một trong hai ô không được để trống',
				missing: true
			});
		}

		if (reactant_formulas !== '' && product_formulas !== '') {
			return {
				status: 200,
				body: {
					message: 'Success'
				},
				showOutput: true
			};
		}

		return {
			showOutput: false
		};
	}
};
