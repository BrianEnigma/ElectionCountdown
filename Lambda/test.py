#!/usr/bin/env python3

import date_countdown

if __name__ == '__main__':
    countdown = date_countdown.DateCountdown(debug=True)
    countdown.get_delta()

    print("\n")
    countdown = date_countdown.DateCountdown(target_year=2020, target_month=9, target_day=6, target_label='Election', debug=True)
    countdown.get_delta()

    print("\n")
    countdown = date_countdown.DateCountdown(target_year=2020, target_month=9, target_day=5, target_label='Electoral College', debug=True)
    countdown.get_delta()

    print("\n")
    countdown = date_countdown.DateCountdown(target_year=2020, target_month=9, target_day=4, target_label='Electoral Certification', debug=True)
    countdown.get_delta()

    print("\n")
    countdown = date_countdown.DateCountdown(target_year=2020, target_month=9, target_day=7, target_label='Inauguration', debug=True)
    countdown.get_delta(brief=True)
