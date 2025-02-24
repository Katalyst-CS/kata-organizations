from operator import truediv

from peewee import DoesNotExist

from infrastructure.db.models.organization_model import Organization


#En el repositorio incluimos las operaciones CRUD


class OrganizationRepository:

    #Crear una organizacion
    def create(self, data):
        return Organization.create(**data)

    # Lista todas las organizaciones

    def get_all(self):
        return list(Organization.select())

    # Buscar organizacion por id
    def get_by_id(self, org_id):
        try:
            Organization.select().where(Organization.id == org_id)
        except DoesNotExist:
            return None

    # Actualizar organizacion
    def update(self, org_id, data):

        # Buscamos la organizacion
        org = self.get_by_id(org_id)

        if not org:
            return None

        query = Organization.update(**data).where(Organization.id == org_id)
        query.execute()
        return self.get_by_id(org_id)

    # Borrar una organizacion.

    def delete(self, org_id):
       org = Organization.get_by_id(org_id)
       if org:
           org.delete_isntace()
           return True
       return False