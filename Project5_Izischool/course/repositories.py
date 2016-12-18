from rest_framework import status
from course.models import course


class CourseRepository:
    def get_course_list(self):
        return course.objects.all()

    def get_course_detail(self, ex_id: int):
        return course.objects.get(pk=ex_id)

    def post_course(self, data: dict):
        return data, status.HTTP_201_CREATED

    def put_course(self, ex_id: int, data: dict):
        return data, status.HTTP_200_OK

    def delete_course(self,ex_id:int):
        CourseRepository.get_course_detail(self, ex_id=ex_id).delete()
        return status.HTTP_204_NO_CONTENT

    def search_course(self,name:str):
        return course.objects.filter(name=name)