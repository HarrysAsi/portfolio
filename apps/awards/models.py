import os, datetime
from django.db import models

from apps.user.models import CustomUser
from django.utils.translation import ugettext_lazy as _


def create_file_path(self, filename):
    """
    Function which defines the path for the uploaded images for a product
    :param self:
    :param filename: the file name
    :return: the path where the uploaded file is going to be saved
    """
    timestamp = datetime.datetime.now().timestamp()
    return os.path.join(self.title + "/" + 'award_files' + "/" + str(int(timestamp)) + filename)


class Award(models.Model):
    """
    Model award which represents the awards for a user
    """

    class Meta:
        db_table = 'award'
        verbose_name = _('award')
        verbose_name_plural = _("award's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(verbose_name=_("Attachment"),
                            upload_to=create_file_path,
                            blank=True,
                            null=True,
                            max_length=500)
    title = models.CharField(_("title"), blank=False, max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'post {self.id}  - {self.title}'
