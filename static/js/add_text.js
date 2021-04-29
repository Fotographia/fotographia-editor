const show_add_text = (event) => {
    event.preventDefault()
    const form = document.getElementById("add-text-form")
    
    if (form.style.display === "none") {
        form.style.display = "block"
    } else {
        form.style.display = "none"
    }
}

const add_text = (event) => {
    event.preventDefault()

    const instext = document.getElementById("ins_text").value
    const xpos = document.getElementById("x_pos").value
    const ypos = document.getElementById("y_pos").value
    const selfamily = document.getElementById("sel_family").value
    const selstyle = document.getElementById("sel_style").value
    const pickcolor = document.getElementById("pick_color").value
    const selsize = document.getElementById("sel_size").value
    const selalign = document.getElementById("sel_align").value

    const body = JSON.stringify({instext,xpos,ypos,selfamily,selstyle,pickcolor,selsize,selalign})
    const queryString = window.location.search

    fetch(`/api/add-text${queryString}`, {
            method: "POST",
            body,
            headers:{'content-type': 'application/json'},
        }
     )
    .then(response => {
        reloadImage()
    })
    .catch( err => 
        alert(err)
    )
}