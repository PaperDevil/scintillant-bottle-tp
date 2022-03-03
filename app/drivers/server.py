import bottle


class BottleServer:
    @staticmethod
    def create_app():
        """Application factory"""
        app = application = bottle.default_app()

        # Register basic routes
        from app.routes import routes, errors, options
        from app.routes import scintillant  # Register Scintillant settings

        return app