from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'course_api'

'''router = DefaultRouter()
router.register('', CourseList, basename='course')
urlpatterns = router.urls
'''

urlpatterns = [
    path('course/<int:pk>/', CourseDetail.as_view(), name='detailcourse'),
    path('search/', CourseListDetailfilter.as_view(), name='coursesearch'),
    path('course/create/', CreateCourse.as_view(), name='createcourse'),
    path('', CourseList.as_view(), name='listcreate'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/create/', ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),

    #path('edit/postdetail/<int:pk>/', AdminCourseDetail.as_view(), name='admindetailcourse'),
    #path('edit/<int:pk>/', EditCourse.as_view(), name='editcourse'),
    #path('delete/<int:pk>/', DeleteCourse.as_view(), name='deletecourse'),

]

