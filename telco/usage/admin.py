from django.contrib import admin

from telco.usage.models import UsageSpecCharacteristic, VoiceCallUsage, UsageCharacteristicValue

admin.site.register(VoiceCallUsage)
admin.site.register(UsageSpecCharacteristic)
admin.site.register(UsageCharacteristicValue)