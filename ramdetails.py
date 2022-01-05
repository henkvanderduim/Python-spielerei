import os
import psutil

# getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()

cpu_usage = (load15 / os.cpu_count()) * 100

print("Het CPU gebruik is: ", cpu_usage)
