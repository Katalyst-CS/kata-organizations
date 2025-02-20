from flask import Blueprint, jsonify, request

from src.core.services.orgmetadata_service import OrgMetadataService

# Aqui se inclyen todos los endpoints

# Creamos un objeto blueprint para manejar las rutas.

metadata_bp = Blueprint('metadata_bp', __name__)

# Inicializamos el servicio
service = OrgMetadataService()


# Creamos los endpoints

# Crear metadato
@metadata_bp.route('/metadata', methods=['POST'])
def create_metadata():
    # recogemos los datos enviados por el cliente
    data = request.get_json()

    # Verificacion basica.
    if not data:
        return jsonify({"error": "Faltan datos."}), 400

    # Verificamos campos obligatorios
    required_fields = ['key', 'value']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan campos requeridos: key y value."}), 400

    try:
        meta = service.create_metadata(data)
        return jsonify({'message': f'Metadato creado', 'id': str(meta.id)}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


# Lista de todos los metadatos
@metadata_bp.route('/metadata', methods=['GET'])
def get_all_metadatas():
    meta_list = service.list_metadata()
    if not meta_list:
        return jsonify({'error': 'No se encontraron metadatos.'}), 404

    result = [{'id': str(meta.id), 'key': meta.key, 'value': meta.value} for meta in meta_list]
    return jsonify(result), 200

# TODO CONTINUAR CON
#  GET /metadata/<id> → Obtener un metadato por ID.
#  PUT /metadata/<id> → Actualizar un metadato existente.
#  DELETE /metadata/<id> → Eliminar un metadato por su ID
