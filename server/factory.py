from . import routes
from .extensions import app, cors, sched
from .settings import config


def create_app(config):
    """
        Create application instance.
    """
    app.config.from_object(config)
    app.static_folder = config.STATIC_DIR

    cors.init_app(app)
    sched.start()
    
    return app
