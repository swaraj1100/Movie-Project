from django.urls import path
from movie_app import views
app_name='movie_app'
urlpatterns = [

    path('',views.index,name="index"),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete, name='delete')
]

