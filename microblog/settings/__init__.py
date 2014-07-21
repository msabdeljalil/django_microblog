# Apparently it errored out in D1.4
# if u had settings.base. You need just .base...
from .base import *
try:
    from .local import *
except ImportError:
    pass
