from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
# from app.feed.forms import SearchForm


mod_service = Blueprint('service', __name__, url_prefix='/service')

@mod_service.route("/about/")
def about():
    return render_template('service/about.html')

@mod_service.route("/help/")
def help():
    return render_template('service/help.html')

@mod_service.route("/faq/")
def faq():
    return render_template('service/faq.html')

@mod_service.route("/terms/")
def terms():
    return render_template('service/terms.html')

@mod_service.route("/policy/")
def policy():
    return render_template('service/policy.html')
