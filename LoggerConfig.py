import os

# how will you ask for the logs?
# example
# http://localhost:8000/sekritDokuments
URL = "sekritDokuments"

# what folder to check if it is writeable
LOG_FILE_FOLDER_PATH = "/tmp"

# where to save the logs
LOG_FILE_FULL_PATH = LOG_FILE_FOLDER_PATH+"/django_access.log"

# http://localhost:8000/sekrit_url?param=pass
AUTH_PARAMETER = 'param' #secret parameter
AUTH_KEY = "pass" #secret value