<script>
    import Menu from "./menu deslizable/menu.svelte";
    import Sectionwrapper from "./sectionwrapper.svelte";
  import Stars from "./Stars.svelte";
</script>

<div class="background">
    <Sectionwrapper id="header">
        <Menu/>
<div class="flex flex-col gap-10 flex-1 items-center justify-center pb-10 md:pb-14">
      <h1 class="text-5xl sm:text-6xl md:text-7xl lg:text-8xl max-w-[1200px]
      mx-auto w-full text-center font-semibold text-white">
      Tu momento. Tu estilo. Tu barbería.
    </h1>
    <p class="text-xl sm:text-2xl md:text-3xl text-center max-w-[1000px] mx-auto w-full text-white">
  Deja de pensar en tu look, ¡y ven a crearlo! En nuestra barbería, tienes a tu disposición a <span class="italic">expertos en estilo, las últimas tendencias, técnicas precisas</span> y mucho, mucho más.
</p>
<button class="specialBtnDark">
        <p class="text-base sm:text-lg md:text-xl">¡Haz tu reserva! &rArr;</p>
    </button>
<Stars/>

    </div>
    </Sectionwrapper>
</div>

<style>
    .background {
        height: 100vh;
        /* La imagen de fondo */
        background-image:
            /* Primer degradado: Un overlay oscuro que se superpone a la imagen. */
            /* Puedes ajustar el 'rgba(0, 0, 0, 0.5)' para controlar la oscuridad. */
            /* El 0.5 es la opacidad (50%). Cero es transparente, 1 es sólido. */
            linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7)),
            /* Segundo elemento: Tu imagen de fondo. */
            url('assets/background.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }
</style>
