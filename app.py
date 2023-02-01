from flask import Flask, render_template, request, redirect, url_for, flash

from game_logic import Game


app = Flask(__name__)
app.config.update(TESTING=True, SECRET_KEY="f738dj3f487fhf830w0dpjfjg039e3902394uf")

game = Game()


@app.route("/")
def main():
    global game
    return render_template("game.html", game=game)


@app.route("/start_round", methods=["POST"])
def start_round():
    global game

    if request.method == "POST":
        bet = request.form["bet"]
        game.start_round(int(bet))
        for message in game.messages:
            flash(message)

    return redirect(url_for("main"))


@app.route("/hit_or_stand", methods=["POST"])
def hit_or_stand():
    global game

    if request.method == "POST":
        if "hit" in request.form:
            game.hit()
        elif "stand" in request.form:
            game.stand()
            print(game.player.hand.cards)
        for message in game.messages:
            flash(message)

    return redirect(url_for("main"))


@app.route("/reset", methods=["POST"])
def reset():
    global game

    if request.method == "POST":
        game.game_reset()

    return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(debug=True)
