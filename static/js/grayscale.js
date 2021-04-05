const grayscale = (event) => {
    event.preventDefault()

    const queryString = window.location.search
    fetch(`/api/grayscale${queryString}`)
    .then(response => {
        reloadImage()
    })
    .error( err => 
        alert(err)
    )
}
