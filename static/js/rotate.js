const rotate = (event) => {
    event.preventDefault()
    const queryString = window.location.search

    fetch(`/api/rotate${queryString}`)
    .then(response => {
        reloadImage()
        getResolution()
    })
    .catch( err => 
        alert(err)
    )
}