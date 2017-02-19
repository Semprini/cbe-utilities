from django.contrib import admin

from telco.usage.models import UsageSpecCharacteristic, VoiceCallUsage

admin.site.register(VoiceCallUsage)
admin.site.register(UsageSpecCharacteristic)
