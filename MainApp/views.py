from django.shortcuts import render, redirect
from .models import *
from .forms import *

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

def new_topic(request):

    if request.method != 'POST':

        form = TopicForm()

    else:

        print(request.POST)
        form = TopicForm(data = request.POST)

        if form.is_valid():

            form.save()
            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)


def new_entry(request, topic_id):

    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':

        form = EntryForm()

    else:

        print(request.POST)
        form = EntryForm(data = request.POST)

        if form.is_valid():

            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic', topic_id = topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)

