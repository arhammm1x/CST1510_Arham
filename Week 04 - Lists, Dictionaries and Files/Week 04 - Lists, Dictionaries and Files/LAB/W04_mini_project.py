"""
RECORD CHECK  -  my version
===========================

Name  : Muhammed Jazeel
Lane  : IT     
Date  : 16 October 2026

"""




def check_record(value, limit): # defines a func named chk_rec that accepts value and limit as it parameters
    """returns the amount of gb used and the dfference"""
    difference = limit - value 
    percent = (value / limit) * 100
    if percent >= 100: 
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
        
    return difference, percent, status # returns the calculated valued back to ()


def print_report(label, value, limit, difference, percent, status): # a dedicated func to print the entire report
    """prints the entire report"""
    print()
    print("=" * 34)
    print(f"  Record check  -  {label}")
    print("="* 34)
    print(f"  {'used':<10}    :     {value:>10.2f}")
    print(f"  {'total':<10}   :    {limit:>10.2f}")
    print(f"  {'free':<10}    :     {difference:>10.2f}")
    print(f"  {'percent':<10} :  {percent:>10.2f}")
    print(f"  {'status':<10}  : {status:>10}")




def load_records(path):
    """Read records from a file and return a list of dicts."""
    records_list = [] # creates an empty list store the dicts from the file
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                label, value, limit = line.split(",")
                records_list.append({"label": label.strip(),"value": float(value),"limit": float(limit)})
    return records_list # returns the completed list of record dicts


def save_results(path, evaluated_records): # defines a new function to to be saved
    """Write labels and status to a new file, one per line."""
    with open(path, "w") as f:
        for rec in evaluated_records:
            f.write(f"{rec['label']},{rec['status']}\n")
input_file = "LAB\\records_sample.txt"
try:
    records = load_records(input_file)
except FileNotFoundError:
    print(f"Error: {input_file} not found")
    records = [] # to ensure the loop wont fail

over_limit_count = 0  #to keep track of recs exceeding the limit count
evaluated_records = [] #to colklect results

for rec in records: #strarts a loop over the list records
    diff, pct, status = check_record(rec["value"], rec["limit"])
    print_report(rec["label"], rec["value"], rec["limit"], diff, pct, status)
    
    evaluated_records.append({"label": rec["label"], "status": status}) # add this into the empty list
    
    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"\n{over_limit_count} of {len(records)} were over limit")
save_results("results.txt", evaluated_records) #v save_results to save into results.txt
    


