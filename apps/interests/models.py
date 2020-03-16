from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.user.models import CustomUser


class Interest(models.Model):
    """
    Interest Model which holds all the interests for a user
    """

    class Meta:
        db_table = 'interest'
        verbose_name = _('interest')
        verbose_name_plural = _("interest's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(_("content"), blank=False)

    def __str__(self):
        return f'Interest: {self.id} - {self.user}'
