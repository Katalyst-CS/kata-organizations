from flask import Flask, jsonify

from infrastructure.db.init_db import initialize_db
from infrastructure.http.controllers.organization_controller import organization_bp


def create_app():
    app = Flask(__name__)

    initialize_db()

    app.register_blueprint(organization_bp)
    print("Blueprint de organizations registrado correctamente")
   # app.register_blueprint(metadata_bp)

    @app.route('/')
    def index():
        return "API Kata organizations corriendo."

    @app.route('/test', methods=['GET'])
    def test_connection():
        return jsonify({'message': 'Conexión exitosa'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)