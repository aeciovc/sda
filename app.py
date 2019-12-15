from flask import Flask, request

from events.controller import EventController

app = Flask(__name__)
app.debug = True

@app.route("/event", methods=["POST"])
def event_create():
    
    event = {
        "name":request.form['name'],
        "description":request.form['description'],
        "place":request.form['place'],
        "day":request.form['day'],
        "picture":request.form['picture'],
    }

    event_controller = EventController()
    
    result = event_controller.create(event)

    return {}, 201