// prevent browser getting the image from the cache
const reloadImage = () => {
    let src = document.getElementById("img").src
    document.getElementById("img").src = src + "?" + new Date().getTime()
}