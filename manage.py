from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate

from users.routes import users
from extensions import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

app.register_blueprint(users, url_prefix="/users")

# with app.app_context():
#     db.create_all()

migrate = Migrate(app, db)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)


# flask db init
# flask db migrate -m "message"
# flask db upgrade

# user = User.query.filter_by(email=email_to_search).first()
# user = User.query.filter(User.email == email_to_search).first()
# users = User.query.filter_by(email=email_to_search).all()