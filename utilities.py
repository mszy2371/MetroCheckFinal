import calendar

door_codes = {'All temporary toilets': 'C3470X',
              'Barnet Church toilet': 'C1986Y',
              'North Finchley bus station': '2531',
              'Muswell Hill toilet': '(2+5),3,4,1',
              'Archway toilet': '4957',
              'Winchmore Hill toilet': '7904',
              'Southgate toilet': '2,(4+1),(3+5)',
              'Turnpike Lane toilet': '(1+2),(4+5),3',
              'Turnpike Lane canteen': '2,3,5',
              'Edmonton Green bus station': '4,(3+1),2',
              'Walthamstow bus station': '(3+5),2,(1+4)',
              'Millbrook Park toilet': '(2+4),3'
              }

months_list = []
for month in calendar.month_name[1:]:
    months_list.append(month)

years_list = []
for year in range(2020, 2030):
    years_list.append(year)
