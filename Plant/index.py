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
import translater_dictionary as td

app = Flask(__name__)

# the home page
@app.route('/plant', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
