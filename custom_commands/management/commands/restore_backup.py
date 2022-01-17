from os import getenv, system
from django.core.management.base import BaseCommand
from requests import post
#########################

class Command(BaseCommand):
    '''Restore backup command'''

    def handle(self, *args, **kwargs):
        '''Restore backup from elephantsql database'''

        Get_backup_id = input(str('\nPlease enter backup id : '))
        while len(Get_backup_id) <= 1:
            Get_backup_id = input(str('\nPlease enter backup id : '))

        Confirmation = input(str(f'Are you sure you want to restore the {Get_backup_id} backup ID? (y/n) : '))
        if Confirmation.lower() == 'y' or Confirmation.lower() == 'yes':
            self.stdout.write(self.style.WARNING('\nOkay, pleas wait...\n'))

            # Parameters
            url = 'https://api.elephantsql.com/api/backup/restore'
            data = {
                'backup_id': Get_backup_id
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
                    self.stdout.write(self.style.SUCCESS(f'Result :\n\n{req}\nBackup restored successfully.'))
                
                elif req.json()['message'] == 'Not found':
                    self.stdout.write(self.style.ERROR('The backup ID is not correct !'))
            
            except Exception as e:
                # print error
                self.stdout.write(self.style.ERROR(e))

        else:
            self.stdout.write(self.style.WARNING('\nThe action was canceled.'))