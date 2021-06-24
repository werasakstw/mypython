
# ISO 8601 suggested a day-time format:
#       		YYYY-MM-DD:hh:mm:ss
#       'M' is for month and 'm' is for minute.

# Most operating systems do not allow file name with colon ':'.
# So they use:	YYYY-MM-DD-hh-mm-ss

# <str>.split(<separator>) returns a list of strings in the <str>.
s = '2020-12-31-00-01-02'
print(s.split('-'))     # ['2020', '12', '31', '00', '01', '02']

# String Parser:
# time.strptime(<str>, <pattern>) returns a time.struct_time.
from time import strptime
st = strptime(s, '%Y-%m-%d-%H-%M-%S') 
print(st)## time.struct_time(tm_year=2020, tm_mon=12, tm_mday=31,
         ## tm_hour=0, tm_min=1, tm_sec=2, tm_wday=3, tm_yday=366, tm_isdst=-1)

# Time Struct
print(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour,   ## 2020 12 31 0
      st.tm_min, st.tm_sec, st.tm_wday, st.tm_yday)    ## 1 2 3 366

# Local Time
from time import localtime
## Get a time struct of localtime.
print(localtime()) ## time.struct_time(tm_year=2021, tm_mon=5, tm_mday=14,
     ## tm_hour=12, tm_min=8, tm_sec=20, tm_wday=4, tm_yday=134, tm_isdst=0)

## Slice the first six elements.
print(localtime()[:6]) ## (2021, 5, 14, 12, 8, 20)

# Date:
print('%4d-%02d-%02d' % localtime()[:3])    # 2021-05-14
# Time:
print('%02d-%02d-%02d' % localtime()[3:6])  # 12-14-16

#------------------------------------------------------------------------

# File Name Factory:
# Embedding the date and time to file names is a good practice.
def get_file_name(title, ext):
    ts = '%4d-%02d-%02d-%02d-%02d-%02d' % localtime()[:6]
    return '%s-%s.%s' % (title, ts, ext)
print(get_file_name('MyLog', 'log'))  ## MyLog-2021-05-14-12-16-55.log

# Flie Time Stamp:
# All files have time stamps.
import time, os
# time.ctime() converts date and time values into printable format.
print(time.ctime(os.path.getatime(__file__)))   # access time
print(time.ctime(os.path.getmtime(__file__)))   # modificationtime
print(time.ctime(os.path.getctime(__file__)))   # creation time

