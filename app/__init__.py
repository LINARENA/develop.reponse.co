from flask import Flask, render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.user.controllers import mod_user as user_module
app.register_blueprint(user_module)

from app.feed.controllers import mod_feed as feed_module
app.register_blueprint(feed_module)

from app.service.controllers import mod_service as service_module
app.register_blueprint(service_module)

db.create_all()
for rule in app.url_map.iter_rules():
    print(rule)
