<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<div
	class={`transition-all duration-500 ${form?.showOutput ? 'w-1/2' : 'w-3/4'} max-h-full max-w-full overflow-auto rounded-lg bg-white p-8 shadow-lg`}
>
	<form method="post" use:enhance class="space-y-4">
		{#if form?.missing}
			<div class="text-sm font-semibold text-red-500">*{form.message}</div>
		{/if}
		<div>
			<label for="reactant_formulas" class="block text-sm font-medium text-gray-700">
				Chất phản ứng
				<input
					type="text"
					id="reactant_formulas"
					name="reactant_formulas"
					class="mt-1 block w-full rounded-md border border-gray-300 p-2"
				/>
			</label>
		</div>
		<div>
			<label for="product_formulas" class="block text-sm font-medium text-gray-700">
				Chất sản phẩm
				<input
					type="text"
					id="product_formulas"
					name="product_formulas"
					class="mt-1 block w-full rounded-md border border-gray-300 p-2"
				/>
			</label>
		</div>
		<button
			type="submit"
			class="w-full rounded-md bg-blue-500 px-4 py-2 font-semibold text-white hover:bg-blue-700"
			>Tìm chuỗi phản ứng</button
		>
	</form>
</div>
