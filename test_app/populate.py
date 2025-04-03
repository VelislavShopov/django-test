import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","Django.settings")

from faker import Faker
django.setup()
from test_app.models import User

fake = Faker()

for _ in range(10):
    User.objects.create(firstName = fake.first_name(), lastName = fake.last_name(), email = fake.email())