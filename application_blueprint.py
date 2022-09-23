from flask import Blueprint, render_template

application_blueprint = Blueprint("application_blueprint",__name__)

@application_blueprint.route('/')
def index():
    return render_template('index.html')

@application_blueprint.route('/resume')
def resume():
    return render_template('resume.html')