const showFlip = (event) => {
    event.preventDefault()
    const form = document.getElementById("flip-form")

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
    const span = document.getElementById("flip-close")
    span.onclick = function() {
      form.style.display = "none";
    }


}



const flip = (event) => {
    event.preventDefault()
    const queryString = window.location.search

    var flipSelect = document.getElementById("flip-select");
    var val = flipSelect.value;

    fetch(`/api/flip${queryString}`, {
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