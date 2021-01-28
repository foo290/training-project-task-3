from django.shortcuts import render, HttpResponse, redirect
from django.http.request import HttpRequest
from .forms import UploadImageForm
from logger_service import get_custom_logger

putlog = get_custom_logger(__name__)


# Create your views here.

def uploader(request: HttpRequest) -> HttpResponse:
    putlog.debug('Request received on uploader...')

    if request.method == 'POST':
        putlog.info('Request is POST request.')
        form = UploadImageForm(request.POST, files=request.FILES)

        if form.is_valid():
            putlog.debug('Form is valid, Saving form and redirecting to "upload_success" route.')
            form.save()
            return redirect('upload_success')
        else:
            putlog.error('Form was invalid')
    else:
        putlog.warning('request was not POST, creating blank form')
        form = UploadImageForm()

    context = {
        'upload_form': form
    }

    return render(request, template_name='image_uploader/uploadView.html', context=context)


def uploaded(request: HttpRequest):
    putlog.info('Uploaded successful')
    return render(request, template_name='image_uploader/uploadedSuccessfully.html')

