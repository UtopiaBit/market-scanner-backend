from flask import Flask
from flask_cors import CORS
import markets
from waitress import serve
import os


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
# app.run(debug=False)


if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    port = int(os.environ.get("PORT", 5000))
    # We now use this syntax to server our app.
    serve(app, host="0.0.0.0", port=port)

