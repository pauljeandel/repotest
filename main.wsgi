#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/paul/boutigo/aiwriter/')
from main import app as application
application.secret_key = 'boutigo.clefsecrete.flask'