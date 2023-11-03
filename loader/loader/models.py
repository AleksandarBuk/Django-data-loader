from django.db import models


class TestModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    # ... add all fields based on your CSV ...

    def __str__(self):
        return self.field1
