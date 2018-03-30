import numpy as np
import json
import os
import django
import sys

# you have to set the correct path to you settings module
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Planit.Planit.settings")
django.setup()

# import the django module
from .models import Section

# loads in the json files
with open('id_to_name_mapping.json', 'r') as f:
	id_to_name_mapping = json.loads(f.read())

with open('show_data.json', 'r') as f:
	db = json.loads(f.read())
request = None


