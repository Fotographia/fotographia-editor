const negate = (event) => {
    event.preventDefault()

    const queryString = window.location.search
    fetch(`/api/negate${queryString}`)
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}
