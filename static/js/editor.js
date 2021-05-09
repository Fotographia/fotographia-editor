window.onbeforeunload = (() => {
    // show warning dialog
    return ""
})

// Variables
const canvas = document.querySelector(".zoomable")
const zoomInButton = document.getElementById("zoomIn")
const zoomOutButton = document.getElementById("zoomOut")
let centerX = window.innerWidth / 2;
let centerY = window.innerHeight / 2;

// Instantiate panzoom object with properties
const pz = panzoom(canvas, {
    bounds: true,
    zoomSpeed: 0.055,           // 6.5% per mouse wheel event
    maxZoom: 3,
    minZoom: 0.1,
    smoothScroll: false,        // disable momentum
    zoomDoubleClickSpeed: 1,    // disable double click zoom

    initialX: 500,
    initialY: 200,
    initialZoom: 0.4,
})

// Controlbar zoom buttons
zoomInButton.addEventListener('click', (e) => {
    e.preventDefault()
    pz.smoothZoom(centerX, centerY, 1.2)
})

zoomOutButton.addEventListener('click', (e) => {
    e.preventDefault()
    pz.smoothZoom(centerX, centerY, 0.8)
})

// Toolbar menu
const acc = document.getElementsByClassName("toolbar__accordion");
let i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    const panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}