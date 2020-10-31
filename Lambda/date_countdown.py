#!/usr/bin/env python3

import datetime
from pprint import pprint
import pytz
import settings


class DateCountdown:
    def __init__(self,
                 target_year=settings.Settings['target_year'],
                 target_month=settings.Settings['target_month'],
                 target_day=settings.Settings['target_day'],
                 target_label=settings.Settings['target_label'],
                 target_label_short=settings.Settings['target_label_short'],
                 debug=False):
        self._debug = debug
        self._my_timezone = pytz.timezone('US/Pacific')
        self._target = datetime.datetime(year=target_year, month=target_month, day=target_day, hour=0, minute=0, second=0, microsecond=0, tzinfo=self._my_timezone)
        self._label = target_label
        self._label_short = target_label_short
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
            result['label'] = self._label
        else:
            result['label'] = self._label_short
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
