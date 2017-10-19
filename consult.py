# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
from calendar import monthrange
import fpdf
import random

jmeno = raw_input("Please set Jmeno prijmeny: \n")
zakazaka1, zakazaka2, zakazaka3  = input("Please set Zakazka cislo (separete by comma): \n")
month, year = input("Please set a month number and year (separete by comma): \n")
amount = input("Please set a amount money: \n")
amount_text = raw_input("Please write this number by letter: \n")
who_sign = int(input("Who will sign a document? Head of department = 1; Not him = 2 \n Need to write a number: 1 or 2 \n"))
print("month = ", str(month), "\n year = ", str(year))
days_in_month = monthrange(year, month)[1]
print("Days in month: ", str(days_in_month))
total_hours = input("Please set a total working hours: \n")
try:
    except_days = [x for x in input("Please set a except days (separete by comma): \n")]
except SyntaxError:
    except_days = [1]
    print("You do not set days. Okay :(")
work_days = [i for i in range(1, days_in_month+1) if i not in except_days]
# for day in work_days:
#     ans = datetime.date(year, month, day)
#     if ans.strftime("%A") != 'Saturday' and ans.strftime("%A") != 'Sunday':
#         print(day, ans.strftime("%A"))
### importing content files
with open("action_list.txt") as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
names_month = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# FOR PDF FILES
first = "Univerzita Karlova v Praze"
second = "Prirodovedeska faculta"
third = "Albertov 6, 128 43 Praha 2"
number = "ICO: 00216208; DIC: CZ00216208"
month = names_month[month-1]

pdf = fpdf.FPDF()
pdf.add_page()
pdf.set_font("Arial", size=9)
x_num = 155; y_num = 15
pdf.text(x=x_num, y=y_num, txt=first)
pdf.text(x=x_num, y=y_num+4, txt=second)
pdf.text(x=x_num, y=y_num+8, txt=third)
pdf.text(x=x_num, y=y_num+12, txt=number)
#  TITLE
x_num = 50
y_num = 35
pdf.set_font('Arial', 'B', 14)
pdf.text(x=x_num, y=y_num, txt='VIKAZ PRACE / ODPRACOVANYCH HODIN')
pdf.text(x=x_num+22, y=y_num+6, txt='PRIKAZ K PROPLACENI')
### begin
pdf.set_font("Arial", size=8)
my_border = 0
pdf.cell(80, 30, txt="", border=my_border, ln=2, align="C")
pdf.cell(30, 10, txt="", border=my_border, align="C")
pdf.cell(40, 10, txt='', border=my_border, align='C', ln=1)
pdf.cell(30, 8, txt="Chislo dohody:", border=my_border, align="C")
pdf.cell(8, 8, txt="", border=my_border, align="C")
pdf.cell(30, 8, txt="", border=1, ln=2, align='C')
pdf.cell(30, 2, txt='', border=my_border, ln=1, align='C')
# NEW LINE
pdf.cell(38, 8, txt="Jmeno, prijmeny, titul:", border=my_border, align="C")
pdf.cell(130, 8, txt="        "+jmeno, border=1, align='L', ln=1)
#  NEW LINE
pdf.cell(30, 2, txt='', border=my_border, ln=1, align='C')
pdf.cell(38, 8, txt="      Zakazka cislo:", border=my_border, align="L")
pdf.cell(12, 8, txt=str(zakazaka1), border=1, align='C')
pdf.cell(4, 8, txt="-", border=my_border, align='C')
pdf.cell(10, 8, txt=str(zakazaka2), border=1, align='C')
pdf.cell(4, 8, txt="-", border=my_border, align='C')
pdf.cell(20, 8, txt=str(zakazaka3), border=1, align='C', ln=1)
# NEW LINE
pdf.cell(30, 2, txt='', border=my_border, ln=1, align='C')
pdf.cell(38, 8, txt="      Vse odmeni v Kc:", border=my_border, align="L")
pdf.cell(35, 8, txt=str(amount)+" Kc", border=1, align='C', ln=1)
# NEW LINE
pdf.cell(30, 2, txt='', border=my_border, ln=1, align='C')
pdf.cell(38, 8, txt="      Vse odmeni slovne:", border=my_border, align="L")
pdf.cell(130, 8, txt="        "+amount_text, border=1, align='L', ln=1)
#  END HEADER
# START TABLE
pdf.set_font("Arial", 'B', size=7)
pdf.cell(30, 8, txt='', border=my_border, ln=1, align='C')
pdf.cell(20, 6, txt="Mesic:", border=1, align="C")
pdf.cell(16, 6, txt=month, border=1, align="C")
pdf.cell(150, 6, txt="Rok "+str(year), border=1, align="C", ln=1)
# NEW LINE
pdf.set_font("Arial", size=6)
pdf.cell(20, 4, txt="Den v mesice", border=1, align="C")
pdf.cell(16, 4, txt="Pochet hodin", border=1, align="C")
pdf.cell(150, 4, txt="Popis cinnosti", border=1, align="C", ln=1)
# NEW LINES
for i in range(1,32):
    pdf.cell(20, 4, txt=str(i)+".", border=1, align="C")
    pdf.cell(16, 4, txt="", border=1, align="C")
    pdf.cell(150, 4, txt="", border=1, align="L", ln=1)

