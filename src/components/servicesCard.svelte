<script>
    let servicios = [
        {
            nameService: "Barba",
            imgUrl: 'assets/services/barba.jpg'
        },
        {
            nameService: "Cabello",
            imgUrl: 'assets/services/cabello.jpg'
        },
        {
            nameService: "Cuidado Personal",
            imgUrl: 'assets/services/cuidado-personal.jpg'
        },
        {
            nameService: "Rostro",
            imgUrl: 'assets/services/rostro.jpg'
        },
    ]
</script>

<div id="contenedor">
    {#each servicios as servicio }
        <div class="servicio-item"> 
            <div class="imagen-wrapper"> <img src={servicio.imgUrl} alt={servicio.nameService}>
            </div>
            <p>{servicio.nameService}</p>
        </div>
    {/each}
</div>

<style>
    #contenedor {
        display: flex;
        flex-wrap: wrap; 
        justify-content: space-around; 
        gap: 1rem; 
        padding: 1rem;
        cursor: pointer;
    }
    .servicio-item {
        border: 2px solid black;
        min-width: calc(25% - 1.5rem); 
        max-width: calc(25% - 1.5rem);
        display: flex;
        flex-direction: column;
        text-align: center; 
    }

    /* ESTO ES LO NUEVO: Estilos cuando el cursor está encima */
    .servicio-item:hover {
        background-color: #e0e0e0;
        border-color: #007bff; /* Un azul, por ejemplo */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Sombra sutil para efecto de elevación */
        transform: translateY(-5px); /* Pequeño efecto de elevación */
        transition: all 0.3s ease; /* Transición para todos los cambios */
    }

    @media (max-width: 768px) {
        .servicio-item {
            min-width: calc(50% - 1rem); 
            max-width: calc(50% - 1rem);
        }
    }

    @media (max-width: 480px) {
        .servicio-item {
            min-width: calc(100% - 1rem);
            max-width: calc(100% - 1rem);
        }
    }

    .imagen-wrapper {
        width: 100%; 
        height: 200px; 
        overflow: hidden; 
        display: flex; 
        justify-content: center;
        align-items: center;
    }

    .servicio-item img {
        width: 100%; 
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .servicio-item p {
        padding: 0.5rem; 
        font-weight: bold;
        background-color: white;
    }
</style>