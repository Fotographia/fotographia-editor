const show_brightness = (event) => {
    event.preventDefault()
    const form = document.getElementById("brightness-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}


const brightness = (event) => {
    event.preventDefault()
    const queryString = window.location.search
    
    var bright_value = document.getElementById("brightness_value").value
    const body = JSON.stringify({bright_value})
    
    fetch(`/api/brightness${queryString}`, {
        method: "POST",
        body,
        headers:{
            'Content-type': 'application/json'
        },
    })
    .then(response => {
        reloadImage()
    })
    .error( err => 
        alert(err)
    )
}