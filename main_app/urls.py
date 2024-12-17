from django.urls import path
from .views import upload_note_view,approve_notes
app_name = 'main_app'
urlpatterns = [
    path('upload-note/', upload_note_view,name='uploaded_note' ),
    path('note-lists/<int:note_id>/',approve_notes,name='note_lists'),
]
