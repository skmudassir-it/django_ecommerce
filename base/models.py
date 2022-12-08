from django.db import models
import uuid


class BaseModel(models.Models):
    uod = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
