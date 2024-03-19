from flask import Flask, render_template, request
from handlers.merge_requests import get_merge_requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/merge_requests')
def merge_requests():
    state = request.args.get("state")
    return render_template("merge_requests.j2", merge_requests=get_merge_requests(state))


app.run(host='0.0.0.0')
