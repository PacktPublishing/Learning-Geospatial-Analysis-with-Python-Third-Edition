"""fmtDecode.py - Simple program to manually decode binary formats."""

import struct
import collections
import pickle
import os
import sys

def export():
    print("Saving results")
    out = None
    if cached:
        out = open(oname, "a")
    else:
        out = open(oname, "w")
        out.write(header)
    for record in fileDesc:
        for field in record:
            out.write("{}".format(field))
        out.write("\n")
    out.close()
    pickle.dump(cached, open(pickleJar, "wb"))
    sys.exit()

header = "POSTION\tFIELD\tSAMPLE\tTYPE\tBYTE_ORDER\n"
fileDesc = []
files = os.listdir(".")
count = 1
print("Available Files: ")

for f in files:
    print(" {}. {}".format(count, f))
    count += 1

fnum = input("Enter the number of the file to decode: ")
if not fnum:
    sys.exit()
fname = files[int(fnum)-1]
base = os.path.splitext(fname)[0]
print(base)

pickleJar = "{}.p".format(base)

cached = []

if os.path.exists(pickleJar):
    print("Cached session available.")
    print()
    useCache = input("Use it? Yes (Y), No (N)?")
    if "y" in useCache.lower() or useCache == "":
        cached = pickle.load(open(pickleJar, "rb"))
    else:
        cached = []

oname = "{}_decode.txt".format(base)

f = open(fname, "rb")
loc = f.tell()
f.seek(0, 2)
eof = f.tell()
f.seek(0)
prev = 0

if len(cached) > 0:
    print("Using cache...")
    f.seek(cached[-1])
    prev = cached[-2]

print(("Starting at byte {}...".format(f.tell())))

try:
    formatDict = {"char": {"format": "c", "len": 1},
                  "signed char": {"format": "b", "len": 1},
                  "unsigned char": {"format": "B", "len": 1},
                  "_Bool": {"format": "?", "len": 1},
                  "short": {"format": "h", "len": 2},
                  "unsigned short": {"format": "h", "len": 2},
                  "int": {"format": "i", "len": 4},
                  "unsigned int": {"format": "I", "len": 4},
                  "long": {"format": "l", "len": 4},
                  "unsigned long": {"format": "L", "len": 4},
                  "long long": {"format": "q", "len": 8},
                  "unsigned long long": {"format": "Q", "len": 8},
                  "float": {"format": "f", "len": 4},
                  "double": {"format": "d", "len": 8}}

    formats = collections.OrderedDict(sorted(formatDict.items(),
                                             key=lambda t: t[0]))

    while f.tell() < eof:
        record = []
        start = f.tell()
        record.append("{}\t".format(start))
        cached.append(start)
        fields = []
        print()
        count = 1
        try:
            # Little endian formats
            for fmt in formats:
                form = formats[fmt]["format"]
                bytes = formats[fmt]["len"]
                field = struct.unpack("<{}".format(form), f.read(bytes))
                print("{}. Little {}: {}".format(count, fmt, field))
                count += 1
                f.seek(start)
                fields.append([str(field[0]), fmt, "little", str(bytes)])
        except:
            pass

        try:
            # Big endian formats
            for fmt in formats:
                form = formats[fmt]["format"]
                bytes = formats[fmt]["len"]
                field = struct.unpack(">{}".format(form), f.read(bytes))
                print("{}. Big {}: {}".format(count, fmt, field))
                count += 1
                f.seek(start)
                fields.append([str(field[0]), fmt, "big", str(bytes)])
        except:
            pass

        print("{}. Go back to previous".format(count))
        count += 1
        print("{}. Save and Exit".format(count))
        print()
        print("Current location: {}".format(f.tell()))
        opt = input("Enter the number of one of the above options: ")
        if not opt:
            opt = "30"
        choice = int(opt.strip())
        desc = ""
        if choice <= count-2:
            desc = input("Enter a field description: ")
            record.append("{}\t".format(desc))
            record.append("{}\t".format(fields[choice-1][0]))
            record.append("{}\t".format(fields[choice-1][1]))
            record.append("{}\t".format(fields[choice-1][2]))
            f.seek(start + int(fields[choice-1][3]))
            prev = start
            fileDesc.append(record)
        elif choice == count-1:
            f.seek(prev)
            print("Going back to previous field.")
        elif choice == count:
            break
    f.close()
    export()
except KeyboardInterrupt:
    print()
    reverse = input("How many records back? ")
    if not reverse:
        reverse = "0"
    reverse = int(reverse)
    for i in range(reverse):
        cached.pop()
    pickle.dump(cached, open(pickleJar, "wb"))
    print("The program will exit.  Restart and use cached version.")
except:
    raise
