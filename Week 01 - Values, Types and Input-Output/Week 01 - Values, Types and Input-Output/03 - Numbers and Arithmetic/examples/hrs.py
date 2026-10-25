total_seconds = 9137
hrs = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60
print(total_seconds, "seconds =", hrs, "hours,", minutes, "minutes,", seconds,"seconds")