function playVideo() {
    var video = document.getElementById("myVideo");
    video.style.display = "block";
    video.play();
}

function openLightbox(img) {
    document.getElementById("lightbox").style.display = "block";
    document.getElementById("lightbox-img").src = img.src;
}

function closeLightbox() {
    document.getElementById("lightbox").style.display = "none";
}

function showPopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "block";

    setTimeout(function() {
        popup.style.display = "none";
    }, 3000);
}

function openCert(img) {
    document.getElementById("certLightbox").style.display = "block";
    document.getElementById("certImg").src = img.src;
}

function closeCert() {
    document.getElementById("certLightbox").style.display = "none";
}

