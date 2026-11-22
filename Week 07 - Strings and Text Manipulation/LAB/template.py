
"""
RECORD CHECK - IT lane
======================

Name: Arham Farid
Lane: IT
Date: 15 November 2026

Tier: Threshold
Run it: python template.py
"""



def parse_line(raw_line):
    """Clean and parse one messy IT server record into a dictionary."""

    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}

    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = float(value.strip())

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"]
    }



raw_records = [
    "  SRV-01 , used=87 , total=100  ",
    "srv-02,USED=65,TOTAL=100",
    "  Srv-03, used=45, total=100 ",
    "SRV-04 , USED=95 , TOTAL=100 ",
    "  srv-05, used=72 , TOTAL=100  "
]



for raw_record in raw_records:
    record = parse_line(raw_record)
    print(record)
