# -*- utf-8 -*-
from django.shortcuts import render
from .forms import MessageForm
from django.conf import settings
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from django.http import HttpResponse
import random
from calendar import monthrange
import datetime
pdfmetrics.registerFont(TTFont('Arial', settings.STATICFILES_DIRS[0] + '/fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBd', settings.STATICFILES_DIRS[0] + '/fonts/arialbd.ttf'))


def fillformer(request):
    value_dict = {}
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # value_dict['chislo_dohody'] = data['chislo_dohody']
            value_dict['jmeno'] = data['jmeno']
            value_dict['zakaz_chislo1'] = data['zakaz_chislo1']
            value_dict['zakaz_chislo2'] = data['zakaz_chislo2']
            value_dict['zakaz_chislo3'] = data['zakaz_chislo3']
            value_dict['odmenyKc'] = data['odmenyKc']
            value_dict['odmenySl'] = data['odmenySl']
            value_dict['actions'] = data['actions']
            value_dict['date_field'] = data['date_field']
            value_dict['date_field_except'] = data['date_field_except']
            value_dict['total_work_time'] = data['total_work_time']
            value_dict['decision'] = data['decision']
            # some_view(request)
            # print(value_dict)
            return some_view(request, value_dict)
        else:
            return HttpResponse('You put not valid info!!!')

    return render(request, 'fillformer/content.html', {'form': MessageForm(), 'value_dict': value_dict})



