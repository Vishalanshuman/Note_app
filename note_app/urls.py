from django.urls import path
from .views import NoteView, NoteDeletePutGetView

urlpatterns = [
    path("note/", NoteView.as_view()),
    path("note/<int:id>/", NoteDeletePutGetView.as_view()),

    
]

