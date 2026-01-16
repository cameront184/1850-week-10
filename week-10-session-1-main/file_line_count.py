import sys

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# example: python file_line_count.py testdir/dust_of_snow.txt

if len(sys.arv) < 2:
    print(f"No file supplied: python {sys.argv[0]}", file=sys.stderr)
    sys.exit(1)

file_name = sys.argv[1]

try:
    # Open the file and read its content
    with open(file_name, 'r') as infile:
        lines= infile.readlines()
        
    # Remove empty lines (eg. use loop or list comprehension)
    non_empty_lines = [line for line in lines if line.strip() != ""]

    # Get the number of lines
    number_of_lines = len(non_empty_lines)

    print(f"{file_name} has {number_of_lines} lines.")
except:
    print(f"File not found: python {sys.argv[0]} {file_name}", file=sys.stderr)
    sys.exit(1)

