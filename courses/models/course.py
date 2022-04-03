from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=120)
    for_class = models.IntegerField()
    description = models.TextField()
    fee = models.IntegerField()
    duration = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table ="course"

    def __str__(self) -> str:
        return self.name