const showEdge = (event) => {
    event.preventDefault()
    const form = document.getElementById("edge_detection-form")

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
    const span = document.getElementById("edge-detection-close")
    span.onclick = function() {
      form.style.display = "none";
    }


}

const edge_detection = (event) => {
    event.preventDefault()
    const queryString = window.location.search

    var flipSelect = document.getElementById("edge_detection-select");
    var val = flipSelect.value;

    fetch(`/api/edge-detection${queryString}`, {
        method: "POST",
        body: JSON.stringify({val}),
        headers: {
            'Content-Type': 'application/json'
        },    
    })
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}