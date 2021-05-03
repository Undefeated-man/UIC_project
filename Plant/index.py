"""
	###########################################################################
	#		                                                                  #
	#		Project: Observing Plants                                         #
	#		                                                                  #
	#		Filename: index.py                                                #
	#		                                                                  #
	#		Programmer: Vincent Holmes (Vincent_HolmesZ@outlook.com)          #
	#		                                                                  #
	#		Description: if you like this, feel free to click and give me a   #
	#                      star~~                                             #
	#		                                                                  #
	#		Start_date: 2021-04-13                                            #
	#		                                                                  #
	#		Last_update: 2021-04-13                                           #
	#		                                                                  #
	###########################################################################
"""


from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)

app = Flask(__name__)

# the home page
@app.route('/plant', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/features', methods=['GET'])
def features():
    return render_template("features.html")
    
@app.route('/introduction', methods=['GET'])
def introduction():
    return render_template("introduction.html")
    
@app.route('/location', methods=['GET'])
def location():
    return render_template("location.html")

@app.route('/reward', methods=['GET'])
def reward():
    return render_template("reward.html")

if __name__ == "__main__":
    app.run()
