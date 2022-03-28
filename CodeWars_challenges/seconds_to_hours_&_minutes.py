seconds = 323500
hours = seconds/60/60
hours2 = int(hours)
new_sec = seconds - hours2*60*60
minutes = new_sec/60
minutes = int(minutes)
print(str(hours2) + " hour(s) and " + str(minutes) + " minute(s)")