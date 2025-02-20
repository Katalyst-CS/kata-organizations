from peewee import DoesNotExist

from src.infrastructure.db.models.org_metadata_model import OrgMetadata


class OrgMetadataRepository:

    # Crear un metadato
    def create(self, data):
        meta = OrgMetadata(**data)
        meta.save()
        return meta

    # Listar metadatos
    def get_all(self):
        return list(OrgMetadata.select())

    # Buscar metadato por id
    def get_by_id(self, meta_id):

        try:
            return OrgMetadata.get(OrgMetadata.id == meta_id)
        except DoesNotExist:
            return None

    # Actualizar metadato
    def update(self, meta_id, data):
        meta = self.get_by_id(meta_id)
        if not meta:
            return None
        #Actualizacion de campos
        query = OrgMetadata.update(**data).where(OrgMetadata.id == meta_id)
        query.execute()
        return self.get_by_id(meta_id)

    # Borrar metadato
    def delete(self, meta_id):
        meta = self.get_by_id(meta_id)
        if meta:
            meta.delete_instance()
            return True
        return False
