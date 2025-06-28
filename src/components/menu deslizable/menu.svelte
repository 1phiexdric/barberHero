<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import arrow from "./icons/arrow.svg";
  import menuHamburger from "./icons/menu.svg";
  import { config } from './menu.config';

  let title = "Friedrich";
  let menu = config.menu
  let estilos = config.style
  let subMenus: Array<HTMLElement> = $state([])
  let mostrar = $state(false)

  function addClickAction(node: HTMLElement, tieneSubmenu: boolean) {
    if (tieneSubmenu) {
      node.addEventListener("click", () => {
        let subMenu = node.children[1] as HTMLElement;
        subMenus.push(subMenu)
        let arrow = node.querySelector('.menu_arrow') as HTMLElement;
        let height = 0;

        if (subMenu.clientHeight === 0) {
          height = subMenu.scrollHeight;
          arrow.style.transform = 'rotate(0deg)';
        } else {
        arrow.style.transform = 'rotate(-90deg)';
      }

        subMenu.style.height = `${height}px`;
      });
    }
  }
  const deleteStyleHeight = ()=>{
    subMenus.forEach((elemento) => {
      // Aquí puedes manipular cada elemento del subMenus si lo necesitas
      if(elemento.getAttribute('style')){
        elemento.removeAttribute('style')
      }
    })
  }
  onMount(()=>{
    window.addEventListener('resize', ()=>{
      if(window.innerWidth > 800){
        deleteStyleHeight()
      }
    })
    document.documentElement.style.setProperty('--navbar-bg', estilos.backgroundColor)
    document.documentElement.style.setProperty('--navbar-text', estilos.textColor)
    document.documentElement.style.setProperty('--navbar-nesting', estilos.nestingColor)
    document.documentElement.style.setProperty('--navbar-hover', estilos.menuHover)
    document.documentElement.style.setProperty('--hamburger-button-color', estilos.hamburgerBtn)
  })

</script>

<div id="main-container">
  <nav class="menu">
    <section class="menu_container">
      <img src="assets/icon.png" id="menu_logo" alt="" width="100px">

      <ul class="menu_links {mostrar ? 'menu_links--show' : ''}">
        {#each menu as opcion}
          <li class="menu_item">
              <a href={opcion.href} class="menu_link" onclick={()=> mostrar = !mostrar}>{opcion.title}</a>
          </li>
        {/each}
      </ul>
      <button class="menu-toggle" onclick={()=> mostrar = !mostrar} aria-label="Toggle">
      <div class="hamburger" class:open={mostrar}>
        <span></span>
        <span></span>
        <span></span>

</div>
</button>
    </section>
  </nav>
</div>

<style>
  /* Fuente*/
  @import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Red+Rose:wght@300..700&display=swap");

  :global(:root){
    --navbar-bg: rgb(0, 0, 0);
    --navbar-text: black;
    --navbar-nesting: white;
    --navbar-hover: white;
    --hamburger-button-color: white
  }

  #main-container {
    margin: 0;
    padding: 0;
  }
  .menu {
    background-color: var(--navbar-bg);
    color: var(--navbar-text);
    height: 70px;
  }
  .menu_container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 90%;
    max-width: 1200px;
    height: 100%;
    margin: 0 auto;
  }

.menu-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
  }

  .menu_links {
    height: 100%;
    transition: all 0.5s ease-in;
    display: flex;
  }
  .menu_item {
    list-style: none;
    position: relative;
    height: 100%;
    --clip: polygon(0 0, 100% 0, 100% 0, 0 0);
    --arrow-rotate: -90deg;
  }
  .menu_item:hover {
    --clip: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
    --arrow-rotate: 0deg;
  }
  .menu_nesting {
    list-style: none;
    clip-path: var(--clip);
    transition: all 0.3s;
    position: absolute;
    right: 0;
    bottom: 0;
    width: 100%;
    font-size: 1rem;
    transform: translateY(100%);
    background-color: var(--navbar-nesting);
  }
  .menu_arrow {
    transform: rotate(var(--arrow-rotate));
    transition: transform 0.3s;
    display: block;
    margin-left: 3px;
  }
  .menu_link {
    color: var(--navbar-text);
    text-decoration: none;
    padding: 0 30px;
    display: flex;
    height: 100%;
    align-items: center;
  }
  .menu_link:hover {
    background-color: var(--navbar-hover);
  }
  .menu_link--inside {
    padding: 30px 20px;
  }
  .menu_link--inside:hover {
    background-color: #796499;
  }
  button{
    background-color: transparent;
    border: none;
    cursor: pointer;
    width: 25px;
    height: 25px;
  }
  button:active{
    box-shadow: 2px 0px 10px rgb(0, 0, 0, 0.5);
  }


    .hamburger span {
    width: 100%;
    height: 3px;
    background-color: var(--hamburger-button-color);
    border-radius: 5px;
    transition: all 0.3s ease-in-out;
  }

  .hamburger.open span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }
  .hamburger.open span:nth-child(2) {
    opacity: 0;
  }
  .hamburger.open span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
  }
  @media (width < 800px) {

  .hamburger {
  width: 25px;
  height: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
    .menu_links{
      display: none;
    }


        .menu-toggle {
      display: block;
    }

    .menu_link {
      padding: 25px 0;
      padding-left: 30px;
      height: auto;
    }
    .menu_arrow {
      margin-left: auto;
      margin-right: 20px;
      transform: rotate(var(--arrow-rotate));
      transition: transform 0.1s;
    }
    .menu_nesting {
      display: grid;
      position: unset;
      width: 100%;
      transform: translateY(0);
      height: 0;
      transition: height 0.3s ease-in;
    }
    .menu_link--inside {
      width: 90%;
      margin-left: auto;
      border-left: 1px solid #7c7c7c;
    }
    .menu_item {
      --clip: 0;
      overflow: hidden;
    }
  }

    @media (width < 800px) {

  .hamburger {
  width: 25px;
  height: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
    .menu_links{
        position: fixed;
        height: calc(100vh - 70px);
        max-width: 400px;
        width: 100%;
        top: 70px;
        bottom: 0;
        right: 0;
        background-color: white;
        overflow-y: auto;
        z-index: 1000;
        display: grid;
        grid-auto-rows: max-content;
        transform: translateX(100%);
    }

    .menu_links--show{
        transform: unset;
        width: 100%;
    }

        .menu-toggle {
      display: block;
    }

    .menu_link {
      padding: 25px 0;
      padding-left: 30px;
      height: auto;
    }
    .menu_arrow {
      margin-left: auto;
      margin-right: 20px;
      transform: rotate(var(--arrow-rotate));
      transition: transform 0.1s;
    }
    .menu_nesting {
      display: grid;
      position: unset;
      width: 100%;
      transform: translateY(0);
      height: 0;
      transition: height 0.3s ease-in;
    }
    .menu_link--inside {
      width: 90%;
      margin-left: auto;
      border-left: 1px solid #7c7c7c;
    }
    .menu_item {
      --clip: 0;
      overflow: hidden;
    }
  }
</style>