def some_view(request, value_dict):
    month_dict = {
        '01': 'leden',
        '02': 'únor',
        '03': 'břesen',
        '04': 'duben',
        '05': 'květen',
        '06': 'červen',
        '07': 'červenec',
        '08': 'srpen',
        '09': 'září',
        '1': 'leden',
        '2': 'únor',
        '3': 'břesen',
        '4': 'duben',
        '5': 'květen',
        '6': 'červen',
        '7': 'červenec',
        '8': 'srpen',
        '9': 'září',
        '10': 'říjen',
        '11': 'listopad',
        '12': 'prosinec',
    }
    date_of_doc = [x.strip()for x in value_dict['date_field'].split(',')][1]
    print(date_of_doc)
    days_in_month = monthrange(int([x.strip()for x in value_dict['date_field'].split(',')][1]), int([x.strip()for x in value_dict['date_field'].split(',')][0]))[1]
    # print(days_in_month)
    # print(list(value_dict['date_field_except']))
    all_days = [i for i in range(1, days_in_month + 1) if str(i) not in [x.strip()for x in value_dict['date_field_except'].split(',')]]
    print("ALL DAYS EXCEPT :", all_days)
    work_days = []
    for day in all_days:
        ans = datetime.date(int(value_dict['date_field'].split(',')[1]), int(value_dict['date_field'].split(',')[0]), day)
        if ans.strftime("%A") != 'Saturday' and ans.strftime("%A") != 'Sunday':
            # print(day, ans.strftime("%A"))
            work_days.append(day)
    print("WORK DAYS = ", work_days)
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+str(value_dict['jmeno']) + '".pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    avalable = p.getAvailableFonts()
    print(avalable)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    my_x = 450; my_y = 800
    p.setFont('Arial', 8)
    p.drawString(my_x, my_y, "Univerzita Karlova v Praze")
    p.drawString(my_x, my_y-10, u"Přírodovědeská faculta")
    p.drawString(my_x, my_y-20, "Albertov, 6 128 43 Praha 2")
    p.drawString(my_x, my_y-30, "IČO: 00216208, DIČ: CZ00216208")
    # p.drawString(10, 10, value_dict['chislo_dohody'])
    my_x = 210; my_y = 740
    p.setFont('ArialBd', 13)  # BOLD !!!
    p.drawString(my_x-40, my_y, "VÝKAZ PRÁCE / ODPRACOVANÝCH HODIN")
    p.drawString(my_x+30, my_y-17, "PŘÍKAZ K PROPLACENÍ")
    # START  ROWS
    my_x = 45; my_y = 690
    p.setFont('Arial', 7)
    p.drawString(my_x, my_y, u"Číslo dohody:")
    my_x_tab_s = 130; my_x_tab_e = 210;
    my_y_tab_s = 700; my_y_tab_e = 685;
    p.grid([my_x_tab_s, my_x_tab_e], [my_y_tab_s, my_y_tab_e])  # X_s X_e ; Y_s Y_e
    # NEW ROW
    p.drawString(my_x, my_y-20, "Jméno, příjmení, titul:")
    p.grid([my_x_tab_s, 500], [my_y_tab_s-20, my_y_tab_e-20])
    p.drawString(my_x_tab_s+15, my_y-21, value_dict['jmeno'])
    # NEW ROW
    # list_number = [x.strip() for x in value_dict['zakaz_chislo'].split(',')]
    # print(list_number[0], list_number[1], list_number[2])
    p.drawString(my_x, my_y - 40, "Zakázka číslo:")
    p.grid([my_x_tab_s, my_x_tab_s+30], [my_y_tab_s-40, my_y_tab_e-40])
    p.setFont('Arial', 7)  #
    p.drawString(my_x_tab_s+7, my_y_tab_s-51, value_dict['zakaz_chislo1'])
    p.drawString(my_x_tab_s + 34, my_y_tab_s - 51, "-")
    #
    p.grid([my_x_tab_s+40, my_x_tab_s+65], [my_y_tab_s-40, my_y_tab_e-40])
    p.drawString(my_x_tab_s + 46, my_y_tab_s - 51, value_dict['zakaz_chislo2'])
    p.drawString(my_x_tab_s + 69, my_y_tab_s - 51, "-")
    #
    p.grid([my_x_tab_s+75, my_x_tab_s+120], [my_y_tab_s-40, my_y_tab_e-40])
    p.drawString(my_x_tab_s + 85, my_y_tab_s - 51, value_dict['zakaz_chislo3'])
    # NEW ROW
    p.setFont('Arial', 7)  #
    p.drawString(my_x, my_y-60, "Výše odměny v Kč:")
    p.grid([my_x_tab_s, my_x_tab_e], [my_y_tab_s-60, my_y_tab_e-60])  # X_s X_e ; Y_s Y_e
    p.drawString(my_x_tab_s+25, my_y-61, value_dict['odmenyKc']+" Kč")
    # NEW ROW
    p.drawString(my_x, my_y-80, "Výše odměny slovně:")
    p.grid([my_x_tab_s, 500], [my_y_tab_s-80, my_y_tab_e-80])  # X_s X_e ; Y_s Y_e
    p.drawString(my_x_tab_s+15, my_y-81, value_dict['odmenySl'])
    # TABLE HEAD
    p.setFont('ArialBd', 7)  # BOLD !!!
    p.grid([my_x-15, my_x+45], [my_y_tab_s-110, my_y_tab_e-107])
    p.drawString(50, my_y-109, "Měsíc:")
    p.grid([my_x+45, my_x+105], [my_y_tab_s-110, my_y_tab_e-107])
    p.drawString(110, my_y - 109, month_dict[value_dict['date_field'].split(',')[0]])

    p.grid([my_x+105, my_x+530], [my_y_tab_s-110, my_y_tab_e-107])
    p.drawString(340, my_y - 109, "Rok"+str(value_dict['date_field'].split(',')[1]))
    # NEXT ROW
    p.setFont('Arial', 7)
    p.grid([my_x-15, my_x + 45], [my_y_tab_s-122, my_y_tab_e-119])
    p.drawString(my_x-5, my_y-120, "Den v měsíci")
    p.grid([my_x+45, my_x + 105], [my_y_tab_s - 122, my_y_tab_e - 119])
    p.drawString(my_x+55, my_y-120, "Počet hodin")
    p.grid([my_x + 105, my_x + 530], [my_y_tab_s - 122, my_y_tab_e - 119])
    p.drawString(334, my_y - 120, "Popis činnosti")
    # A LOT OF ROWS
    my_x_start1 = 30; my_x_end1 = 90
    my_x_start2 = 90; my_x_end2 = 150
    my_x_start3 = 150; my_x_end3 = 575
    my_y_tab_start1 = 578; my_y_tab_end1 = 566
    my_x_start_label = 57; my_y_start_label = 570
    for i in range(1, 32):
        if i > 9:
            my_x_start_label = 55
        p.grid([my_x_start1, my_x_end1], [my_y_tab_start1-i*12, my_y_tab_end1-i*12])
        p.drawString(my_x_start_label, my_y_start_label-i*12, str(i)+'.')
        p.grid([my_x_start2, my_x_end2], [my_y_tab_start1-i*12, my_y_tab_end1-i*12])
        p.grid([my_x_start3, my_x_end3], [my_y_tab_start1-i*12, my_y_tab_end1-i*12])
    # for for data
    calc_total_hours = 0  # STARTS TABLE LIST; ENDS 243
    day_chosen = random.sample(work_days, len(work_days))
    total_time = int(value_dict['total_work_time'])
    # list_i = random.randint(0, len([x.strip() for x in value_dict['actions'].split(',')]))
    # print("LIST I", list_i)
    print("DAY CHOSEN = ", day_chosen)
    # print('Actions = ', [x.strip() for x in value_dict['actions'].split(',')])
    i = 0
    while calc_total_hours != int(value_dict['total_work_time']):
        x_num = 118
        y_num = 569

        action_list = random.sample([x.strip() for x in value_dict['actions'].split(',')], len([x.strip() for x in value_dict['actions'].split(',')]))
        action_list = 32 * action_list
        print(action_list)
        # p.drawString(118, 546, "5")
        for day in day_chosen:
            # print('DAY = ', day)
            time_work = random.randint(2, 5)
            if (total_time - calc_total_hours >= 5) and (time_work < 5):
                # print("time work = ", time_work)
                p.drawString(x_num, y_num-12*day, str(time_work))
                p.drawString(x_num+50, y_num-12*day, action_list[i])
                calc_total_hours = calc_total_hours + time_work
                # print ('calc_total_hours', calc_total_hours)
                i += 1
                # print('number action', i)
                # print (y_num + 4 * day)
                # print('I = ', i)
            elif 0 < total_time - calc_total_hours <= 4:
                time_work = total_time - calc_total_hours
                # print("time work = ", time_work)
                p.drawString(x_num, y_num-12*day, str(time_work))
                p.drawString(x_num+50, y_num-12*day, action_list[i])
                calc_total_hours = calc_total_hours + time_work
                # print('calc_total_hours', calc_total_hours)
                i += 1
                # print('I = ', i)
            elif total_time - calc_total_hours == 0:
                break
            else:
                print("Time work generated unsuitable...")
                # i = i - 1
            # time.sleep(1)

    # NEW ROW
    p.setFont('ArialBd', 8)
    p.grid([my_x_start1, my_x_end1], [my_y_tab_start1 - 32 * 12, my_y_tab_end1 - 32 * 12])
    p.drawString(my_x_start_label-23, my_y_start_label - 32 * 12, 'Celkem hodin:')
    p.grid([my_x_start2, my_x_end2], [my_y_tab_start1 - 32 * 12, my_y_tab_end1 - 32 * 12])
    p.drawString(my_x_start_label + 60, my_y_start_label - 32 * 12, value_dict['total_work_time'])
    p.grid([my_x_start3, my_x_end3], [my_y_tab_start1 - 32 * 12, my_y_tab_end1 - 32 * 12])
    #
    p.setFont('Arial', 8)
    if value_dict['decision'] == 'No' or value_dict['decision'] == 'no':
        p.drawString(my_x_start_label+8, my_y_start_label - 36 * 12, 'vedoucí pracoviště')
        p.roundRect(my_x_start_label-4, my_y_start_label-434, 8, 8, 4, fill=0)
        # p.roundRect(my_x_start_label-2, my_y_start_label-433, 6, 6, 2, fill=1)
        # canvas.roundRect(left, bottom, width, height, radius):
        p.roundRect(my_x_start_label+88, my_y_start_label-434, 8, 8, 4, fill=0)
        p.roundRect(my_x_start_label+90, my_y_start_label-432, 4, 4, 2, fill=1)
        p.drawString(my_x_start_label + 100, my_y_start_label - 36 * 12, 'řešitel grantu')
        #
    else:
        p.drawString(my_x_start_label + 8, my_y_start_label - 36 * 12, 'vedoucí pracoviště')
        p.roundRect(my_x_start_label - 4, my_y_start_label - 434, 8, 8, 4, fill=0)
        p.roundRect(my_x_start_label - 2, my_y_start_label - 432, 4, 4, 2, fill=1)
        # canvas.roundRect(left, bottom, width, height, radius):
        p.roundRect(my_x_start_label + 88, my_y_start_label - 434, 8, 8, 4, fill=0)
        # p.roundRect(my_x_start_label+90, my_y_start_label-433, 6, 6, 2, fill=1)
        p.drawString(my_x_start_label + 100, my_y_start_label - 36 * 12, 'řešitel grantu')
    p.drawString(my_x_start_label + 340, my_y_start_label - 430,
                 '.......................................................................')
    p.drawString(my_x_start_label + 367, my_y_start_label - 440, 'datum a podpis zaměstnance')

    p.drawString(my_x_start_label + 340, my_y_start_label - 480,
                 '.......................................................................')
    p.drawString(my_x_start_label + 345, my_y_start_label - 490, 'datum a podpis odpovědhého pracovníka')
    p.drawString(my_x_start_label + 375, my_y_start_label - 500, 'zaměstnaneckého oddělení')
    #
    p.drawString(my_x_start_label, my_y_start_label - 480,
                 '.......................................................................')
    p.drawString(my_x_start_label + 18, my_y_start_label - 490, 'datum, jméno, příjmení a podpis')
    p.showPage()
    p.save()
    return response