calc_total_hours = 0  # STARTS TABLE LIST; ENDS 243
day_chosen = random.sample(work_days, len(work_days)); i = 0
# print (day_chosen)
while calc_total_hours != total_hours:
    x_num = 30; y_num = 115
    action_list = random.sample(content, len(content))
    for day in day_chosen:
        time_work = random.randint(2, 8)
        if (total_hours - calc_total_hours >= 5) and (time_work < 5):
            # print("time work = ", time_work)
            pdf.text(x=x_num+8,    y=y_num+4*day, txt=str(time_work))
            pdf.text(x=x_num+20, y=y_num+4*day, txt=action_list[i])
            calc_total_hours = calc_total_hours + time_work
            # print ('calc_total_hours', calc_total_hours)
            i += 1
            # print('number action', i)
            # print (y_num + 4 * day)
        elif 0 < total_hours - calc_total_hours <= 4:
            time_work = total_hours - calc_total_hours
            # print("time work = ", time_work)
            pdf.text(x=x_num + 8, y=y_num + 4 * day, txt=str(time_work))
            pdf.text(x=x_num + 20, y=y_num + 4 * day, txt=action_list[i])
            calc_total_hours = calc_total_hours + time_work
            # print('calc_total_hours', calc_total_hours)
            i += 1
# Last LINE
pdf.set_font("Arial", 'B', size=6)
pdf.cell(20, 4, txt="Celkem hodin", border=1, align="C")
pdf.cell(16, 4, txt=str(total_hours), border=1, align="C")
pdf.cell(150, 4, txt="", border=1, align="C", ln=1)
# ELLIPSE & TEXT
if who_sign == 2:
    pdf.set_font("Arial", size=7)
    pdf.ellipse(x=15, y=252, w=2.5, h=2.5)
    pdf.text(x=19, y=254, txt="vidouchi pracovitse")
    pdf.ellipse(x=45, y=252, w=2.5, h=2.5)
    pdf.ellipse(x=45.4, y=252.4, w=1.7, h=1.7, style="F")
    pdf.set_font("Arial", 'B', size=7)
    pdf.text(x=50, y=254, txt="rasitel grantu")
else:
    pdf.set_font("Arial", "B", size=7)
    pdf.ellipse(x=15.4, y=252.4, w=1.7, h=1.7, style="F")
    pdf.ellipse(x=15, y=252, w=2.5, h=2.5)
    pdf.text(x=19, y=254, txt="vidouchi pracovitse")
    pdf.ellipse(x=45, y=252, w=2.5, h=2.5)
    pdf.set_font("Arial", size=7)
    pdf.text(x=50, y=254, txt="rasitel grantu")
# date and sign
pdf.set_font("Arial", size=7)
pdf.text(x=141, y=254, txt="............................................................................")
pdf.text(x=150, y=258, txt="datum a podpis zamestranice")

# date and sign pracovnika
pdf.text(x=141, y=272, txt="............................................................................")
pdf.text(x=146, y=276, txt="datum a podpis odpovedhe pracovnika")
pdf.text(x=153, y=279, txt="zamesranickeho oddeleni")

# Date jmeno podpis
pdf.text(x=15, y=272, txt="............................................................................")
pdf.text(x=22, y=276, txt="datum, jmeno, prijmeni a podpis")

print("Success! Take your pdf and have fun.")
pdf.output("output.pdf")