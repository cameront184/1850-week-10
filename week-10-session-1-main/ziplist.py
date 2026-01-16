# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# use zipfile methods to list the contents of the zip file
# test your script on the test.zip file

import sys
import zipfile
from zipfile import ZipFile   # methods in this module can be used

if len(sys.argv) < 2:
    print("No filename given", file=sys.stderr)            # Gives an error message if user doesnt input a file
    sys.exit(1)

archive_filename = sys.argv[1]

if not zipfile.is_zipfile(archive_filename):                                 # error message if the file the user inputed is not a zip
    print("file is not a zip file", file=sys.stderr)                         # all error mesages pass to the stderr channel if it fails

try:
    with ZipFile(archive_filename, "r") as infile:         # Used a zipfile.namelist to list the contents in the zip
        for name in infile.namelist():
            print(name)
except:
    print("Filename given but file does not exist", file=sys.stderr)         # error message for if the file that the user has inputed doesnt exist


