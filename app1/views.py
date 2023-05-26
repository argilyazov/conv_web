from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import MainPageSerializer, ConvertorSerializer
from files.models import *
from files.forms import *
from .Convertor_app import *



def index_page(request):
    formats = MainPageFormats.objects.all()
    return render(request, 'main/index.html', {"formats": formats})

class Views():
    def __init__(self):
        self.converter = None
    def post_editor(self,request):
        form_select = ResumeForm
        form_editor = EditorForm(request.POST, request.FILES)
        if form_editor.is_valid():
            form_editor.save()

            command = Editor.objects.last()
            ex_cmd = (command.command, command.source.split(), command.result.split())

            self.converter.execute(ex_cmd)
            # Files.objects.create(converter.to_excel())
            return render(request, 'main/excelToExcel.html',
                          {"table_result_header": list(self.converter.result),
                           "table_source_header": list(self.converter.original),
                           "table_source": self.converter.original.values.tolist(),
                           "table_result": self.converter.result.values.tolist(), "form_select": form_select,
                           "form_editor": form_editor})

    def exceltoexcel_page(self,request):
        form_editor = EditorForm

        if request.method == 'POST':
            form_select = ResumeForm(request.POST, request.FILES)
            if form_select.is_valid():
                form_select.save()
                # return HttpResponseRedirect("/")
                db_file = Files.objects.last().file
                self.converter = Convertor_app(db_file)
                return render(request, 'main/excelToExcel.html', {"table_result_header": list(self.converter.result),
                                                                  "table_source_header": list(self.converter.original),
                                                                  "table_source": self.converter.original.values.tolist(),
                                                                  "table_result": self.converter.result.values.tolist(),
                                                                  "form_select": form_select,
                                                                  "form_editor": form_editor})
        else:
            form_select = ResumeForm

        return render(request, 'main/excelToExcel.html', {"form_select": form_select, "form_editor": form_editor})



def wordtoexcel_page(request):
    return render(request, 'main/wordtoexcel.html')


def exceltojson_page(request):
    return render(request, 'main/exceltojson.html')


class MainPageAPIView(APIView):  # Представления 1
    def get(self, request):
        json_model = MainPage.objects.first()
        conv_formats = MainPageFormats.objects.all()
        data_formats = MainPageDataFormats.objects.all()
        json_model.convertation_formats = [{'source_format': conv_format.source_format,
                                            'result_format': conv_format.result_format} for conv_format in conv_formats]
        json_model.data_formats = [{'title': data_format.title,
                                    'description': data_format.description} for data_format in data_formats]
        json_model.communities = ['exam1', 'exam2']
        json_model.save()
        json_result = MainPage.objects.all()
        return Response(MainPageSerializer(json_result, many=True).data)


class ConvertorAPIView(APIView):
    def get(self, request):
        convertor_model = Convertor.objects.first()
        format_title = ConvertorFormatTitle.objects.first()
        editor = ConvertorEditor.objects.first()
        editor_view_empty_cells = ConvertorEditor_ViewEmptyCells.objects.first()
        vtc = ConvertorViewTextResult.objects.first()
        vtc_settings = ConvertorViewTextResult_Settings.objects.first()

        convertor_model.format_title['source_format'] = format_title.source_format
        convertor_model.format_title['result_format'] = format_title.result_format

        convertor_model.editor['title'] = editor.title
        convertor_model.editor['source_cells_title'] = editor.source_cells_title
        convertor_model.editor['result_cells_title'] = editor.result_cells_title
        convertor_model.editor['convertor_commands'] = ['exam1', 'exam2']
        convertor_model.editor['view_empty_cells'] = {"title": editor_view_empty_cells.title,
                                                      'views': ['viewsExam1', 'viewsExam2']}
        convertor_model.editor['view_empty_cells']['views'] = ['exam1', 'exam2']
        convertor_model.editor['apply_button_title'] = editor.apply_button_title

        convertor_model.view_text_result['result_format_title'] = vtc.result_format_title
        convertor_model.view_text_result['settings'] = [{'type': vtc_settings.type, 'text': vtc_settings.text,
                                                         'status': vtc_settings.status,
                                                         'status_text': vtc_settings.status_text}]

        convertor_model.save()
        convertor_result = Convertor.objects.all()

        return Response(ConvertorSerializer(convertor_result, many=True).data)
