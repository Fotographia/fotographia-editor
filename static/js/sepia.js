const sepia = (event) => {
    event.preventDefault()

    const queryString = window.location.search
    fetch(`/api/sepia${queryString}`)
    .then(response => {
        reloadImage()
    })
    .error( err => 
        alert(err)
    )
}
