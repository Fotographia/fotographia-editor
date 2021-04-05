const blurImage = (event) => {
    event.preventDefault()
    const queryString = window.location.search

    fetch(`/api/blur${queryString}`)
    .then(response => {
        reloadImage()
    })
    .error( err => 
        alert(err)
    )
}