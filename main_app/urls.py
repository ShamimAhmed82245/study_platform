from django.urls import path
from .views import upload_note_view,approve_notes
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView
from .forms import EmailAuthenticationForm

app_name = 'main_app'
urlpatterns = [
    path('upload-note/', upload_note_view,name='uploaded_note' ),
    path('note-lists/<int:note_id>/',approve_notes,name='note_lists'),
    path('login/',LoginView.as_view(template_name='login.html',authentication_form=EmailAuthenticationForm,),name='login'),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
]
