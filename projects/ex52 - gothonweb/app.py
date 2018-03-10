from flask import Flask, render_template, session, redirect, url_for, request, render_template
import planisphere


app = Flask(__name__)

@app.route('/')
def index():
	""" this is used to setup the session """
	session['room_name'] = planisphere.START
	return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
	room_name = session.get('room_name')

	if request.method == "GET":
		if room_name and room_name != "generic_death":
			room = planisphere.load_room(room_name)
			return render_template("show_room.html", room=room)
		else:
			""" if not GET is passed, player died or a bug occured """
			return render_template("you_died.html")
	else:
		action = request.form.get('action')

		if room_name and action:
			room = planisphere.load_room(room_name)
			next_room = room.go(action)

			if not next_room:
				session['room_name'] = planisphere.name_room(next_room)
			else:
				session['room_name'] = planisphere.name_room(next_room)
		return redirect(url_for("game"))

app.secret_key = 'swag'

if __name__ == "__main__":
	app.run()