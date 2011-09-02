import json
import sys
import os
import subprocess

if __name__ == "__main__":
    config_location = sys.argv[1]
    
    config = json.load(open(config_location))
    for db_name, settings in config.items():
        print db_name
        print settings
        
        os.chdir(settings['dir'])
        
        retcode = subprocess.call(["mysqldump", "-u"+settings['user'], "-p"+settings['pass'], "-r foo_db.dump"])
