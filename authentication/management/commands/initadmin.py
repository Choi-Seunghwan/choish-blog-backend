from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = os.getenv('DJANGO_INITSUPERUSER')
            email = os.getenv('DJANGO_INITSUPERUSEREM')
            pw = os.getenv('DJANGO_INITSUPERUSERPW')
            
            print( 'Creating account ', username, email)
            User.objects.create_superuser(username, email, pw)
            