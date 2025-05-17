import os
from tokenize import group

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

django.setup()

#From users.models import User, group

#new_group = Group(name='Ученики')

#new_group.save()

#user = User.ojects.create(username="admin",
#                          email='admin@gmail.com', role='admin')