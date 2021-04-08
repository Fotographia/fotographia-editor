const show_gamma_correction = (event) => {
    event.preventDefault()
    const form = document.getElementById("gamma-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}


const gamma_correction = (event) => {
    event.preventDefault()

    const gamma_value = document.getElementById("gamma_value").value
    const body = JSON.stringify({gamma_value})

    console.log("Test. OK?")
    const queryString = window.location.search
    fetch(`/api/gamma-correction${queryString}`,{
        method: "POST",
        body,
        headers:{'content-type': 'application/json'}
    })
    .then(response => {
        console.log("Fetch")
        reloadImage()
    })
    .error( err => 
        alert(err)
    )
}