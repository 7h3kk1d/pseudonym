# Create your views here.
from django.shortcuts import render
from notes.models import Note
from django.http import Http404

def index(request):
    latest_note_list = Note.objects.order_by('-pub_date')[:5]
    context = {
        'latest_note_list': latest_note_list,
    }
    return render(request, 'notes/index.html',context)
def output(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
            raise Http404
    return render(request, 'notes/output.html', {'note': note})
