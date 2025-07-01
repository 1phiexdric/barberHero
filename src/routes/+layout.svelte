<script lang="ts">
	import '../app.css';
  import BtnToTop from '../components/BtnToTop.svelte';
  import Footer from '../components/footer.svelte';
  import Menu from '../components/menu deslizable/menu.svelte';
	
  let { children } = $props();
	
</script>

<Menu/>
<BtnToTop/>
{@render children()}

<Footer/>