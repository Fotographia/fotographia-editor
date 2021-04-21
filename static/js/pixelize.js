const showPixelize = (event) => {
    event.preventDefault()
    const form = document.getElementById("pixel-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}


const pixelize = (event) => {
    event.preventDefault()

    const pixels = document.getElementById("pixels").value
    const body = JSON.stringify({pixels})

    const queryString = window.location.search
    fetch(`/api/pixelize${queryString}`,{
        method: "POST",
        body,
        headers:{'content-type': 'application/json'}
    })
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}