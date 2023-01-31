function setCardBackgrounds() {
    var cards = document.querySelectorAll('.card');
    for (var i = 0; i < cards.length; i++) {
        cards[i].style.backgroundImage = "url('static/images/cards/" + cards[i].id + ".png')";
        cards[i].style.backgroundSize = "cover";
    }
}

window.addEventListener("load", setCardBackgrounds);