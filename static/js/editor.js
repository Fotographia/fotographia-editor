window.onbeforeunload = (() => {
    // show warning dialog
    return ""
})

// Variables
const canvas = document.querySelector(".zoomable")
const zoomInButton = document.getElementById("zoomIn")
const zoomOutButton = document.getElementById("zoomOut")
let x = window.innerWidth / 2;
let y = window.innerHeight / 2;

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
    pz.smoothZoom(x, y, 1.2)
})

zoomOutButton.addEventListener('click', (e) => {
    e.preventDefault()
    pz.smoothZoom(x, y, 0.8)
})