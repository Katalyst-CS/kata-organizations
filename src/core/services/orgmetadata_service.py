from src.core.exceptions.MetadataNotFoundException import MetadataNotFoundException
from src.infrastructure.db.repositories.orgmetadata_repository import OrgMetadataRepository


class OrgMetadataService():
    def __init__(self):
        self.repository = OrgMetadataRepository()

    # Crear metadato
    def create_metadata(self, data):
        return self.repository.create(data)

    # Lista de todos los metadatos
    def list_metadata(self):
        return list(self.repository.get_all())

    # Obtener metadato por Id.
    def get_metadata_by_id(self, meta_id):
        metadata = self.repository.get_by_id(meta_id)
        if not metadata:
            raise MetadataNotFoundException(f"Metadato con id: {meta_id} no encontrado.")
        return metadata

    # Actualizar metadato
    def update_metadata(self, meta_id, data):
        updated_metadata = self.repository.update(meta_id, data)
        if not updated_metadata:
            raise MetadataNotFoundException(f"No se pudo actualizar el metadato con ID {meta_id}.")
        return (updated_metadata)

    # Borrar metadato
    def delete_metadata(self, meta_id):
        deleted_metadata = self.repository.delete(meta_id)
        if deleted_metadata:
            return {"message": f"Metadato con id {meta_id} borrado con exito."}
        else:
            raise MetadataNotFoundException(f"Metadato con id: {meta_id} no encontrado.")
