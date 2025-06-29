<script lang="ts">
    import arrowleft from './assets/arrow-left.svg'
    import arrowrigth from './assets/arrow-rigth.svg'
    import user from "./assets/user.png"
    let { sliderBody} = $props()
    

    let current = $state(0)
    function changePosition(n:number){
        current = current + n
        if(current >= sliderBody.length){
            current=0
        }
        if(current < 0){
            current = sliderBody.length - 1;
        }
    }

</script>
<div id="main-container">
    <section class="slider">
        <div class="slider_container container">
            <img src="{arrowleft}" alt="flecha izquierda" class="slider_arrow"
            id="before" bind:this={arrowBefore} onclick={()=>changePosition(-1)}>
            {#each sliderBody as item, index}
            <section class="slider_body {index === current ? 'slider_body--show' : ''}">
                <div class="slider_text">
                    <h2 class="subtitle">{item.subtitle}</h2>
                <p class="slider_reviews">
                    {item.reviews}
                </p>
                </div>
                <figure class="slider_picture">
                    <img src="{item.imgUrl ? item.imgUrl: user}" alt="foto" class="slider_img">
                </figure>
            </section>
            
            {/each}

            <img src="{arrowrigth}" alt="flecha derecha" class="slider_arrow" id="then" onclick={()=> changePosition(1)}>
        </div>
    </section>
</div>
<style>

@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap');

#main-container{
    font-family: "Raleway";
}

.container{
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
    overflow: hidden;
}

.slider{
    background-color: black;
    padding: 40px 0;
}

.slider_container{
    display: grid;
    grid-template-columns: 50px 1fr 50px;
    align-items: center;
    gap: 1em;
}

.slider_body{
    grid-column: 2/3;
    grid-row: 1/2;
    opacity: 0;
    pointer-events: none;
    display: grid;
    background-color: black;
    grid-template-columns: 1fr max-content;
    align-items: center;
    transition: opacity 0.9s;
}

.slider_body--show{
    opacity: 1;
    pointer-events: unset;
}

.slider_text{
    max-width: 600px;
}

.subtitle{
    font-size: 2.5rem;
    margin-bottom: 20px;
}

.slider_reviews{
    font-weight: 300;
    font-size: 20px;
    line-height: 1.7;
}



.slider_img{
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    display: block;
    margin: auto;
    box-shadow: 0 2px 60px 0 rgba(128,128,128,0.3);
}

.slider_arrow{
    cursor: pointer;
    width: 90%;
}

.slider_arrow:nth-of-type(2){
    justify-self: end;
}
@media(width<750px){
    .slider_body{
        grid-template-columns: 1fr;
        grid-template-rows: max-content 1fr;
        gap: 1em;
    }

    .slider_picture{
        grid-row: 1/2;
    }
    .slider_img{
        width: 210px;
        height: 210px;
    }
}

@media(width<425px){
    .slider_container{
        grid-template-columns: 25px 1fr 25px;

    }
    .slider_arrow{
        width: 100%;

    }
    .slider_img{
        width: 180px;
        height: 180px;
    }
    .subtitle{
        text-align: center;
        font-size: 2rem;
        margin-bottom: 15px;
    }
    .slider_reviews{
        font-size: 1rem;
        line-height: 1.6;
    }
}

</style>