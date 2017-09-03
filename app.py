from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/count", methods=['POST'])
def countOperation():
    global globalScore

    #Increment/Decrement count value
    if( request.form['count'] == 'increment' ):
        globalScore+=1
    else:
        globalScore-=1

    #Redirect to '/'
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run()
