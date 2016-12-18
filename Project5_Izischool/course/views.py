from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from course.forms import CourseForm
from course.models import course
from course.serializers import CourseSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class ListCourseView(View):
    template_name = "list_course.html"

    def get(self, request):
        c = course.objects.all()
        paginator = Paginator(c, 8)
        pageNumber = request.GET.get('page')
        try:
            list = paginator.page(pageNumber)
        except PageNotAnInteger:
            list = paginator.page(1)
        except EmptyPage:
            list = paginator.page(paginator.num_pages)
        context = {
            'list': list
        }
        return render(request, self.template_name, context)


class PostCourseView(View):
    template_name = "add_course.html"
    form = CourseForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        errors = ""
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['image']
            static_path = '/static/product/img/' + f.name
            default_storage.save('course/' + static_path, ContentFile(f.read()))
            course(
                name=form.data.get("name"),
                subtitle=form.data.get("subtitle"),
                image=static_path,
                price=form.data.get("price"),
                hitcount=0
            ).save()
        else:
            errors = "Error!"
        return render(request, self.template_name, {"form": self.form, "errors": errors})


class DetailCourseView(View):
    name = "detail_course.html"

    def get(self, request, ex_id):
        course_detail = course.objects.get(pk=ex_id)

        context = {
            'detail': course_detail
        }
        return render(request, self.name, context)



class EditCourseView(View):
    name = "edit_course.html"
    form = CourseForm

    def get(self, request, ex_id):
        # self.form = TemplateForm(request.GET, request.FILES).data
        des = course.objects.get(pk=ex_id)
        self.form = des
        context = {
            'course': des,
            'form': self.form
        }
        return render(request, self.name, context)

    # def post(self, request, ex_id, static_path=None):
    #     global cou
    #     form = CourseForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         cou = course.objects.get(pk=ex_id)
    #         if len(request.FILES) > 0:
    #             f = request.FILES['image']
    #             static_path = '/static/product/img/' + f.name
    #             default_storage.save('course/' + static_path, ContentFile(f.read()))
    #             cou.image = static_path
    #         cou.name = self.form.data.get("name"),
    #         cou.subtitle = self.form.data.get("subtitle"),
    #         cou.price = self.form.data.get("price"),
    #         cou.save()
    #     cou.name = request.POST["name"]
    #     cou.subtitle = request.POST["subtitle"]
    #     cou.image = static_path
    #     cou.price = request.POST["price"]
    #     context = {
    #                 "course": cou
    #             }
    #     return render(request, self.name, context)

    @csrf_exempt
    def post(request, cou_id):
        try:
            cou = course.objects.get(pk=cou_id)
        except cou.DoesNotExist:
            errors = "Error!"
            return HttpResponse(status=400)

        # if request.method == 'GET':
        #     serializer = CourseSerializer(cou)
        #     return JSONResponse(serializer.data)
        data = JSONParser().parse(request)
        serializer = CourseSerializer(cou, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


#
class DeleteCourseView(View):
    name = "list_course.html"

    def get(self, request, ex_id):
        des = course.objects.get(pk=ex_id)
        des.delete()
        ex = course.objects.all()
        context = {
            'course': ex
        }
        return render(request, self.name, context)


class SearchCourse(View):
    template_name = "list_course.html"

    def get(self,request, name):
        c = course.objects.filter(name=name)
        paginator = Paginator(c, 8)
        pageNumber = request.GET.get('page')
        try:
            list = paginator.page(pageNumber)
        except PageNotAnInteger:
            list = paginator.page(1)
        except EmptyPage:
            list = paginator.page(paginator.num_pages)
        context = {
            'list': list,
            'nameCourse':name
        }
        return render(request, self.template_name, context)