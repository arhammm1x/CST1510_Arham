"""
RECORD CHECK  -  my version
===========================

Name  : Arham Farid
Lane  : IT
Date  : 24 October 2026

Run it:   python template.py

"""



class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label #stores the passed in attributes directly to self
        self.value = value
        self.limit = limit

        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1 #calls self status, if the records exceeds it inrements by 1
    def status(self):
        """returns the status"""
        percent = self.value/self.limit *100 #calculate the percentage of limit consumed
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
    




def load_records(path): #defines a function that accepts a file 
    record_list = [] #to store the created obecjts to records
    with open(path) as f:
        for line in f:
            line = line.strip() #removes white spcaes
            if line:
                label, value, limit = line.split(",") 
                record_list.append(Record(label, float(value), float(limit)))
    return record_list # returns completed list of records obj back to the called ()

filename = "server_sample.txt" #created a sample file with data
with open(filename, "w") as f:
    f.write("SRV-01, 85.0, 100\n")
    f.write("SRV-02, 101.0, 100\n")
    f.write("SRV-03, 95.0, 100\n")

records = load_records(filename) #Calls load_records() passing the file path


for record in records: #iterates through records
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value         : {record.value}")
    print(f"  Limit         : {record.limit}")
    print(f"  Status         : {record.status()}")
    print("=" * 34)


print(f"total rec over the limit: {Record.over_limit_count}")