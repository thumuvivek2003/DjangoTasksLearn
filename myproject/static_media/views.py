# static_media/views.py

from django.shortcuts import render
from .forms import UploadForm
from .models import UploadedFile

def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()

    images = UploadedFile.objects.all()
    return render(request, 'upload.html', {'form': form, 'images': images})
