from flask import Flask, render_template, url_for, request
from tboard_engine import *
from rotalines import *
from utilities import door_codes
from datetime import date
import os
from dotenv import load_dotenv
import sqlite3


load_dotenv()


app = Flask(__name__)
app.static_folder = 'static'

conn = sqlite3.connect(os.getenv('DB_NAME'), check_same_thread=False)

c = conn.cursor()


def display_duties(table):
    c.execute(f'SELECT * FROM {table}')

    return c.fetchall()


@app.route("/")
@app.route("/home")
@app.route("/index", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/checker", methods=['get', 'post'])
def checker():
    checkerdate = request.args.get("checkerdate")
    if checkerdate is None or checkerdate == '':
        checkerdate = datetime.today().strftime('%Y-%m-%d')

    weekday = datetime.strptime(checkerdate, '%Y-%m-%d').strftime('%A')

    return render_template('checker.html', title='Checker', drivers=drivers, checkerdate=checkerdate,
                           duty_routes=duty_routes, mon_thu_times=mon_thu_times, fri_times=fri_times,
                           sat_times=sat_times, sun_times=sun_times, weekday=weekday)


@app.route('/duties')
def duties():
    global number
    mon_thu = display_duties('mon_thu_duties')
    friday = display_duties('friday_duties')
    saturday = display_duties('saturday_duties')
    sunday = display_duties('sunday_duties')
    return render_template('duties.html', mon_thu=mon_thu, friday=friday, saturday=saturday, sunday=sunday)


@app.route("/doorcodes")
def doorcodes():
    return render_template('doorcodes.html', title='DoorCodes', door_codes=door_codes)


@app.route("/individual/", methods=['GET', 'POST'])
def individual():
    return render_template('individual.html', title='Individual', drivers=drivers, rotamonth=date.today())



@app.route("/individual/printrota/<rotamonth>", methods=['GET', 'POST'])
def printrota(rotamonth):
    today = date.today()
    pickname = request.args.get('pickname')
    date_to_pass = datetime.strptime(rotamonth, '%Y-%m-%d').date()
    dispmonth = date_to_pass.strftime('%B %Y')

    for driver in drivers:
        if driver.first == pickname:
            chosen_driver = driver
            backward = chosen_driver.sub_one_month(date_to_pass)
            fwd = chosen_driver.add_one_month(date_to_pass)


            return render_template('printrota.html', chosen_driver=chosen_driver, mon_thu_times=mon_thu_times,
                                   fri_times=fri_times, sat_times=sat_times, sun_times=sun_times, dispmonth=dispmonth,
                                   rotamonth=rotamonth, fwd=fwd, backward=backward, pickname=pickname, today=today)


@app.route("/holidays/<year>")
def holidays(year):
    if year not in ('2021', '2022', '2023', '2024'):
        year = '2021'
    year = str(year)
    early = f"e.'{year}'"
    summer = f"s.'{year}'"
    late = f"l.'{year}'"
    c.execute(f'''SELECT d.rota_line, d.first, e.block, {early}, {summer}, {late}
    			 FROM early_winter AS e INNER JOIN summer AS s ON s.block = e.summer_id
    			 INNER JOIN late_winter AS l ON l.block = e.block
                 JOIN drivers AS d ON d.hol_block = e.block
    			 ORDER BY d.rota_line''')

    datas = c.fetchall()
    return render_template("holidays.html", datas=datas, year=year)



if __name__ == "__main__":
    app.run(debug=True)
