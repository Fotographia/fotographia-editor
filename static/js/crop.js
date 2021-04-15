const show_crop = (event) => {
    event.preventDefault()
    const form = document.getElementById("crop-form")
    
    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}

const crop = (event) => {
    event.preventDefault()

    const X = document.getElementById("X_value").value
    const Y = document.getElementById("Y_value").value
    const xOffset = document.getElementById("xOffset_value").value
    const yOffset = document.getElementById("yOffset_value").value

    const body = JSON.stringify({X,Y,xOffset,yOffset})

    const queryString = window.location.search
    fetch(`/api/crop${queryString}`,{
            method: "POST",
            body,
            headers:{'content-type': 'application/json'}
        }
     )
    .then(response => {
        reloadImage()
        getResolution()
    })
    .error( err => 
        alert(err)
    )
}