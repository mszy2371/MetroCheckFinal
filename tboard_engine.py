""" The purpose of the program is to create a personalised rota for Metroline Potters Bar night shift drivers
and lets them check their colleagues rotas or specified dates to find a person who is off duty and would be able
 to swap on the desire date"""

import timeboard as tb
from rotalines import *
from datetime import datetime, date
import calendar


class Driver:

    def __init__(self, first, last, rota_line, hol_block=None):
        self.first = first
        self.last = last
        self.rota_line = rota_line
        self.hol_block = hol_block

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Tboard(Driver):
    today = date.today()
    week_start = tb.Marker(each='W', at=[{'days': 5}])
    lines_personal = [0, ]
    for i in range(len(lines)):
        lines_personal.append(lines[i:] + lines[:i])

    def __init__(self, first, last, rota_line, hol_block=None):
        super().__init__(first, last, rota_line, hol_block)
        self.rota = tb.Organizer(marker=self.week_start, structure=self.lines_personal[self.rota_line])
        self.rota_order = tb.Organizer(marks='16 May 2020', structure=[self.rota])
        self.clnd = tb.Timeboard(base_unit_freq='D', start='11 January 2020',
                                 end='10 July 2030', layout=self.rota_order)
        self.schedule = self.clnd.add_schedule(self.last, selector=lambda label: label != 0)

    def add_one_month(self, orig_date=None):
        new_year = orig_date.year
        new_month = orig_date.month + 1
        if new_month > 12:
            new_year += 1
            new_month -= 12
        last_day_of_month = calendar.monthrange(new_year, new_month)[1]
        new_day = min(orig_date.day, last_day_of_month)
        return orig_date.replace(year=new_year, month=new_month, day=new_day)

    def sub_one_month(self, orig_date=None):
        new_year = orig_date.year
        new_month = orig_date.month - 1
        if new_month < 1:
            new_year -= 1
            new_month += 12
        last_day_of_month = calendar.monthrange(new_year, new_month)[1]
        new_day = min(orig_date.day, last_day_of_month)
        return orig_date.replace(year=new_year, month=new_month, day=new_day)

    def ivl(self, date):
        ivl_list = []
        for item in (self.clnd(date, period='M')):
            ivl_list.append(item.start_time.date()),
            ivl_list.append(item.start_time.strftime('%A'))
            ivl_list.append(item.label)
        return ivl_list


# creating personalized rotas associate to drivers' names


dvr_line1 = Tboard('Theo', 'Fernandes', 1, 'C4')
dvr_line2 = Tboard('Abdesslam', 'Ketami', 2, 'G3')
dvr_line3 = Tboard('Deniz', 'Yesildal', 3, 'C3')
dvr_line4 = Tboard('Marcin', 'Szymanek', 4, 'G1')
dvr_line5 = Tboard('Courage', 'Mabani', 5, 'F3')
dvr_line6 = Tboard('Saden', 'Chelemben', 6, 'H2')
dvr_line7 = Tboard('Rexhep', 'Dibra', 7)
dvr_line8 = Tboard('Naim', 'Neza', 8)
dvr_line9 = Tboard('Costas', 'Constantinou', 9, 'C2')
dvr_line10 = Tboard('Mark', 'Lunam', 10, 'F1')
dvr_line11 = Tboard('Hisham', 'Dowidar', 11)
dvr_line12 = Tboard('Ozzie', 'Hassan', 12, 'D3')
dvr_line13 = Tboard('Ray', 'Darabi', 13)
dvr_line14 = Tboard('Mario', 'Stavrinou', 14)
dvr_line15 = Tboard('Rashid', 'Abed', 15, 'F2')
dvr_line16 = Tboard('Raza', 'Shazad', 16, 'B4')
dvr_line17 = Tboard('Mamad', 'Bodhee', 17, 'G2')
dvr_line18 = Tboard('Suresh', 'Bhagat', 18, 'F1')

drivers = [dvr_line1, dvr_line2, dvr_line3, dvr_line4, dvr_line5, dvr_line6,
           dvr_line7, dvr_line8, dvr_line9, dvr_line10, dvr_line11, dvr_line12,
           dvr_line13, dvr_line14, dvr_line15, dvr_line16, dvr_line17, dvr_line18]


