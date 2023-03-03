from django.core.management.base import BaseCommand

import carddatabase.models

# this is messed up
class Command(BaseCommand):
    help = 'Sanitize card names'

    def handle(self, *args, **options):
        for card in carddatabase.models.CardInfo.objects.all():
            card.save()
        self.stdout.write(self.style.SUCCESS('Successfully sanitized card names.'))
