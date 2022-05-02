from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView, form_submit,post_detailview,UpdateCommentVote
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='home'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('about/',views.about, name='about'),
    path('post/enlarge/<int:pk>/',views.post_detailview, name='discussion'),
    path('post/discussion/delete/<int:id>/', views.deletecomment, name='delete_com'),
    path('post/discussion/review/<int:comment_id>/<str:option>',UpdateCommentVote.as_view(),name='review'),
    path('city', views.city, name="weather"),
    path('form',views.form_submit, name="form")
]