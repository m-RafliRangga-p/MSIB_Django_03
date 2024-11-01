import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contoh_1.settings')

import django
django.setup()

#Fake Populate Script
import random 
from app_1.models import Topic, Webpage, AccesRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #Get the topic for the entry
        top = add_topic()

        #crate fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create a new webpage
        webp = Webpage.objects.get_or_create(topic = top, url=fake_url, name=fake_name)[0]

        # Create a fake acces record
        acc_rec = AccesRecord.objects.get_or_create(name=webp, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating Script...")
    populate(20)
    print("Done")
