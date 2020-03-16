from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from apps.user.models import CustomUser


class Project(models.Model):
    """
    Address Model which holds all the address data for a user
    """

    class Meta:
        db_table = 'project'
        verbose_name = _('project')
        verbose_name_plural = _("project's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=256, blank=False)
    link = models.URLField(_("link"), max_length=256, blank=True)
    description = models.TextField(_("description"), blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Project: {self.id} - {self.user.email}'
