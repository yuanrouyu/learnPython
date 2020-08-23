#!/usr/bin/env python3

# -*- coding: utf-8 -*-



# from datetime import datetime
# now=datetime.now()
# print(now)

# dt=datetime(2015,4,19,12,20)
# print(dt)
# a=dt.timestamp()
# print(a)
# # timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

# cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
# print(cday)


# from datetime import datetime ,timedelta
# now=datetime.now()
# now2=now+timedelta(hours=10)
# print(now2)
# now-timedelta(days=1)
# datetime.datetime(2015,5,17,16,57,3,540997)


# from datetime import datetime, timedelta, timezone

# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))

# tzutc8=timezone(timedelta(hours=8))
# now=datetime.now()
# print(now)
# dt=now.replace(tzinfo=tzutc8)
# print(dt)


# utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

# utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))

# def to_timestamp(dt_str, tz_str):
#     dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#     g =int(re.match(r'^UTC([+-]\d+):\d+$', tz_str).group(1)) 
#     nt=dt-timedelta(hours=g)
#     return nt.timestamp()

import re
m=re.match(r'^UTC([+-]\d+):\d+$', 'UTC+5:00')
a=m.group(2)

print(a)