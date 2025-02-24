import uuid

from flask import Blueprint, jsonify, request

from core.exceptions.MetadataNotFoundException import MetadataNotFoundException
from core.services.orgmetadata_service import OrgMetadataService

# Aqui se inclyen todos los endpoints

# Creamos un objeto blueprint para manejar las rutas.

metadata_bp = Blueprint('metadata_bp', __name__)

# Inicializamos el servicio
service = OrgMetadataService()


# ENDPOINTS

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
        return jsonify({'message': f'Metadato creado', 'ID': str(meta.id)}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f"Error interno del servidor: {str(e)}"}), 500


# Lista de todos los metadatos
@metadata_bp.route('/metadata', methods=['GET'])
def get_all_metadatas():
    try:
        meta_list = service.list_metadata()
        if not meta_list:
            return jsonify({'error': 'No se encontraron metadatos.'}), 404

        result = [{'id': str(meta.id), 'key': meta.key, 'value': meta.value} for meta in meta_list]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': f"Error interno del servidor: {str(e)}"}), 500


# Obtener un metadato por ID.

@metadata_bp.route('/metadata/<meta_id>', methods=['GET'])
def get_metadata_by_id(meta_id):
    # Validacion del formato del UUID
    try:
        uuid.UUID(meta_id)
    except ValueError:
        return jsonify({'error': 'ID invalido. Debe ser un UUID.'}), 400

    try:
        meta = service.get_metadata_by_id(meta_id)

        if not meta:
            return jsonify({"error": "Metadato no encontrado."}), 404

        return jsonify({'id': str(meta.id), 'key': meta.key, 'value': meta.value}), 200
    except Exception as e:
        return jsonify({'error': f"Error interno del servidor: {str(e)}"}), 500


# Actualizar un metadato existente.

@metadata_bp.route('/metadata/<meta_id>', methods=['PUT'])
def update_metadata(meta_id):
    # Validacion del uuid
    try:
        uuid.UUID(meta_id)
    except ValueError:
        return jsonify({"error": "ID inválido. Debe ser un UUID."}), 400

    data = request.get_json()

    # Verificacion basica.
    if not data:
        return jsonify({"error": "Faltan datos."}), 400

    # Verificamos campos obligatorios
    required_fields = ['key', 'value']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan campos requeridos: key y value."}), 400

    try:
        updated_metadata = service.update_metadata(meta_id, data)
        if updated_metadata:
            return jsonify({'message': f'Metadato actualizado.', 'id': str(updated_metadata.id)}), 200
        else:
            return jsonify({'error': f"No se pudo actualizar el metadato con id {meta_id}."}), 400
    except MetadataNotFoundException as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': f"Error interno del servidor: {str(e)}"}), 500


# Eliminar un metadato por su ID
@metadata_bp.route('/metadata/<meta_id>', methods=['DELETE'])
def delete_metadata(meta_id):
    # Validacion del uuid
    try:
        uuid.UUID(meta_id)
    except ValueError:
        return jsonify({"error": "ID inválido. Debe ser un UUID."}), 400

    try:
        deleted = service.delete_metadata(meta_id)
        if deleted:
            return jsonify({'message': 'Metadato eliminado.'}), 200
        else:
            return jsonify({'error': f"Metadato con id {meta_id} no encontrado."}), 404

    except MetadataNotFoundException as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': f"Error interno del servidor: {str(e)}"}), 500
