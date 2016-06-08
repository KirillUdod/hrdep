from django.conf.urls import url


from .views import MainView, Game1View, Game2View, IndexView

urlpatterns = [

    url(r'^$', MainView.as_view(), name='main'),

    url(r'^games/$', IndexView.as_view(), name='index'),
    url(r'^game1/$', Game1View.as_view(), name='game1'),
    url(r'^game2/$', Game2View.as_view(), name='game2')

]