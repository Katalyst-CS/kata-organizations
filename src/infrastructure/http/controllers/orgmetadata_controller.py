from flask import Blueprint




#Creacion del Blueprint para las rutas de Organization.
organization_bp = Blueprint('organization_bp', __name__)
service = OrganizationService()

