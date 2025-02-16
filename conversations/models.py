from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStapedModel):
    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStapedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    Conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says {self.text}"

