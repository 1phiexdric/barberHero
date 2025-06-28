<script>
    import Contact from "./contact.svelte";
</script>
<footer
        class="py-16 sm:py-20 md:py-24 px-4 md:px-8"
>
        <div class="flex flex-col gap-8 md:col-span-2"> <!-- gap aumentado -->
                <Contact/>
        </div>
        <div class="social">

            <p class="opacity-60 font-semibold text-center my-8">&copy; 2025 BarberHero LTD. TODOS LOS DERECHOS RESERVADOS.</p> <!-- margen vertical añadido -->
            <div class="social-icons mt-8"> <!-- margen superior añadido -->
                    <a href=""><i class="fa-brands fa-instagram"></i></a>
                    <a href=""><i class="fa-brands fa-facebook"></i></a>
                    <a href=""><i class="fa-brands fa-twitter"></i></a>
                    <a href="mailto:info@barberhero.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
                    <a href=""><i class="fa-brands fa-linkedin"></i></a>
                    <a href=""><i class="fa-brands fa-youtube"></i></a>
            </div>
        </div>
</footer>
<style>
        footer{
                padding: 30px 10px;
        }
        .social{
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .social-icons{
                display: flex;
                width: 70%;
                justify-content: space-between;
                margin: auto;
        }

        .social-icons a{
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: #000;
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                /* Opcional: quitar el borde rojo */
                border: none;
        }

        .social-icons a i{
                font-size: 22px;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                height: 100%;
        }
</style>