const show_crop = (event) => {
    event.preventDefault()
    const form = document.getElementById("crop-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}

fetch(`/api/resolution${queryString}`)
    .then(response => response.json())
    .then(data => {
        const width = document.getElementById("width")
        width.innerHTML = data.width
        
        const height = document.getElementById("height")
        height.innerHTML = data.height
    })

const crop = (event) => {
    event.preventDefault()

	reloadImage()

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
        document.getElementById("X").innerHTML = X
        document.getElementById("Y").innerHTML = Y
        document.getElementById("xOffset").innerHTML = xOffset
        document.getElementById("yOffset").innerHTML = yOffset
    })
    .error( err => 
        alert(err)
    )
}