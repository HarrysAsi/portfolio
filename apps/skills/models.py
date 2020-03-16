from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.user.models import CustomUser


class ToolType(models.Model):
    """
    Sponsor Type model which represents the available types for a sponsor
    """

    class Meta:
        db_table = 'tool_type'
        verbose_name = _('tool_type')
        verbose_name_plural = _("tool_type's")

    desc_code = models.CharField(_("desc_code"), max_length=128, blank=False, default="")
    description = models.CharField(_("description"), max_length=128, blank=False)

    def __str__(self):
        return f'ToolType {self.id} - {self.description}'


class Tool(models.Model):
    """
    Address Model which holds all the address data for a user
    """

    class Meta:
        db_table = 'tool'
        verbose_name = _('tool')
        verbose_name_plural = _("tool's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(ToolType, on_delete=models.SET_NULL, blank=True, null=True)
    tool_description = models.CharField(_("tool or language"), max_length=255, blank=False)
    tool_image = models.CharField(_("tool image(ex:fab fa-html5)"), max_length=128, blank=True)
    qualification_rating = models.IntegerField(_("qualification_rating"), blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Tool: {self.id} - {self.user.email}'
