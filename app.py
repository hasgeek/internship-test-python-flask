from flask import Flask, render_template, redirect, request

#imported additional 'redirect' and 'request' for redirecting back to homepage and parsing POST form respectively
app = Flask(__name__)
globalScore = 0 #initial value
theme = "light-green accent-4" #initial class 

@app.route("/")
def hello():
  global globalScore
    #Render the template with the globalScore data
  return render_template("index.html",count=globalScore,my_style = theme) #Rendered the template with globalScore data and applied class according to value of globalData


# Define a new @app.route for '/count' with the method POST
# that checks the 'count' value of the submitted form data.
# if the value is 'increment', increase globalScore by 1
# else if the value is 'decrement' decrease globalScore by 1
# and finally issue a redirect back to '/' so the new score is shown

@app.route('/count', methods=['POST'])
def form():
	global globalScore
	global theme
	my_boolean = request.form['count'] # my_boolean with value of 'count'
	if my_boolean == 'increment':
		globalScore+=1			#increment globalScore 
	else:
		globalScore-=1      #decrement globalScore

#checking conditions for class	
	if globalScore>0:
		theme = "light-green accent-4" #class for count > 0
	else:
		theme = "orange accent-4" #class for count <= 0
	#finally redirect to homepage		
	return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
