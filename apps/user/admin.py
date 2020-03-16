from .models import CustomUser, Address, Profile
from django.contrib import admin
from django.contrib.sessions.models import Session
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import pprint


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')

    _session_data.allow_tags = True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy = 'expire_date'


admin.site.register(Session, SessionAdmin)
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(Profile)
