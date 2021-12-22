from flask import Flask
from flask_cors import CORS
import markets


# function to return an initialized flask app
def create_app():
    app = Flask(__name__)

    # flask apps have a secret key that ecrypts session data
    app.config["SECRET_KEY"] = "happy scanning"
    # import and register your blueprints/routes

    # we don't want any prefixed so just put /
    app.register_blueprint(markets.routes, url_prefix="/")
    return app


# get initialized flask app and run it
app = create_app()
app.run(debug=False)

# from waitress import serve

# serve(app, host="0.0.0.0", port=8080)

# below there is a security line not sure if we need it
# if __name__ == "__main__":
#     # running in dev mode will re-run the server everytime you hit save
#     app.run(debug=True)
