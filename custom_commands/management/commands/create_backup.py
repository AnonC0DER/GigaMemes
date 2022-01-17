from os import getenv, system
from django.core.management.base import BaseCommand
from requests import post
#########################

class Command(BaseCommand):
    '''Create Backup command'''

    def handle(self, *args, **kwargs):
        '''Create a new backup from elephantsql database'''
        self.stdout.write(self.style.WARNING('\nOkay, pleas wait...\n'))

        # Parameters
        url = 'https://api.elephantsql.com/api/backup'
        data = {
            'db' : f'{getenv("NAME")}'
        }
        auth = ('', f'{getenv("DB_API_TOKEN")}')

        try:
            # Create request 
            req = post(url, data=data, auth=auth)
            # Check the status code
            if req.status_code == 200:
                # Clear terminal
                system('clear')
                # print result
                self.stdout.write(self.style.SUCCESS(f'Result :\n\n{req}\nBackup created successfully.'))

        except Exception as e:
            # print error
            self.stdout.write(self.style.ERROR(e))