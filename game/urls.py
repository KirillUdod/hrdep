from django.conf.urls import url


from .views import MainView, IndexView

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^game/$', IndexView.as_view(), name='index')

]