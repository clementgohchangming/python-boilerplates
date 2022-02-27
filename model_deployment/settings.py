"""
A settings file which contains all environment variables used by the service.
"""

import os

"""
LOGGING_LEVEL - contains the highest logging level to be used for logging
WARN        <- highest
INFO
DEBUG       <- lowest
"""
LOGGING_LEVEL: str = str(os.getenv("LOGGING_LEVEL", "DEBUG"))