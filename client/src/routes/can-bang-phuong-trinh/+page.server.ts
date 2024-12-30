import { fail, type Actions } from '@sveltejs/kit';

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const reactant_formulas = formData.get('reactant_formulas');
		const product_formulas = formData.get('product_formulas');

		if (!reactant_formulas || reactant_formulas === '') {
			return fail(400, {
				message: 'Không được để trống chất tham gia',
				reactant_formulas,
				missing: true
			});
		}

		if (!product_formulas || product_formulas === '') {
			return fail(400, {
				message: 'Không được để trống chất sản phẩm',
				product_formulas,
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
