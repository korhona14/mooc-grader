from django.conf.urls import url

from access import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^queue-length$', views.queue_length, name='queue-length'),
    url(r'^test-result$', views.test_result, name='test-result'),
    url(r'^ajax/([\w-]+)/([\w-]+)$', views.exercise_ajax, name='ajax'),
    url(r'^([\w-]+)/$', views.course, name='course'),
    url(r'^([\w-]+)/aplus-json$', views.aplus_json, name='aplus-json'),
    url(r'^([\w-]+)/([\w-]+)$', views.exercise, name='exercise'),
    url(r'^([\w-]+)/([\w-]+)/(\d+)/generatedfile/([\w-]+)$', views.generated_exercise_file,
        name='generated-file'),
]
