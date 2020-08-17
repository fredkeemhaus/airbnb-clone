from django.db import models
from core import models as core_models


class Review(core_models.TimeStapedModel):
    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.Inaccuracy = models.IntegerField()
    cleanliness = models.Inaccuracy = models.IntegerField()
    loaction = models.Inaccuracy = models.IntegerField()
    check_in = models.Inaccuracy = models.IntegerField()
    value = models.Inaccuracy = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"
