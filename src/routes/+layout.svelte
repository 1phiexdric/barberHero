<script lang="ts">
	import '../app.css';
  import Footer from '../components/footer.svelte';
  import Menu from '../components/menu deslizable/menu.svelte';
	import { fade, blur } from 'svelte/transition';
  let { children } = $props();
	let y:number = $state(0)
	let outerHeight:number = $state(0)	
</script>

{@render children()}
{#if y> outerHeight}
	<div class="bg-white fixed top-0 left-0 w-full flex flex-col z-20 px-4" in:fade={{ duration: 200 }} out:blur={{duration:200}}>
		<Menu/>
	</div>
{/if}
<svelte:window bind:scrollY={y} bind:outerHeight />
<Footer/>