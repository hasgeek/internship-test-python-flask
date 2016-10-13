from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Global variable which stores the overall score in main memory
# of application.
globalScore = 0

# Landing page which renders the homepage and the score. 
@app.route("/", methods=["GET"])
def homepage():
    global globalScore
    # Render the template with the globalScore data
    return render_template("index.html", score=globalScore)


# Define a new @app.route for '/count' with the method POST
# that checks the 'count' value of the submitted form data.
# if the value is 'increment', increase globalScore by 1
# else if the value is 'decrement' decrease globalScore by 1
# and finally issue a redirect back to '/' so the new score is shown.
# We throw proper HTTP 4xx error code if unable to process the request.
@app.route('/count', methods=["GET","POST"])
def modify_counter():
    global globalScore
    if request.method == 'POST':
        try:
            if request.form['count'] == "increment":
                globalScore += 1
            elif request.form['count'] == "decrement":
                globalScore -= 1
            else:
                # Invalid value present in form field 'count'
                abort(422)    
        except Exception, e:
            abort(400)
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.run()
