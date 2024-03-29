const showResize = (event) => {
    event.preventDefault()
    const form = document.getElementById("resize-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == form) {
            form.style.display = "none";
        }
    } 
    const span = document.getElementById("resize-close")
    span.onclick = function() {
      form.style.display = "none";
    }


}

const resize = (event) => {
    event.preventDefault()

    const width = document.getElementById("resize-width").value
    const height = document.getElementById("resize-height").value

    const body = JSON.stringify({width, height})

    const queryString = window.location.search
    fetch(`/api/resize${queryString}`, {
            method: "POST",
            body,
            headers:{'content-type': 'application/json'}
        }
    )
    .then(response => {
        reloadImage()
        document.getElementById("width").innerHTML = width
        document.getElementById("height").innerHTML = height
    })
    .catch( err => 
        alert(err)
    )
}
