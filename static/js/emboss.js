const show_emboss = (event) => {
    event.preventDefault()
    const form = document.getElementById("emboss-form")

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
    const span = document.getElementById("emboss-close")
    span.onclick = function() {
      form.style.display = "none";
    }


}

const emboss = (event) => {
    event.preventDefault()
    
    const embDepth = document.getElementById("emboss_depth").value
    const embScale = document.getElementById("emboss_scale").value
    const embOffset = document.getElementById("emboss_offset").value
    
    const body = JSON.stringify({embDepth,embScale,embOffset})

    const queryString = window.location.search

    fetch(`/api/emboss${queryString}`,{
            method: "POST",
            body,
            headers:{'content-type': 'application/json'},
        }
    )
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}
