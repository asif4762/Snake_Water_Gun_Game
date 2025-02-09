from flask import Flask, render_template, request
import random

app = Flask(__name__)

youDist = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDist = {1: "Snake", -1: "Water", 0: "Gun"}

def play_game(user_choice):
    computer_choice = random.choice(["Snake", "Water", "Gun"])
    you = youDist[user_choice]
    computer = youDist[computer_choice]

    if you == computer:
        result = "It's a Draw!"
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        result = "You Win!"
    else:
        result = "You Lose!"

    return user_choice, computer_choice, result

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_choice = request.form["choice"]
        user_choice, computer_choice, result = play_game(user_choice)
        return render_template("index.html", user_choice=user_choice, computer_choice=computer_choice, result=result)
    return render_template("index.html", user_choice=None, computer_choice=None, result=None)

if __name__ == "__main__":
    app.run(debug=True)
