from email.mime import base
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('schools', views.SchoolViewSet)

school_router = routers.NestedDefaultRouter(
    router, 'schools', lookup='school')
school_router.register('students', views.SchoolStudentViewSet,
                       basename='school-students')


# URLConf
urlpatterns = router.urls + school_router.urls