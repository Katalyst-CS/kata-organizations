from src.infrastructure.db.models.organization_model import Organization


#En el repositorio incluimos las operaciones CRUD


class OrganizationRepository:

    #Crear una organizacion
    def create(self, data):
        return Organization.create(**data)

    #