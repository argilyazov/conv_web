from django.db import models

# Create your models here.


from django.db import models

class Files(models.Model):
    title = models.CharField(max_length=255, default='no title')
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.title


class MainPageDataFormats(models.Model): # Модель
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class MainPageFormats(models.Model):
    source_format = models.TextField()
    result_format = models.TextField()
    url = models.TextField()

class MainPage(models.Model):
    title = models.CharField(max_length=255)
    app_description = models.TextField()
    formats_title = models.CharField(max_length=255)
    formats_help = models.TextField()
    convertation_formats = models.JSONField(default=list, blank=True)
    data_formats = models.JSONField(default=list, blank=True)
    confidentiality_title = models.CharField(max_length=255)
    confidentiality_text = models.TextField()
    tagline = models.TextField()
    communities = models.JSONField(default=list, blank=True)
    def __str__(self):
        return self.title

class ConvertorFormatTitle(models.Model):
    source_format = models.TextField()
    result_format = models.TextField()

class ConvertorEditor(models.Model):
    title = models.CharField(max_length=255)
    source_cells_title = models.CharField(max_length=255)
    result_cells_title = models.CharField(max_length=255)
    convertor_commands = models.JSONField(default=list, blank=True)
    view_empty_cells = models.JSONField(default=dict, blank=True)
    apply_button_title = models.TextField()

class ConvertorEditor_ViewEmptyCells(models.Model):
    title = models.CharField(max_length=255)
    views = models.JSONField(default=list, blank=True)

class ConvertorViewTextResult(models.Model):
    result_format_title = models.CharField(max_length=255)
    settings = models.JSONField(default=list, blank=True)

class ConvertorViewTextResult_Settings(models.Model):
    type = models.TextField()
    text = models.TextField()
    status = models.BooleanField(default=True)
    status_text = models.TextField()
class Convertor(models.Model):
    format_title = models.JSONField(default=dict, blank=True)
    download_help = models.TextField()
    download_table_title = models.CharField(max_length=255)
    result_table_title = models.CharField(max_length=255)
    editor = models.JSONField(default=dict, blank=True)
    download_button_title = models.CharField(max_length=255)
    view_text_result = models.JSONField(default=dict, blank=True)