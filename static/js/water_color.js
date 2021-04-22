const show_watercolor = (event) => {
    event.preventDefault()
    const form = document.getElementById("water-color-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}

const water_color = (event) => {
    event.preventDefault()
    
    const watercolor_val = document.getElementById("watercolor_value").value
    const body = JSON.stringify({watercolor_val})

    const queryString = window.location.search

    fetch(`/api/water-color${queryString}`,{
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