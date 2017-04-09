from django.contrib import admin

from utilities.usage.models import UsageSpecCharacteristic, VoiceCallUsage, UsageCharacteristicValue

admin.site.register(VoiceCallUsage)
admin.site.register(UsageSpecCharacteristic)
admin.site.register(UsageCharacteristicValue)