// prevent browser getting the image from the cache
const reloadImage = () => {
    let src = document.getElementById("img").src
    document.getElementById("img").src = src + "?" + new Date().getTime()
    const export_button = document.getElementById("export_button") 
    export_button.href = export_button.href + "?" +  new Date().getTime()
}