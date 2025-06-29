<script>
  import Sectionwrapper from "./sectionwrapper.svelte";
  import { blur, fade } from "svelte/transition";
  let showMore = $state(false)
  let faqs = [
        {
            question: "¿Qué servicios ofrecen en la barbería?",
            ans: "Ofrecemos una amplia gama de servicios, incluyendo cortes de cabello clásicos y modernos, afeitado tradicional con navaja, arreglo de barba, tratamientos faciales para hombres y limpieza de cejas.",
        },
        {
            question: "¿Necesito una cita previa o puedo ir sin cita?",
            ans: "Recomendamos encarecidamente reservar una cita para asegurar tu lugar y reducir el tiempo de espera. Aunque aceptamos clientes sin cita previa, la atención estará sujeta a la disponibilidad del momento.",
        },
        {
            question: "¿Cuáles son sus horarios de atención?",
            ans: "Nuestro horario es de [Día] a [Día] de [Hora de apertura] a [Hora de cierre], y los [Días de fin de semana, si aplica] de [Hora de apertura] a [Hora de cierre]. Te invitamos a consultar nuestra sección de contacto para los horarios exactos y días festivos.",
        },
        {
            question: "¿Cuánto tiempo dura un corte de cabello o un afeitado?",
            ans: "Un corte de cabello estándar suele durar entre 30 y 45 minutos. Un afeitado tradicional o arreglo de barba puede tomar entre 20 y 30 minutos, dependiendo de la complejidad y los servicios adicionales solicitados.",
        },
        {
            question: "¿Utilizan productos específicos para el cuidado del cabello y la barba?",
            ans: "Sí, utilizamos únicamente productos de alta calidad, seleccionados por nuestros expertos para el cuidado masculino, que nutren y protegen tanto el cabello como la piel. También tenemos algunos a la venta en la barbería.",
        },
        {
            question: "¿Ofrecen servicios para niños?",
            ans: "¡Claro que sí! Contamos con barberos experimentados en cortes de cabello para niños, asegurando una experiencia cómoda y divertida para los más pequeños.",
        },
        {
            question: "¿Cómo puedo reservar una cita?",
            ans: "Puedes reservar tu cita directamente a través de nuestro sistema de reserva online haciendo clic en el botón 'Reservar Cita' en nuestra página web, o llamando a nuestro número de teléfono [Tu número de teléfono].",
        },
        {
            question: "¿Tienen algún programa de fidelidad o descuentos?",
            ans: "Sí, preguntanos sobre nuestro programa de fidelidad al visitarnos. Recompensamos a nuestros clientes habituales con descuentos especiales y promociones exclusivas.",
        },
        {
            question: "¿Puedo comprar productos en la barbería?",
            ans: "¡Absolutamente! Contamos con una selección de productos premium para el cuidado del cabello, barba y piel, los mismos que usamos en nuestros servicios, disponibles para que los lleves a casa.",
        },
        {
            question: "¿Qué medidas de higiene y seguridad toman?",
            ans: "La higiene y seguridad son nuestra máxima prioridad. Seguimos estrictos protocolos de desinfección de herramientas y estaciones de trabajo, y nuestros barberos utilizan equipos de protección personal para garantizar un ambiente seguro para todos.",
        },
    ];
</script>

<Sectionwrapper id="FQAs">
  <div
    class="flex flex-col gap-10 sm:gap-5
    py-20 flex-1 items-center justify-center container"
  >
    <div class="flex flex-col gap-2">
      <h2
        class="text-4xl sm:text-5xl md:text-6xl max-w-[1000px] mx-auto w-full
     text-center "
      style="margin-top: 10px;"  
    >
        Preguntas Frecuentes
      </h2>
      <div id="separador">
        </div>
    </div>
    <div
      class="flex flex-col gap-8 sm:gap-10
    md:gap-14 w-full fqas-container"
    >
      {#each !showMore? faqs.slice(0, 2): faqs as faq}
                <div
                    class="flex flex-col gap-2 text-left max-w-[800px] w-full mx-auto relative p-4 px-6 fqa"
                 in:fade={{ duration: 300 }} out:fade={{ duration: 300 }}>
                    <div
                        class="absolute top-0 left-0 w-1/3 h-[1px] bg-slate-950 -translate-x-4"
                    ></div>
                    <div
                        class="absolute top-0 left-0 h-2/3 w-[1px] bg-slate-950 -translate-y-4"
                    ></div>
                    <h4 class="text-lg sm:text-xl md:text-2xl pt-2 opens-sans">
                        {faq.question}
                    </h4>
                    <p class="pl-2">{faq.ans}</p>
                </div>
            {/each}
            <button id="show-more" onclick={()=> showMore = !showMore}>
              {#if !showMore}
                Mostrar Más
              {:else}
                Mostrar Menos
              {/if}
            </button>
    </div>
  </div>
</Sectionwrapper>
<style>
  .container {
    margin: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* Remove border if not needed */
    /* border: 1px solid red; */
    width: 80%;
    max-width: max-content;
  }

  .fqas-container{
    padding: 10px;
    width: 100%;
  }

  .fqa{
    padding-left: 5px;
  }

  #show-more{
    border: 1px solid black;
    border-radius: 0;
    min-width: 35%;
    max-width: 60%;
    margin: auto;
    cursor: pointer;
    outline: none;
  }
  /* Cambia el borde a gris después de presionar el botón */
  #show-more::after {
    border: 1.5px solid #888;
    outline: 2px solid #888;
  }
  #separador{
    width: 40%;
    border-bottom: 1px solid black;
    margin: 0 auto 20px;
  }

  @media(width<800){
    .container{
      width: 70%;
    }
    .fqas-container{
      width: 70%;
    }
  }

</style>
