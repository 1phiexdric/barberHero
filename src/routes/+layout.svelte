<script lang="ts">
	import '../app.css';
  import Footer from '../components/footer.svelte';
	
	let { children } = $props();
</script>

{@render children()}
<Footer/>