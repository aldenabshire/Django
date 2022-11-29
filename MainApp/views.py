from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    """The home page for Learning Log."""
    return render(request, 'MainApp/index.html')

def topics(request):

    topics = Topic.objects.order_by('-date_added')

    context = {'t':topics}

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):

    t = Topic.objects.get(id = topic_id)
    entries = Entry.objects.filter(topic = t)

    context = {'topic':t, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

    