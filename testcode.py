import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import *

topics = Topic.objects.all()

print(topics)

for t in topics:

    print(t.text)
    print(t.date_added)

chess = Topic.objects.get(id = 1)
print(chess.text)

entries = Entry.objects.filter(topic = chess)

for e in entries:

    print(e.text)
    print(e.date_added)

from django.contrib.auth.models import User

for user in User.objects.all():

    print(user.username)
    print(user.last_login)