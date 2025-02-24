from infrastructure.db.database import db
from infrastructure.db.models.org_metadata_model import OrgMetadata
from infrastructure.db.models.organization_model import Organization


def initialize_db():
    with db:
        db.create_tables([Organization, OrgMetadata], safe=True) #Safe = True evita crear tablas existentes de nuevo.
        print("Tablas creadas correctamente.")


if __name__ == '__main__':
    initialize_db()
