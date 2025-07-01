<script lang="ts">
  let y: number = $state(0)
  let innerHeight: number = $state(0)
  let innerWidth: number = $state(0)
  function goTop(){
	document.body.scrollIntoView()
  }
</script>
<!-- 
	Usé 'right-0' y 'justify-end' para pegar el botón a la derecha.
	'fixed bottom-0 right-0' posiciona el contenedor en la esquina inferior derecha.
	'justify-end' en el flex asegura que el contenido se alinee a la derecha.
-->
<div class="fixed bottom-0 right-0 w-full flex justify-end p-10 z-[10] duration-200
	{y > 0 ? 'opacity-100 pointer-events-auto' : 'pointer-events-none opacity-0'}">
	<button onclick={goTop} aria-label="to-top" class="rounded-full bg-slate-900 px-3 sm:px-4 hover:bg-slate-800 cursor-pointer">
		<i class="fa-solid fa-arrow-up grid place-items-center aspect-square"></i>
	</button>
</div>
<svelte:window bind:scrollY={y} bind:innerHeight bind:innerWidth/>