// Get resolution
const queryString = window.location.search

fetch(`/api/resolution${queryString}`)
.then(response => response.json())
.then(data => {
    const width = document.getElementById("width")
    width.innerHTML = data.width
    
    const height = document.getElementById("height")
    height.innerHTML = data.height
})
.error( err => 
    console.log(err)
)