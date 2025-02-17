import uuid
from datetime import datetime

from peewee import Model, UUIDField, CharField, TimestampField

from src.infrastructure.db.database import db


# Modelo para ORGANIZATION
class Organization(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)  # ID único
    customer_id = UUIDField(null=True)  # Puede ser nulo, ya que es una referencia externa
    legal_name = CharField(max_length=300)
    name = CharField(max_length=200)
    direction = UUIDField()
    date_created = TimestampField(default=datetime.now)
    date_modified = TimestampField(default=datetime.now)

    class Meta():
        database = db
        table_name = "organizations"

    def save(self, *args, **kwargs):
        """Sobreescribimos save() para actualizar date_modified en cada cambio."""
        self.date_modified = datetime.now()
        return super().save(*args, **kwargs)
