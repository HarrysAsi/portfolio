from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from apps.user.models import CustomUser


class Education(models.Model):
    """
    Education Model which holds all the educational data for a user
    """

    class Meta:
        db_table = 'education'
        verbose_name = _('education')
        verbose_name_plural = _("education's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school_name = models.CharField(_("school name"), max_length=255, blank=False)
    degree_title = models.CharField(_("degree title"), max_length=255, blank=False)
    information = models.CharField(_("information"), max_length=255, blank=True)
    gpa = models.FloatField(_("gpa"), blank=True)
    date_started = models.DateField(_("date started"), blank=True)
    date_ended = models.DateField(_("date ended"), blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Education: {self.id} - {self.user.email}'
