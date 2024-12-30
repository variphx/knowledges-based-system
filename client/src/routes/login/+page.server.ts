import type { Actions } from '@sveltejs/kit';

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const username = formData.get('username');
		const password = formData.get('password');

		// Perform your authentication logic here
		if (username === 'admin' && password === 'password') {
			return {
				status: 200,
				body: {
					message: 'Login successful'
				}
			};
		} else {
			return {
				status: 401,
				body: {
					message: 'Invalid username or password'
				}
			};
		}
	}
};
