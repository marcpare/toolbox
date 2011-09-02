import json
import datetime
import sys
import os
import subprocess

if __name__ == "__main__":
    config_location = sys.argv[1]
    
    config = json.load(open(config_location))
    for db_name, settings in config.items():
        print "backuping %s" % db_name
        
        os.chdir(settings['dir'])
        now = datetime.datetime.now()
        backup_name = now.strftime("%A")
        
        retcode = subprocess.call(["mysqldump", "-u"+settings['user'], "-p"+settings['pass'], "-r %s"%backup_name, db_name])
