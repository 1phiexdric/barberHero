<script>
  import Sectionwrapper from "./sectionwrapper.svelte";
  import ServicesCard from "./servicesCard.svelte";


</script>
<Sectionwrapper id="services">
<div class="flex flex-col gap-10 sm:gap-14 md:gap-24
    flex-1 items-center justify-center pb-10 md:pb-14 margin-top">
    <div class="flex flex-col gap-2">
        <h2 class="text-4xl sm:text-5xl md:text-6xl max-2-[1000px] mx-auto
        w-full text-center">SERVICIOS</h2>
        <div id="separador">
        </div>
        <p class="opacity-60 text-base smLtext-lg md:text-xl text-center">
            DESCUBRE Y RESERVA NUESTROS SERVICIOS EXCLUSIVOS, DISEÑADOS PARA TI
¡TRANSFORMA TU ESTILO CON ASESORÍA PERSONALIZADA!
        </p>
</div>
<ServicesCard/>
</div>
</Sectionwrapper>

<style>
    #separador{
        border-bottom: 1px solid black;
        width: 30%;
        margin: 10px auto;
    }
    
</style>