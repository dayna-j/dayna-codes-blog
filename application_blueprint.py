from flask import Blueprint, render_template
# from boto import 

application_blueprint = Blueprint("application_blueprint",__name__)

@application_blueprint.route('/')
def index():
    return render_template('index.html')

@application_blueprint.route('/resume/')
def resume():
    return render_template('resume.html')

@application_blueprint.route('/var/<var>/')
def var(var):
    return render_template('var.html',var={
        "name": "Dayna",
        "addr": "1805 S. Longmore"
    }, aList=[1,2,3,4,5])


# @application_blueprint.route('/resume/<var>')
# def resume(var):
#     return f'<h2>{var}</h2>'