# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# use zipfile methods to list the contents of the zip file
# test your script on the test.zip file

import sys
import zipfile
from zipfile import ZipFile, BadZipFile  # methods in this module can be used

if len(sys.argv) < 2:
    print("Usage: python ziplist.py <file.zip>", file=sys.stderr)            # Gives an error message if user doesnt input a file
    sys.exit(1)

archive_filename = sys.argv[1]
                       
try:
    with ZipFile(archive_filename, "r") as infile:         # Used a zipfile.namelist to list the contents in the zip
        for name in infile.namelist():
            print(name)
except FileNotFoundError:
    print(f"File not found: python ziplist.py {archive_filename}", file=sys.stderr)         # error message for if the file that the user has inputed doesnt exist
    sys.exit(1)

except BadZipFile:
    print(f"Bad zip file: python ziplist.py {archive_filename}", file=sys.stderr)           # error message if the file the user inputed is not a zip
    sys.exit(1)                                                                             # all error mesages pass to the stderr channel if it fails

