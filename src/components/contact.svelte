<script>
    import Sectionwrapper from "./sectionwrapper.svelte";
    // ... otras importaciones si las tienes
</script>


    <h2 class="text-4xl font-bold text-center mb-8">Encuéntranos Aquí</h2>
    <div class="map-container">
        <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3976.600989512396!2d-74.0886650852377!3d4.65991879660235!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f9a35e40a0001%3A0x7d0e4a7b7e0e4a7b!2sPlaza%20de%20Bol%C3%ADvar!5e0!3m2!1ses!2sco!4v1678888888888!5m2!1ses!2sco"
            width="600"
            height="450"
            style="border:0;"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            title="Ubicación de la Barbería"
        ></iframe>
    </div>
    <div class="text-center mt-6" id="contact">
        <p class="text-lg">¡Te esperamos en [Direccion]!</p>
        <p class="text-lg">Horario: 8:30am a 5pm de lun a vie</p>
        <p class="text-lg">Teléfono: +58412111111</p>
        <button class="specialBtnDark">
        <p class="text-base sm:text-lg md:text-xl">¡Haz tu reserva! &rArr;</p>
    </button>
    </div>


<style>
    /* ... Tus estilos existentes para .background, .servicio-item, etc. ... */
    .specialBtnDark{
        border: 1px solid black;
    }
    .map-container {
        width: 100%; /* El contenedor ocupa todo el ancho disponible */
        max-width: 1200px; /* O el max-width que uses para tu contenido principal */
        margin: 0 auto; /* Centra el contenedor del mapa */
        height: 450px; /* Altura deseada para el mapa */
        overflow: hidden; /* Por si acaso */
        border-radius: 8px; /* Bordes redondeados para el mapa */
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); /* Sombra sutil */
    }

    .map-container iframe {
        width: 100%; /* El iframe se estira para llenar el contenedor */
        height: 100%; /* El iframe se estira para llenar el contenedor */
        border: none; /* Elimina el borde predeterminado del iframe */
    }
</style>