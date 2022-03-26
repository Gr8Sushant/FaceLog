from django.contrib import admin
from django.urls import path
from AMS import views
from AMS import adminViews

from FaceLog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('login', views.showLoginPage),

    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    
    path('doLogin', views.doLogin),


    path('admin_home', adminViews.admin_home, name="admin_home"),
    path('add_course', adminViews.add_course,name="add_course"),
    path('add_course_save', adminViews.add_course_save,name="add_course_save"),
    path('add_student', adminViews.add_student,name="add_student"),
    path('add_student_save', adminViews.add_student_save,name="add_student_save"),
    path('add_level', adminViews.add_level,name="add_level"),
    path('add_level_save', adminViews.add_level_save,name="add_level_save"),
    path('manage_student', adminViews.manage_student,name="manage_student"),
    path('manage_course', adminViews.manage_course,name="manage_course"),
    path('manage_level', adminViews.manage_level,name="manage_level"),
    path('edit_student/<str:student_id>', adminViews.edit_student,name="edit_student"),
    path('edit_student_save', adminViews.edit_student_save,name="edit_student_save"),
    path('edit_level/<str:level_id>', adminViews.edit_level,name="edit_level"),
    path('edit_level_save', adminViews.edit_level_save,name="edit_level_save"),
    path('edit_course/<str:course_id>', adminViews.edit_course,name="edit_course"),
    path('edit_course_save', adminViews.edit_course_save,name="edit_course_save"),





    # path('', views.stream, name='index'),
    # path('stream', views.stream, name='stream'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)