import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today}.tar.ga")
    print(backup_files_name)
    shutil.make_archive(backup_files_name.replace('.tar.gz',''),'gztar',source)

source = "/home/ritik/workshop"
destination = "/home/ritik/workshop/backups"
backup_files(source, destination)
