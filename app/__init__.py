from flask import Flask


def create_app(object_name, env="prod"):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config.from_object(object_name)
    app.config['ENV'] = env

    # register our blueprints
    from routes.main import main
    app.register_blueprint(main)  # regist URL

    from routes.user import user
    app.register_blueprint(user)

    return app
