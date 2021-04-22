const show_sketch = (event) => {
    event.preventDefault()
    const form = document.getElementById("sketch-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}

const sketch = (event) => {
    event.preventDefault()
    
    const skmode = document.getElementById("sketch_mode").value
    const skdensity = document.getElementById("sketch_density").value
    const skshading = document.getElementById("sketch_shading").value
    
    const body = JSON.stringify({skmode,skdensity,skshading})

    const queryString = window.location.search

    fetch(`/api/sketch${queryString}`,{
            method: "POST",
            body,
            headers:{'content-type': 'application/json'},
        }
    )
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}