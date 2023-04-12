
function setCardBackgrounds() {
    var cards = document.querySelectorAll('.card');
    for (var i = 0; i < cards.length; i++) {
        cards[i].style.backgroundImage = "url('static/images/cards/" + cards[i].id + ".png')";
        cards[i].style.backgroundSize = "cover";
    }
}

const betAmount = document.querySelector('#bet-amount');
const betUp = document.querySelector('#bet-up');
const betDown = document.querySelector('#bet-down');
const playerChips = document.querySelector('#chips');

betUp.addEventListener('click', function () {
    betAmount.value = parseInt(betAmount.value) + 10;
    if (parseInt(betAmount.value) > 0) {
        betDown.disabled = false;
    }
    if (parseInt(betAmount.value) >= parseInt(playerChips.textContent)) {
        betAmount.value = playerChips.textContent;
        betUp.disabled = true;
    }
});

betDown.addEventListener('click', function () {
    betAmount.value = parseInt(betAmount.value) - 10;
    if (parseInt(betAmount.value) < parseInt(playerChips.textContent)) {
        betUp.disabled = false;
    }
    if (parseInt(betAmount.value) <= 0) {
        betAmount.value = 0;
        betDown.disabled = true;
    }
});

window.addEventListener("load", setCardBackgrounds);