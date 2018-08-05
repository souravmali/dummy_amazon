from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
	name_str = request.args.get('name')
	age_str = request.args['age']
	#return "congrats your fist api"+name_str+"and your age is"+age_str
	return render_template('welcom.html',name=name_str,age=age_str)
@app.route("/swap")
def sourav():
	return "takali takali"

@app.route("/buy",methods=['post'])
def handle_get_and_post():
	import Pdb;pdb.set_trace()
	post_value =request.form["post_parameter1"]
	return"we have succeful handel post request"+post_value

if(__name__=="__main__"):
	app.run()
