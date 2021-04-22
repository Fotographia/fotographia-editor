const show_oilpaint = (event) => {
    event.preventDefault()
    const form = document.getElementById("oilpaint-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}


const oilPaint = (event) => {
    event.preventDefault()
    
    const oillevel_value = document.getElementById("oilpaint_value").value
    const body = JSON.stringify({oillevel_value})

    const queryString = window.location.search

    fetch(`/api/oil-paint${queryString}`, {
        method: "POST",
        body,
        headers:{'content-type': 'application/json'},
    })
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}
