#/project/config.py 

import os

#Debug defaults to true if running locally
if os.getenv('REMOTE', 0):
    DEBUG  = False
else:
    DEBUG  = True

if os.getenv('STAGING', 0):
    STAGING = True
else:
    STAGING = False

CSRF_ENABLED = True
SECRET_KEY = 'guessthisone' ## need to make it as the below