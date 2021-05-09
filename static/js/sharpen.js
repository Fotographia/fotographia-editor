const show_sharpen = (event) => {
    event.preventDefault()
    const form = document.getElementById("sharpen-form")

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
    const span = document.getElementById("sharpen-close")
    span.onclick = function() {
      form.style.display = "none";
    }


}


const sharpen = (event) => {
    event.preventDefault()
    const queryString = window.location.search
    
    var sharpen_val = document.getElementById("sharpen_value").value
    const body = JSON.stringify({sharpen_val})
    
    fetch(`/api/sharpen${queryString}`, {
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