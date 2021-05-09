// Modal box
let modal = document.getElementById("start-modal");

// Get the button that opens the modal
let btn = document.getElementById("start-btn");

// Get the <span> element that closes the modal
let span = document.getElementById("close");

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 

// Upload image
const session_id = Math.random().toString(36).substr(2, 9) 
localStorage.setItem('session_id', session_id)

const imageUploadInput = document.getElementById('start-upload')

imageUploadInput.addEventListener('change', (event) => {
    event.preventDefault()

    const file = event.target.files[0]
    
    const data = new FormData()
    data.append('file', file)
    fetch(`/api/upload?session_id=${session_id}`, {
      method: 'POST',
      body: data
    }).then(response => {
      if (!response.ok) {
        const imageUploadError = document.getElementById('start-upload-error')
        imageUploadError.innerHTML = 'Unsupported image. Please try jpeg, jpg or png.'
      } else {
        window.location.href = `/editor?session_id=${session_id}&filename=${file.name}`
      }
    })
})
