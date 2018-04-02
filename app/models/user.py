"""
Author:
Date:
"""
from mongoengine import Document
from mongoengine.fields import StringField, URLField, DateTimeField

class User(Document):
    """
    App project mongo model
    """
    name = StringField(max_length=24, required=True)
    surname = StringField(max_length=24, required=True)

    @property
    def created(self):
        return self.id.generation_time.isoformat() if self.id else None

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'surname': self.surname,
        }
