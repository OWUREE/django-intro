import datetime
from django.db import models
from django.utils import timezone

class DustBin(models.Model):
    PLASTIC = "P"
    METAL = "M"
    OTHERS = "O"
    TYPES=(
        (PLASTIC,"plastic"),
        (METAL,"metal"),
        (OTHERS,"others")
    )
    type = models.CharField (choices=TYPES, max_length=1)
    level = models.IntegerField()
    date_time = models.DateField(auto_now_add=True)
    comment = models.TextField()
    has_been_emptied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type}-{self.level}"
