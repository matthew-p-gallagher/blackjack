from flask import Flask, render_template, request, redirect, url_for, flash

from game_logic import Game


app = Flask(__name__)

game = Game()


@app.route("/")
@app.route("/play_round", methods=["GET", "POST"])
def main():

    global game

    if request.method == "POST":
        bet = request.form["bet"]
        game.play_round(int(bet))
        return render_template("game.html", game=game)

    return render_template("game.html", game=game)


if __name__ == "__main__":
    app.run(debug=True)
