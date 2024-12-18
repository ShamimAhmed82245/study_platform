from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Note
import pytesseract
from PIL import Image
from django.core.files.storage import default_storage

# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def is_teacher(user):
    return user.role == 'teacher'


@login_required
@user_passes_test(is_teacher)
def approve_notes(request,note_id):
    note = Note.objects.get_or_404(id=note_id)
    note.is_approved=True
    note.save()
    return redirect('notes_list')

def upload_note_view(request):
    if request.method=='POST':
        title = request.POST['title']
        file = request.FILES['file']

        saved_path = default_storage.save(file.name, file)
        absolute_path = default_storage.path(saved_path)  # Get absolute file path

        if file.name.endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(absolute_path)  # Open the file using absolute path
            extracted_text = pytesseract.image_to_string(image)

        elif file.name.endswith('.pdf'):
            extracted_text = "PDF OCR Processing Logic Here"

        else:
            extracted_text = ''

        # Save the extracted content to the database
        obj=Note.objects.create(
            title=title,
            uploaded_by=request.user,
            file=file,
            content=extracted_text
        )
        print(obj)
        return redirect('notes_list')
    return render(request,'notes/uploaded_note.html')


def note_lists(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/note_lists.html',{"notes":all_notes})