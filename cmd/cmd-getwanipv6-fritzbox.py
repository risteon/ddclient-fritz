#!/usr/bin/python3

import os
from pathlib import Path
import sys

from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzConnectionException

# cache API in file
cache_kwargs = {
    "cache_directory": Path("/var/cache/ddclient"),
    "cache_format": "json",
    "use_cache": True,
}

try:
    fritz_address = os.environ["FRITZ_ADDRESS"]
except KeyError:
    sys.exit(1)

try:
    # make sure that env vars FRITZ_USERNAME and FRITZ_PASSWORD are set
    fc = FritzConnection(address=fritz_address, **cache_kwargs)

    response = fc.call_action("WANPPPConnection", "GetInfo")
    print(response["NewExternalIPAddress"])
    sys.exit(0)

except FritzConnectionException:
    sys.exit(1)
