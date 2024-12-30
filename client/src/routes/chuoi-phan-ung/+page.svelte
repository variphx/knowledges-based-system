<script lang="ts">
	import type { ActionData } from './$types';
	import InputForm from './InputForm.svelte';

	let { form }: { form: ActionData } = $props();
</script>

<div
	class="mx-auto my-4 max-w-2xl rounded-lg bg-white bg-opacity-75 p-6 shadow-lg backdrop-blur-md"
>
	<h2 class="text-center text-3xl font-extrabold text-gray-800">
		✨ Tìm chuỗi phản ứng hóa học ✨
	</h2>
</div>

<div class="flex min-h-screen items-center justify-center overflow-hidden py-12">
	<InputForm {form} />
	{#if form?.showOutput}
		<div
			class="ml-4 max-h-full w-1/2 max-w-full overflow-auto rounded-lg bg-gray-100 p-8 shadow-lg"
		>
			<h3 class="mb-4 text-xl font-bold">Kết quả</h3>
			<!-- Output content goes here -->
			<p>{form?.body?.message}</p>
		</div>
	{/if}
</div>
