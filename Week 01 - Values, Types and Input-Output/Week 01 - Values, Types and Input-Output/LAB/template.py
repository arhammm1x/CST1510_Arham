"""
RECORD CHECK  -  my version
===========================

Name  :  Arham Farid
Lane  :  IT   
Date  :  26 September 2026

"""
hostname = input("Enter a hostname: ")     
gb_used = float(input("Enter GB used: "))     
total_gb = float(input("Enter the total GB: "))    
difference = total_gb - gb_used  
percentage = (gb_used / total_gb) *100
mb_used = gb_used *1024        #cobnverts disk usage into MB, (one extra calculated line)
print("=" * 34)
print(f"  Record Check  -  {hostname}")
print("=" * 34)
print(f"  {'GB used':<14}: {gb_used:>10.2f}")
print(f"  {'Total GB used':<14}: {total_gb:>10.2f}")
print(f"  {'Difference':<14}: {difference:>+10.2f}")
print(f"  {'Percentage':<14}: {percentage:>10.2f}%")
print(f"  {'MB Used':<14}: {mb_used:>10.2f}")
print("=" * 34)
