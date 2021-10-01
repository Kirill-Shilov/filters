from django.db import transaction
from django.core.management.base import BaseCommand
from ..factory import TableFactory


class Command(BaseCommand):
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        for _ in range(0, 1000):
            TableFactory()


