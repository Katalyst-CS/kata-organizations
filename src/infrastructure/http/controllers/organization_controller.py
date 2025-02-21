from flask import Blueprint, request, jsonify

from src.core.exceptions.OrganizationNotFoundException import OrganizationNotFoundException
from src.core.services.organization_service import OrganizationService

# Creacion deun Blueprint para las rutas
organization_bp = Blueprint('organization_bp', __name__)
# Instanciamos el servicio de organizacion para acceder a sus metodos.
service = OrganizationService


# Ruta para crear una organizacion
@organization_bp.route('/organizations', methods=['POST'])
def create_organization():
    data = request.get_json()
    try:
        org = service.create_organization(data)
        return jsonify({'message': 'Organizacion creada', 'id': str(org.id)}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


# Ruta para obtener la lista de todas las organizaciones.
@organization_bp.route('/organizations', methods=['GET'])
def list_organizations():
    orgs = service.list_organizations()
    result = [{'id': str(org.id), 'name': org.name} for org in orgs]
    return jsonify(result), 200


# Ruta para obtener una organizacion por Id.
@organization_bp.route('/organizations/<org_id>', methods=['GET'])
def get_organization(org_id):
    org = service.get_organization(org_id)
    return jsonify({'id': org.id, 'name': org.name}), 200


# Ruta para actualizar una organizacion

@organization_bp.route('/organizations/<org_id>', methods=['PUT'])
def update_organization(org_id):
    data = request.get_json()
    try:
        updated_org = service.update_organization(org_id, data)
        return jsonify({'message': 'Organización actualizada', 'id': str(updated_org.id)}), 200
    except OrganizationNotFoundException as e:
        return jsonify({'error': str(e)}), 404


# Ruta para borrar una organizacion

@organization_bp.route('/organizations/<uuid:org_id>', methods=['DELETE'])
def delete_organization(org_id):
    try:
        service.delete_organization(org_id)
        return jsonify({'message': 'Organización eliminada'}), 200
    except OrganizationNotFoundException as e:
        return jsonify({'error': str(e)}), 404
