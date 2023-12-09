"""Django command to wait for db available """

import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for databse........')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Databse unavailable, waiting 1 second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Databse available!'))
