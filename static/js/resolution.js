const getResolution = () => {
    const queryString = window.location.search

    fetch(`/api/resolution${queryString}`)
    .then(response => response.json())
    .then(data => {
        const width = document.getElementById("width")
        width.innerHTML = data.width
        
        const height = document.getElementById("height")
        height.innerHTML = data.height
    })
    .catch( err => 
        alert(err)
    )

}

window.onload = (event) => {
    event.preventDefault()
    
    // prevents browser getting the image from the cache
    reloadImage()
    getResolution()   
}