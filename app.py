from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from game_logic import Game
from game_logic import Card


app = Flask(__name__)
app.config.update(TESTING=True, SECRET_KEY="f738dj3f487fhf830w0dpjfjg039e3902394uf")

game = Game()


@app.route("/")
@app.route("/blackjack")
def main():
    global game
    game.game_reset()
    return render_template("game.html", game=game)


@app.route("/start_round", methods=["POST"])
def start_round():
    global game

    if request.method == "POST":
        bet = request.form["bet"]
        game.start_round(int(bet))  # TODO: handle when not enough chips
        game_data = game.get_json()

    return jsonify(game_data)


@app.route("/reset", methods=["POST"])
def reset():
    global game

    if request.method == "POST":
        game.game_reset()

    return redirect(url_for("main"))


@app.route("/hit", methods=["POST"])
def hit():
    global game

    if request.method == "POST":
        game.hit()
        game_data = game.get_json()
        return jsonify(game_data)


@app.route("/stand", methods=["POST"])
def stand():
    global game

    if request.method == "POST":
        game.stand()
        game_data = game.get_json()
        return jsonify(game_data)


if __name__ == "__main__":
    app.run(debug=True)
