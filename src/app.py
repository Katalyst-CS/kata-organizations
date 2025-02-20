from flask import Flask

from src.infrastructure.http.controllers.organization_controller import organization_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(organization_bp)


    @app.route('/')
    def index():
        return "API Kata organizations corriendo."

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)