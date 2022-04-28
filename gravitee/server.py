from flask import Flask, render_template, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from os import rename
import subprocess
import os 

app = Flask(__name__)

#swagger configs
SWAGGER_URL = '/swagger'
API_URL = '/static/openapispec/pathout.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config = {
            'app_name': "test"
        }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/submit/job')
def submit_job():
    submit = subprocess.run(['sh', './submit.sh'])
    return redirect('/swagger')


if __name__ == '__main__': 
    app.run(debug=True)

