const showContrast = (event) => {
    event.preventDefault()
    const form = document.getElementById("contrast-form")

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

    const span = document.getElementById("contrast-close")
    span.onclick = function() {
      form.style.display = "none";
    }


}



const contrast_feature = (event) => {
    event.preventDefault()
    const queryString = window.location.search

    var contrastSelect = document.getElementById("contrast-select");
    var contrastVal = contrastSelect.value;

    fetch(`/api/contrast${queryString}`, {
        method: "POST",
        body: JSON.stringify({contrastVal}),
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