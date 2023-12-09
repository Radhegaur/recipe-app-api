"""
Django command to wait for db available 
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""
    
    def handle(self, *args, **options):
        pass