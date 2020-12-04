NAMES = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
    "byr",
    "cid",
    "ecl",
    "eyr",
    "hcl",
    "hgt",
    "iyr",
    "pid",
]

def tricode(x):
    return ord(x[0]) << 16 | ord(x[1]) << 8 | ord(x[2])

print("class Tricode {")
for n in NAMES:
    print("  {}(): U64 & imm {{ {} }}".format(n, tricode(n)))
print("}")
