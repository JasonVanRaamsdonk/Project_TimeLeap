from django.contrib import admin
from time_leap.models import AccessRecord, Topic, Webpage, Colourise

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Colourise)
