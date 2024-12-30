<script lang="ts">
	import '../app.css';
	const menuItems = [
		{ href: '/can-bang-phuong-trinh', text: 'Cân bằng phương trình' },
		{ href: '/tra-cuu-phuong-trinh', text: 'Tra cứu phương trình' },
		{ href: '/chuoi-phan-ung', text: 'Chuỗi phản ứng' },
		{ href: '/bao-toan-vat-chat', text: 'Bảo toàn vật chất' },
		{ href: '/hieu-suat-phan-ung', text: 'Hiệu suất phản ứng' },
		{ href: '/doi-don-vi', text: 'Đổi đơn vị' }
	];
	let { children } = $props();
</script>

<div class="flex h-screen bg-gradient-to-r from-green-300 via-blue-300 to-purple-300">
	<!-- Sidebar -->
	<div class="w-64 overflow-hidden bg-gray-100 shadow-lg">
		<div
			class="flex h-16 items-center bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-300 p-4 text-xl font-bold text-gray-800"
		>
			Các bài toán
		</div>
		<script lang="ts">
		</script>

		<ul class="mt-4">
			{#each menuItems as item}
				<li
					class="transform rounded-lg p-4 transition duration-300 ease-in-out hover:scale-105 hover:bg-gray-300 hover:text-gray-800 hover:shadow-lg"
				>
					<a href={item.href} class="block h-full w-full text-lg">{item.text}</a>
				</li>
			{/each}
		</ul>
	</div>

	<!-- Main content -->
	<div class="flex flex-1 flex-col">
		<!-- Header -->
		<header class="flex h-16 items-center bg-white p-4 shadow-md">
			<h1 class="text-2xl font-bold text-gray-800">Hệ giải bài toán hóa học</h1>
		</header>

		<!-- Content -->
		<main class="flex-1 overflow-auto p-4">
			{@render children()}
		</main>
	</div>
</div>
