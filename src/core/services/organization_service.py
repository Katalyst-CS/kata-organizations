from src.core.exceptions.OrganizationNotFoundException import OrganizationNotFoundException
from src.infrastructure.db.repositories.organization_repository import OrganizationRepository


# En esta clase utilizaremos los metodos del repository

class OrganizationService:

    def __init__(self):
        self.repository = OrganizationRepository()

    def create_organization(self, data):
        return self.repository.create(data)

    def list_organizations(self):
        return self.repository.get_all()

    def get_organization(self, org_id):

        org = self.repository.get_by_id(org_id)
        if not org:
            raise OrganizationNotFoundException(f"Organización con ID {org_id} no encontrada.")
        return org

    def update_organization(self, org_id, data):
        updated_org = self.repository.update(org_id, data)
        if not updated_org:
            raise OrganizationNotFoundException(f"No se pudo actualizar la organización con ID {org_id}.")
        return updated_org

    def delete_organization(self, org_id):

        if not self.repository.delete(org_id):
            raise OrganizationNotFoundException(f"No se pudo eliminar la organización con ID {org_id}.")
