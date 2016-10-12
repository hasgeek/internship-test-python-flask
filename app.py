from flask import Flask, render_template, redirect, request

app = Flask(__name__)
globalScore = 0


@app.route("/")
def hello():
    global globalScore
    # Render the template with the globalScore data
    return render_template("index.html", score=globalScore)


# Define a new @app.route for '/count' with the method POST
# that checks the 'count' value of the submitted form data.
# if the value is 'increment', increase globalScore by 1
# else if the value is 'decrement' decrease globalScore by 1
# and finally issue a redirect back to '/' so the new score is shown
@app.route('/count', methods=['POST'])
def count():
    global globalScore
    action = request.form.get("count", "")
    if action == 'decrement':
        globalScore -= 1
    elif action == 'increment':
        globalScore += 1
    return redirect('/')


if __name__ == "__main__":
    app.run()
