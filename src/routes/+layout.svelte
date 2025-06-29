<script lang="ts">
	import '../app.css';
  import Footer from '../components/footer.svelte';
  import Menu from '../components/menu deslizable/menu.svelte';
	
  let { children } = $props();
	
</script>

<Menu/>
{@render children()}

<Footer/>