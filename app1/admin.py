from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(MainPageDataFormats)
admin.site.register(MainPageFormats)
admin.site.register(MainPage)
admin.site.register(ConvertorFormatTitle)
admin.site.register(ConvertorEditor)
admin.site.register(ConvertorEditor_ViewEmptyCells)
admin.site.register(ConvertorViewTextResult)
admin.site.register(ConvertorViewTextResult_Settings)
admin.site.register(Convertor)

