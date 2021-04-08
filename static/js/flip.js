const flip = (event) => {
    event.preventDefault()
    const queryString = window.location.search

    fetch(`/api/flip${queryString}`)
    .then(response => {
        reloadImage()
    })
    .error( err => 
        alert(err)
    )
}