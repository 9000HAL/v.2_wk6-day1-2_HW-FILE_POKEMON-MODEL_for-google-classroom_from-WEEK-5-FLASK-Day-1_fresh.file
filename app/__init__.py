from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment



login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()


def create_app():

    app = Flask(__name__)   
    app.config.from_object(Config)


    #register packages
    login_manager.init_app(app)
    db.init_app(app)              #replaced by SQLAlchemy(app) above [huh???]
    migrate.init_app(app, db)     
    moment.init_app(app)

    #login_manager settings
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You must be logged in to view this page!'
    login_manager.login_message_category = 'warning'


    #import blueprints
    from app.blueprints.main import main
    from app.blueprints.auth import auth
    from app.blueprints.posts import posts

    #register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(posts)
    
    return app



from app import routes, models      #----dk fix 37:55 rec'g


