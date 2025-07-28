from django.contrib import admin
from .models import BogieDetails, BogieChecksheet, BMBCChecksheet, FormData
# Register your models here.


admin.site.register(FormData)
admin.site.register(BogieDetails)
admin.site.register(BogieChecksheet)
admin.site.register(BMBCChecksheet)