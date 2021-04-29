const show_smooth = (event) => {
    event.preventDefault()
    const form = document.getElementById("smooth-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}


const smooth = (event) => {
    event.preventDefault()
    const queryString = window.location.search
    
    var smooth_val = document.getElementById("smooth_value").value
    const body = JSON.stringify({smooth_val})
    
    fetch(`/api/smooth${queryString}`, {
        method: "POST",
        body,
        headers:{
            'Content-type': 'application/json'
        },
    })
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}