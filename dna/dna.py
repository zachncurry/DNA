import csv
import re
import string
import sys
import pandas
import numpy
from sys import argv
from csv import reader, DictReader


# REFERENCE: RE.match tutorial: https://www.youtube.com/watch?v=Dkiz0z3bMg0
# REFERENCE: Loop over data frame https://www.youtube.com/watch?v=LHE0g1ghfV4
# REFERENCE: Pattern searching: https://pythonforbiologists.com/regular-expressions
# REFERENCE: Iterate over dataframs: https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/


if len(sys.argv) < 3:
    print("python dna.py data.csv sequence.txt")
    exit()

if sys.argv[1] == "databases/large.csv":
    # FORMULA FOR LARGE CSV
    with open(sys.argv[1]) as find_suspect:
        people = pandas.read_csv(sys.argv[1])
        people["A"] = "AGATC"
        people["B"] = people['AGATC'] * people["A"]
        people["C"] = "TTTTTTCT"
        people["D"] = people['TTTTTTCT'] * people["C"]
        people["E"] = "AATG"
        people["F"] = people['AATG'] * people["E"]
        people["G"] = "TCTAG"
        people["H"] = people['TCTAG'] * people["G"]
        people["I"] = "GATA"
        people["J"] = people['GATA'] * people["I"]
        people["K"] = "TATC"
        people["L"] = people['TATC'] * people["K"]
        people["M"] = "GAAA"
        people["N"] = people['GAAA'] * people["M"]
        people["O"] = "TCTG"
        people["P"] = people['TCTG'] * people["O"]

    with open(sys.argv[2]) as dna_strand:
        dna_main = open(sys.argv[2], "r")
        dna_read = dna_main.read()

    for i in range(len(people)):
        AGATC_count = dna_read.count(people.loc[i, "B"])
        TTTTTTCT_count = dna_read.count(people.loc[i, "D"])
        AATG_count = dna_read.count(people.loc[i, "F"])
        TCTAG_count = dna_read.count(people.loc[i, "H"])
        GATA_count = dna_read.count(people.loc[i, "J"])
        TATC_count = dna_read.count(people.loc[i, "L"])
        GAAA_count = dna_read.count(people.loc[i, "N"])
        TCTG_count = dna_read.count(people.loc[i, "P"])
        if (AGATC_count == 1) and (TTTTTTCT_count == 1) and (AATG_count == 1) and (AATG_count == 1) and (TCTAG_count == 1) and (TATC_count == 1) and (GAAA_count == 1) and (TCTG_count == 1):
            print(people.loc[i, "name"])
            break
        
    for i in range(len(people)):
        AGATC_count = dna_read.count(people.loc[i, "B"])
        TTTTTTCT_count = dna_read.count(people.loc[i, "D"])
        AATG_count = dna_read.count(people.loc[i, "F"])
        TCTAG_count = dna_read.count(people.loc[i, "H"])
        GATA_count = dna_read.count(people.loc[i, "J"])
        TATC_count = dna_read.count(people.loc[i, "L"])
        GAAA_count = dna_read.count(people.loc[i, "N"])
        TCTG_count = dna_read.count(people.loc[i, "P"])
        if (AGATC_count != 1) or (TTTTTTCT_count != 1) or (AATG_count != 1) or (AATG_count != 1) or (TCTAG_count != 1) or (TATC_count != 1) or (GAAA_count != 1) or (TCTG_count != 1):
            print("Not Found")
            break
        
else:
    # FORMULA FOR SMALL CSV
    with open(sys.argv[1]) as find_suspect:
        people = pandas.read_csv(sys.argv[1])
        people["A"] = "AGATC"
        people["B"] = people['AGATC'] * people["A"]
        people["C"] = "AATG"
        people["D"] = people['AATG'] * people["C"]
        people["E"] = "TATC"
        people["F"] = people['TATC'] * people["E"]

    with open(sys.argv[2]) as dna_strand:
        dna_main = open(sys.argv[2], "r")
        dna_read = dna_main.read()
    
    for i in range(len(people)):
        AGATC_count = dna_read.count(people.loc[i, "B"])
        AATG_count = dna_read.count(people.loc[i, "D"])
        TATC_count = dna_read.count(people.loc[i, "F"])
        if (AGATC_count == 1) and (AATG_count == 1) and (TATC_count == 1):
            print(people.loc[i, "name"])
            break
        
    for i in range(len(people)):
        AGATC_count = dna_read.count(people.loc[i, "B"])
        AATG_count = dna_read.count(people.loc[i, "D"])
        TATC_count = dna_read.count(people.loc[i, "F"])
        if (AGATC_count != 1) or (AATG_count != 1) or (TATC_count != 1):
            print("Not Found")
            break


