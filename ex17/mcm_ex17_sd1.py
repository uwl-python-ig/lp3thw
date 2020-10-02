from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")

in_file = open(from_file)
indata = in_file.read()

print(f"Input file is {len(indata)} bytes long.")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
