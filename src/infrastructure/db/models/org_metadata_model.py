import uuid
from datetime import datetime

from peewee import Model, UUIDField, CharField, TextField, DateTimeField, ForeignKeyField, TimestampField

from infrastructure.db.database import db
from infrastructure.db.models.organization_model import Organization


# Modelo para ORG_METADATA
class OrgMetadata(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)  # ID único
    organization = ForeignKeyField(Organization, backref="metadata", on_delete="CASCADE")
    key = CharField(max_length=255)
    value = TextField()
    date_created = TimestampField(default=datetime.now)
    date_modified = TimestampField(default=datetime.now)

    class Meta():
        database = db
        table_name = "orgs_metadata"

    def save(self, *args, **kwargs):
        """Sobreescribimos save() para actualizar date_modified en cada cambio."""
        self.date_modified = datetime.now()
        return super().save(*args, **kwargs)
