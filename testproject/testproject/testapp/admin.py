from django.contrib import admin
from wiretap.admin import MessageAdmin

from .models import UserMessage

class UserMessageAdmin(MessageAdmin):
    list_display = ('request', 'response', 'remote_addr', 'duration', 'user',)
    list_filter = ('started_at', 'req_method', 'res_status_code',)
    search_fields = ('remote_addr', 'req_path', 'user__username',)

admin.site.register(UserMessage, UserMessageAdmin)
