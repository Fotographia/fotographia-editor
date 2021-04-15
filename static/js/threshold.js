const showThreshold = (event) => {
    event.preventDefault()
    const form = document.getElementById("threshold-form")

    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}


const threshold = (event) => {
    event.preventDefault()

    const queryString = window.location.search

    var thresholdSelect= document.getElementById("threshold_select")
    var thres_value = thresholdSelect.value

    fetch(`/api/threshold${queryString}`, {
        method: "POST",
        body: JSON.stringify({thres_value}),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        reloadImage()
    })
    .error( err =>
        alert(err)
    )
}