const session_id = Math.random().toString(36).substr(2, 9) 
localStorage.setItem('session_id', session_id)

var imageUploadInput = document.getElementById('imageUploadInput')

imageUploadInput.addEventListener('change', function(event) {
    event.preventDefault()

    const file = event.target.files[0]
    
    const data = new FormData()
    data.append('file', file)
    fetch(`/api/uploadImage?session_id=${session_id}`, {
      method: 'POST',
      body: data
    }).then(response => {
      if (!response.ok) {
        const imageUploadError = document.getElementById('imageUploadError')
        imageUploadError.innerHTML = 'Unsupported image. Please try jpeg, jpg or png.'
      } else {
        window.location.href = `/editor?session_id=${session_id}&filename=${file.name}`
      }
    })
})
