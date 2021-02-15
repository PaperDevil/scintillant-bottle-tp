"""
    app - Application initiation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    In this file, you need to register routes, connect third-party
    components and set basic application settings.
"""
import bottle


def create_app():
    """Application factory"""
    app = application = bottle.default_app()

    # Register basic routes
    from app.routes import routes, errors, options

    return app
