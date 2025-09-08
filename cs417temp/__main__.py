import sys
from pathlib import Path

from cs417temp.parse_temps import parse_raw_temps

with Path(sys.argv[1]).open() as o:
    print(list(parse_raw_temps(o)))
