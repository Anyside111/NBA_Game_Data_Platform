from django.core.management.base import BaseCommand
from app.management.commands.load_data import load_data

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **kwargs):
        load_data()
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
