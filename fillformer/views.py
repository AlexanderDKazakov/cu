from django.shortcuts import render
from django.shortcuts import redirect
from .forms import MessageForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.units import cm
from reportlab.lib.colors import pink, black, red, blue, green

def fillformer(request):
    value_dict = {}
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # value_dict['chislo_dohody'] = data['chislo_dohody']
            value_dict['jmeno'] = data['jmeno']
            value_dict['zakaz_chislo'] = data['zakaz_chislo']
            value_dict['odmenyKc'] = data['odmenyKc']
            value_dict['odmenySl'] = data['odmenySl']
            value_dict['total_work_time'] = data['total_work_time']
            # some_view(request)
            return some_view(request, value_dict)
        else:
            return redirect('/')

    return render(request, 'fillformer/content.html', {'form': MessageForm(), 'value_dict': value_dict})



def some_view(request, value_dict):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+str(value_dict['jmeno']) +'".pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    my_x = 450; my_y = 800
    p.setFont("Helvetica", 8)
    p.drawString(my_x, my_y, "Univerzita Karlova v Praze")
    p.drawString(my_x, my_y-10, "Prerodovedceska faculta")
    p.drawString(my_x, my_y-20, "Albertov, 6 12843 Praha 2")
    p.drawString(my_x, my_y-30, "ICO: 00216208, DIC: CZ00216208")
    #p.drawString(10, 10, value_dict['chislo_dohody'])
    my_x = 210; my_y = 740
    p.setFont('Helvetica-Bold', 14)
    p.drawString(my_x-40, my_y, "VYKAZ PRACE / ODPRACOVANYCH HODIN")
    p.drawString(my_x+30, my_y-17, "PRIKAZ K PROPLACENI")
    ###START  ROWS
    my_x = 45; my_y = 690
    p.setFont('Helvetica', 8)
    p.drawString(my_x, my_y, "Cislo dohody:")
    my_x_tab_s = 130; my_x_tab_e = 210;
    my_y_tab_s = 700; my_y_tab_e = 685;
    p.grid([my_x_tab_s, my_x_tab_e], [my_y_tab_s, my_y_tab_e]) ### X_s X_e ; Y_s Y_e
    ### NEW ROW
    p.drawString(my_x, my_y-20, "Jmeno, prijmeny, titul:")
    p.grid([my_x_tab_s, 500], [my_y_tab_s-20, my_y_tab_e-20])
    p.drawString(my_y_tab_s+15, my_y-21, value_dict['jmeno'])
    ### NEW ROW
    p.drawString(my_x, my_y - 40, "Zakazka chislo:")
    p.grid([my_x_tab_s, my_x_tab_s+30], [my_y_tab_s-40, my_y_tab_e-40])
    p.drawString(my_x_tab_s+6, my_y_tab_s-51, value_dict['zakaz_chislo'].split()[0])
    p.drawString(my_x_tab_s + 34, my_y_tab_s - 51, "-")
    ## HERE WILL BE ---
    p.grid([my_x_tab_s+40, my_x_tab_s+65], [my_y_tab_s-40, my_y_tab_e-40])
    p.drawString(my_x_tab_s + 46, my_y_tab_s - 51, value_dict['zakaz_chislo'].split()[1])
    p.drawString(my_x_tab_s + 69, my_y_tab_s - 51, "-")
    ## HERE WILL BE ---
    p.grid([my_x_tab_s+75, my_x_tab_s+120], [my_y_tab_s-40, my_y_tab_e-40])
    p.drawString(my_x_tab_s + 85, my_y_tab_s - 51, value_dict['zakaz_chislo'].split()[2])
    ## NEW ROW
    p.drawString(my_x, my_y-60, "Vise odmeny v Kc:")
    p.grid([my_x_tab_s, my_x_tab_e], [my_y_tab_s-60, my_y_tab_e-60])  ### X_s X_e ; Y_s Y_e
    p.drawString(my_x_tab_s+25, my_y-61, value_dict['odmenyKc']+" Kc")
    ## NEW ROW
    p.drawString(my_x, my_y-80, "Vise odmeny slovne:")
    p.grid([my_x_tab_s, 500], [my_y_tab_s-80, my_y_tab_e-80])  ### X_s X_e ; Y_s Y_e
    p.drawString(my_y_tab_s+15, my_y-81, value_dict['odmenySl'])
    ### TABLE HEAD

    p.setFont('Helvetica-Bold', 8)
    p.grid([my_x-15, my_x+35], [my_y_tab_s-110, my_y_tab_e-107])
    p.drawString(43, my_y-109, "Mesic")
    p.grid([my_x+35, my_x+85], [my_y_tab_s-110, my_y_tab_e-107])
    p.drawString(91, my_y - 109, "MONTH")
    p.grid([my_x+85, my_x+530], [my_y_tab_s-110, my_y_tab_e-107])
    p.drawString(325, my_y - 109, "Rok"+"YEAR")
    ### NEXT ROW
    p.setFont('Helvetica', 7)
    p.grid([my_x-15, my_x + 35], [my_y_tab_s-122, my_y_tab_e-119])
    p.drawString(my_x-12, my_y-120, "Den v mesice")
    #
    p.grid([my_x+35, my_x + 85], [my_y_tab_s - 122, my_y_tab_e - 119])
    p.drawString(my_x+39, my_y-120, "Pohet  hodin")
    #
    p.grid([my_x - 15, my_x + 35], [my_y_tab_s - 122, my_y_tab_e - 119])
    p.drawString(my_x - 12, my_y - 120, "Den v mesice")




    # Close the PDF object cleanly, and we're done.



    p.showPage()
    p.save()
    return response

def coords():
    from reportlab.lib.units import inch
    from reportlab.lib.colors import pink, black, red, blue, green
    c = canvas
    c.setStrokeColor(pink)
    c.grid([inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(black)
    c.setFont("Times-Roman", 20)
    c.drawString(0,0, "(0,0) the Origin")
    c.drawString(2.5*inch, inch, "(2.5,1) in inches")
    c.drawString(4*inch, 2.5*inch, "(4, 2.5)")
    c.setFillColor(red)
    c.rect(0,2*inch,0.2*inch,0.3*inch, fill=1)
    c.setFillColor(green)
    c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)
