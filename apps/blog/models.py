import os, datetime
from django.db import models

from apps.user.models import CustomUser
from django.utils.translation import ugettext_lazy as _


def create_file_path(self, filename):
    """
    Function which defines the path for the uploaded files for a blog
    :param self:
    :param filename: the file name
    :return: the path where the uploaded file is going to be saved
    """
    timestamp = datetime.datetime.now().timestamp()
    return os.path.join(self.title + "/" + 'post_files' + "/" + str(int(timestamp)) + filename)


def create_image_path(self, filename):
    """
    Function which defines the path for the uploaded images for a blog
    :param self:
    :param filename: the file name
    :return: the path where the uploaded file is going to be saved
    """
    timestamp = datetime.datetime.now().timestamp()
    return os.path.join(self.title + "/" + 'post_images' + "/" + str(int(timestamp)) + filename)


class Blog(models.Model):
    """
    Model blog which represents the post functionality
    """

    class Meta:
        db_table = 'blog'
        verbose_name = _('blog')
        verbose_name_plural = _("blog's")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(verbose_name=_("Attachment"),
                            upload_to=create_file_path,
                            blank=True,
                            max_length=500
                            )
    title = models.CharField(_("title"), blank=False, max_length=128)
    image = models.ImageField(_("post image"),
                              blank=False,
                              max_length=500,
                              upload_to=create_image_path,
                              default="images/no_img_available.jpg",
                              )
    content = models.TextField(_("post content"), blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'post {self.id}  - {self.title}'
