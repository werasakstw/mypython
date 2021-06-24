'''
The Universal Time Coordinated (UTC) is based on Gregorian calendar.
The epoch is the UTC 00.00 h which is Jan 1, 1970 at 0° longitude.

ISO8601 suggested a day-time format:
       		YYYY-MM-DD:hh:mm:ss
  'M' is for month and 'm' is for minute.
Most operating systems do not allow file name with colon ':'.
So they use:	YYYY-MM-DD-hh-mm-ss
'''

# String Split.
# <str>.split(<separator>) returns a list of strings in the <str>.
s = '2020-12-31-00-01-02'
##print(s.split('-'))     # ['2020', '12', '31', '00', '01', '02']

# String Time Parser.
from time import strptime
st = strptime(s, '%Y-%m-%d-%H-%M-%S')  # time.struct_time
##print(st)

# Struct Time. 
##print(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour,   ## 2020 12 31 0
##      st.tm_min, st.tm_sec, st.tm_wday, st.tm_yday)    ## 1 2 3 366
    
import time
def time_test():
    print(time.time()) #  the total time elapsed since epoch
          # a float in seconds with 1 μs precision.
##time_test()
 
# Structure Time
# struct_time representing: year, month, day, hours, minutes, and seconds
def struct_test():  
    print(time.gmtime())    ## returns a struct_time of the current UTC
    print(time.localtime()) ## returns a struct_time of local time.
    print(time.ctime())     ## return a compact format string of the current UTC
    print(time.asctime())   ## return a compact format string of local time.
# struct_test()

from time import localtime
def local_time():
    print(localtime())
    print(localtime()[:6])  ## sliceing only the first six elements.
    print('%4d-%2d-%2d' % localtime()[:3])
    print('%4d-%02d-%02d' % localtime()[:3])
    print('%02d-%2d-%2d' % localtime()[3:6])
##local_time()

# Accessing Time Components.
def time_comp():
    t = time.localtime()
    
        ## Slicing
    print(t[:3])    ## year, month, day
    print(t[3:6])   ## hours, minutes,seconds
    print(t[6:9])   ## wday, yday, isdst
    ## wday is the number of the day in the week (starting with 0 = Mon).
    ## yday is the number of the day in the year.
    ## isdst indices whether the daylight change is implemented.

        ## Keys
    print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, t.tm_wday, t.tm_yday)
# time_comp()

''' Time Formater:
time.strftime(format_str, struct_time) returns a ‘compact format’ of time.
    %a (abbreviated weekday name)  %A (full weekday name)    %w (weekday number)
    %b (abbreviated name of month) %B (full name of month)   %m (month number)
    %d (day of month)              %y (year without century) %Y (four digit year)
    %H (hour)   %M (minutes)       %S  (seconds)             %p (AM/PM)
    %c (appropriate date and time) %x (appropriate date)     %X (appropriate time)
'''
def fmt_test():
    t = time.localtime()
    print(time.strftime("%a,%d %b %Y %H:%M:%S", t))
    print(time.strftime("%c", t))
# fmt_test()

'''
time.perf_counter() returns the highest precision possible system clock in nano seconds.
time.process_time() returns the clocks the processor spends on the specific process.
'''
def clock_test():
    print(time.perf_counter())  ##  signifies a system wide time
    print(time.process_time())  ##  signifies the time for the specific process
##clock_test()

def profile_test():
    start = time.perf_counter()
    x = 123 ** 123  ## compute something
    stop = time.perf_counter()
    print('%.10f ns' % ((stop-start)*(10**9)))
##profile_test()

## datetime Module:
import datetime  ## contains classes date, time, datetime, and timedelta.
def date_test():
    d = datetime.date.today()   ## datetime.date(YYYY, MM, DD)
    print(d)
    print(d.year, d.month, d.day, d.weekday())

    ## Gregorian ordinal (Jan 1, 1 is day 1)
    print(d.toordinal())  

    ## Date constants
    print(datetime.date.min, datetime.date.max)
# date_test()

def time_test():
    t = datetime.time(1, 2, 3, 4)  ## hh, mm, ss, microsecond
    print(t)
    print(t.hour, t.minute, t.second, t.microsecond)

    ## Date constants
    print(datetime.time.min, datetime.time.max)
# time_test()

def datetime_test():
    print(datetime.datetime.now())
    print(datetime.datetime.utcnow())
    print(datetime.datetime.today())
    
    ## DateTime constants
    print(datetime.datetime.min, datetime.datetime.max)
# datetime_test()


## Calendar:
import calendar
def calendar_test():
    c = calendar.TextCalendar() ## firstweekday = 1
    # c = calendar.TextCalendar(firstweekday = 6)
    c.prmonth(2017, 6)
    # c.prmonth(2017, 6, w = 4)     ## column width

    ## A year calendar
    # c.pryear(2017)
    # c.pryear(2017, m = 2)         ## month column
    
    ## Calendar may be saved as string. 
    m = c.formatmonth(2017, 6)
    # print(m)
    y = c.formatyear(2017)
    # print(y)
# calendar_test()

#------------------------------------------------------------------------

# File Name Factory:
# Embedding the date and time to file names is a good practice.
def get_file_name(title, ext):
    ts = '%4d-%02d-%02d-%02d-%02d-%02d' % localtime()[:6]
    return '%s-%s.%s' % (title, ts, ext)
##print(get_file_name('MyLog', 'log'))  ## MyLog-2021-05-14-12-16-55.log

# Flie Time Stamp:
# All files have time stamps.
import os
# time.ctime() converts date and time values into printable format.
##print(time.ctime(os.path.getatime(__file__)))   # access time
##print(time.ctime(os.path.getmtime(__file__)))   # modificationtime
##print(time.ctime(os.path.getctime(__file__)))   # creation time




