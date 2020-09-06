#!/usr/bin/env python3

import datetime
from pprint import pprint
import pytz

TARGET_YEAR = 2020
TARGET_MONTH = 11
TARGET_DAY = 3


class DateCountdown:
    def __init__(self, target_year=TARGET_YEAR, target_month=TARGET_MONTH, target_day=TARGET_DAY, debug=False):
        self._debug = debug
        self._my_timezone = pytz.timezone('US/Pacific')
        self._target = datetime.datetime(year=target_year, month=target_month, day=target_day, hour=0, minute=0, second=0, microsecond=0, tzinfo=self._my_timezone)
        if self._debug:
            pprint(self._my_timezone)
            pprint(self._target)

    def get_delta(self, brief=False):
        result = {}
        local_now = datetime.datetime.now(tz=self._my_timezone)
        normalized_local_now = datetime.datetime(year=local_now.year, month=local_now.month, day=local_now.day, hour=0, minute=0, second=0, microsecond=0, tzinfo=self._my_timezone)
        delta = self._target - normalized_local_now
        if not brief:
            result['target'] = self._target.strftime('%Y-%m-%d')
            result['now'] = normalized_local_now.strftime('%Y-%m-%d')
            result['tzinfo'] = str(self._my_timezone)
        result['days'] = delta.days
        result['weeks'] = int(result['days'] * 10 / 7) / 10 # Weeks, to one decimal place
        if result['days'] < 0:
            result['days'] = -1
            result['weeks'] = 0.0
        if self._debug:
            pprint(local_now)
            pprint(normalized_local_now)
            pprint(delta)
            pprint(result)
        return result
