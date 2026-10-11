"""
RECORD CHECK  -  my version
===========================

Name  :Arham Farid
Lane  :IT     
Date  :11 october 2026
"""

def status_of(percent):
    """returns the status for the percent"""
    if percent >= 100:
        return "over limit"
    elif percent >= 90:
        return "warning"
    else:
        return "ok"
def check(value, limit):
    """returns the amount of gb used and the difference"""
    difference = limit - value 
    percent = (value / limit) * 100
    return difference, percent
def print_report(label, value, limit, difference, percent, status):
    """prints the entire report"""
    print()
    print("=" * 34)
    print(f"  Record check  -  {label}")
    print("="* 34)
    print(f"  {'used':<10}  :     {value:>10.2f}")
    print(f"  {'total':<10}  :    {limit:>10.2f}")
    print(f"  {'free':<10}  :     {difference:>10.2f}")
    print(f"  {'percent':<10}  :  {percent:>10.2f}")
    print(f"  {'status':<10}  : {status:>10}")
over_count = 0 
while True:
    label = input("enter the hostname: ")
    if label == "quit":
        break
    value = float(input("enter the gb used: "))
    limit = float(input("enter the total gb: "))
    difference, percent = check(value,limit)
    status = status_of(percent)
    if status == "Over Limit":
        over_count += 1
    print_report(label, value, limit, difference, percent, status)
print(f"total records over limit: {over_count}")    