"""
RECORD CHECK  -  my version
===========================

Name  :  Arham Farid
Lane  : IT    
Date  : 2 October 2026
"""

over_limit_count = 0
while True:
    hostname = input("enter a hostname: ") 
    if hostname == "quit":
        break     
    gb_used = float(input("enter the gb used: "))
    gb_total = float(input("enter the total gb: "))

    difference = gb_total - gb_used  
    percent = (gb_used / gb_total) *100    
    if percent >= 100:
        status = "over limit"
        over_limit_count += 1
    elif percent >= 90:
        status = "warning"
    else:
        status = "ok"
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  Used        : {gb_used:10.2f}")
    print(f"  Total       : {gb_total:10.2f}")
    print(f"  Free        : {difference:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
print(f"total records over limit: {over_limit_count}")

