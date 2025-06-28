<script>
  import Sectionwrapper from "./sectionwrapper.svelte";
  import Slider from "./slider/slider.svelte";
    let sliderBody = [
    {
        subtitle: "Carlos Ramírez",
        reviews: "¡Absolutamente encantado con mi nuevo look! El corte fue preciso y el afeitado, una obra de arte. Sin duda, mi barbería de confianza de ahora en adelante.",
        imgUrl: null // Asume que foto1 es una variable definida previamente o un path
    },
    {
        subtitle: "María Fernanda Díaz",
        reviews: "Aunque es una barbería, me sorprendió gratamente la atención y el cuidado. Mi pareja siempre sale impecable y feliz. Un ambiente excelente y profesionales top.",
        imgUrl: null // Asume que foto2 es una variable definida previamente o un path
    },
    {
        subtitle: "Javier 'El Lobo' García",
        reviews: "Necesitaba un cambio radical y lo obtuve. Me asesoraron perfectamente con mi barba y mi cabello. Salí sintiéndome renovado y con mucho estilo.",
        imgUrl: null // Asume que foto3 es una variable definida previamente o un path
    },
    {
        subtitle: "Roberto Gómez",
        reviews: "Siempre busco la perfección en mi corte y la encontré aquí. La atención al detalle es increíble. ¡Altamente recomendado para quienes valoran un buen servicio!",
        imgUrl: null // Asume que foto4 es una variable definida previamente o un path
    },
    {
        subtitle: "Ana Sofía Castro",
        reviews: "Llevé a mi hijo y no solo le hicieron un corte moderno y genial, sino que lo hicieron sentir muy cómodo. Volveremos, sin duda.",
        imgUrl: null // Asume que foto5 es una variable definida previamente o un path
    }
];
</script>
<Sectionwrapper id="reviews">
<div class="flex flex-col gap-10 sm:gap-14 md:gap-24
    flex-1 items-center justify-center pb-10 md:pb-14 margin-top bg-black text-white margin">
    <div class="flex flex-col gap-2">
        <h2 class="text-4xl sm:text-5xl md:text-6xl max-2-[1000px] mx-auto
        w-full text-center">REVIEWS</h2>
        <div id="separador">
        </div>
        <Slider {sliderBody}/>
        
</div>
</Sectionwrapper>

<style>
    .margin{
        padding: 40px 0;
    }
    #separador{
        border-bottom: 1px solid white;
        width: 30%;
        margin: 10px auto;
    }
</style>