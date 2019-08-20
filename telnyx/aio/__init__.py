import sys

if sys.version_info < (3, 6):
    raise Exception("Python >= 3.6 required for telnyx.async")
