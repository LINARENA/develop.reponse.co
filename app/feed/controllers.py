from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
# from app.feed.forms import SearchForm


mod_feed = Blueprint('feed', __name__, url_prefix='/feed')
@mod_feed.route("/<top_section>/<bottom_section>")
def feed(top_section, bottom_section):
    return render_template('feed/feed.html')
