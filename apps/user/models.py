from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    """
    Model which represents the user model,
    username is set to None because Email is used as username
    """

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _("user's")

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_profile(self):
        return Profile.objects.get_or_create(user=self)

    def get_address(self):
        return Address.objects.get_or_create(user=self)

    def get_experiences(self):
        from ..experience.models import Experience
        return Experience.objects.filter(user=self)

    def get_educations(self):
        from ..education.models import Education
        return Education.objects.filter(user=self)

    def get_skills(self):
        from ..skills.models import Tool
        return Tool.objects.filter(user=self)

    def get_interests(self):
        from ..interests.models import Interest
        return Interest.objects.filter(user=self)

    def get_awards(self):
        from ..awards.models import Award
        return Award.objects.filter(user=self)

    def get_projects(self):
        from ..project.models import Project
        return Project.objects.filter(user=self)


class Address(models.Model):
    """
    Address Model which holds all the address data for a user
    """

    class Meta:
        db_table = 'address'
        verbose_name = _('address')
        verbose_name_plural = _("address's")

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    street = models.CharField(_("street"), max_length=255, blank=True)
    address = models.CharField(_("address"), max_length=150, blank=True)
    city = models.CharField(_("city"), max_length=255, blank=True)
    state = models.CharField(_("state"), max_length=255, blank=True)
    zip_code = models.CharField(_("zip_code"), max_length=15, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Address: {self.id} - {self.user}'


class Profile(models.Model):
    """
    Address Model which holds all the profile data for a user
    """
    GENDER_CHOICES = (
        ('1', _('Male')),
        ('2', _('Female')),
        ('3', _('Not Specified')),
    )

    class Meta:
        db_table = 'profile'
        verbose_name = _('profile')
        verbose_name_plural = _("profile's")

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_profile", primary_key=True)
    gender = models.CharField(verbose_name=_("gender"), max_length=140, choices=GENDER_CHOICES, blank=True)
    profile_picture = models.ImageField(verbose_name=_("profile picture"), upload_to="images",
                                        default='images/default_profile.jpg',
                                        blank=False, max_length=500)
    birthday = models.DateField(_("birthday"), blank=True, )
    telephone = models.CharField(_("telephone"), max_length=128, blank=True)
    website = models.URLField(verbose_name=_("website"), blank=True)
    linkedin = models.URLField(verbose_name=_("linkedin"), blank=True)
    github = models.URLField(verbose_name=_("github"), blank=True)
    gitlab = models.URLField(verbose_name=_("gitlab"), blank=True)
    facebook = models.URLField(verbose_name=_("facebook"), blank=True)
    twitter = models.URLField(verbose_name=_("twitter"), blank=True)
    google_plus = models.URLField(verbose_name=_("google plus"), blank=True)
    biography = models.TextField(verbose_name=_("biography"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile: {self.pk} - {self.user.email}'
