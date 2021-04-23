window.onbeforeunload = (() => {
    // show warning dialog
    return ""
})

// Get canvas element
const element = document.querySelector(".zoomable")

// Instantiate panzoom with properties
panzoom(element,{
    bounds: true,
    zoomSpeed: 0.055, // 6.5% per mouse wheel event
    maxZoom: 3,
    minZoom: 0.1,
    smoothScroll: false, // disable momentum

    initialX: 500,
    initialY: 200,
    initialZoom: 0.4,
})