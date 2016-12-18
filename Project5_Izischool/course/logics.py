from rest_framework import status

from course.repositories import CourseRepository
from course.serializers import CourseSerializer


class CourseLogic:
    def get_course_list(self):
        des = CourseRepository.get_course_list(self)
        serializer = CourseSerializer(des, many=True)
        return serializer.data

    def get_course_detail(self, ex_id: int):
        return CourseRepository.get_course_detail(self,ex_id=ex_id)

    def post_course(self, data: dict):
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return CourseRepository.post_course(self, data=data)
        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def put_course(self, ex_id: int, data: dict):
        des = CourseRepository.get_course_detail(self, ex_id=ex_id)
        serializer = CourseSerializer(des, data=data)
        if serializer.is_valid():
            serializer.save()
            return CourseRepository.put_course(self, ex_id=ex_id, data=data)
        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_course(self, ex_id: int):
        return CourseRepository.delete_course(self, ex_id=ex_id)

    def search_course(self, name:str):
        des = CourseRepository.search_course(self,name=name)
        serializer = CourseSerializer(des, many=True)
        return serializer.data
