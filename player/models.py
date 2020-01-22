from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Invitation(models.Model):
    from_user = models.ForeignKey(User,
                                  related_name="invitations_sent",
                                  null=True,
                                  on_delete=models.SET_NULL)
    to_user = models.ForeignKey(User,
                                related_name="invitations_received",
                                verbose_name="User to invite",
                                help_text="Please select the user you want to play with",
                                null=True,
                                on_delete=models.SET_NULL)
    message = models.CharField(max_length = 300,
                               blank=True,
                               verbose_name = "Optional Message",
                               help_text = "It's always nice to add an offensive message")
    timestamp = models.DateTimeField(auto_now_add=True)
