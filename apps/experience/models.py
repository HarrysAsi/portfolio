from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.user.models import CustomUser


class Experience(models.Model):
    """
    Address Model which holds all the address data for a user
    """

    class Meta:
        db_table = 'experience'
        verbose_name = _('experience')
        verbose_name_plural = _("experience's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(_("job title"), max_length=255, blank=False)
    company_name = models.CharField(_("company name"), max_length=255, blank=False)
    job_description = models.TextField(_("job role"), blank=True)
    date_started = models.DateField(_("date started"), blank=True)
    date_ended = models.DateField(_("date ended"), blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Experience: {self.id} - {self.user}'
