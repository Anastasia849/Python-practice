from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
import datetime


def info_today(d=datetime.datetime.today()):
    response = urllib.request.urlopen(
        'http://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(d.strftime('%d/%m/%Y')))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName('Valute')
    list1 = []
    for node in nodeArray:
        childList = node.childNodes
        dict1 = {}
        for child in childList:
            dict1.update({child.nodeName: child.childNodes[0].nodeValue})
        list1.append(dict1)
    for i in list1:
        i['Value'] = float(i['Value'].replace(',', '.'))
        i['Nominal'] = float(i['Nominal'].replace(',', '.'))
    return list1


def clicked1():
    r1 = float(txt1.get())
    if combo1.get() == combo2.get():
        res = 1
    elif combo1.get() == 'Рубль':
        for i1 in list1:
            if i1.get('Name') == combo2.get():
                res = i1.get('Nominal') / i1.get('Value')
    elif combo2.get() == 'Рубль':
        for i1 in list1:
            if i1.get('Name') == combo1.get():
                res = i1.get('Value') / i1.get('Nominal')
    else:
        val, nom = 0, 0
        for i1 in list1:
            if i1.get('Name') == combo1.get():
                val = i1.get('Nominal') / i1.get('Value')
            if i1.get('Name') == combo2.get():
                nom = i1.get('Nominal') / i1.get('Value')
        res = nom / val
    lbl1.configure(text=r1 * res)


def dates_2019(m):
    list3 = ['Январь 2019', 'Февраль 2019', 'Март 2019', 'Апрель 2019', 'Май 2019', 'Июнь 2019', 'Июль 2019',
             'Август 2019', 'Сентябрь 2019', 'Октябрь 2019', 'Ноябрь 2019', 'Декабрь 2019']
    for i in range(len(list3)):
        if m == list3[i]:
            list4 = []
            start_d = datetime.date(2019, i + 1, 1)
            while start_d.month != i + 2:
                list4.append(start_d)
                if start_d == datetime.date(2019, 12, 31):
                    break
                start_d += datetime.timedelta(days=1)
            return list4


def clicked2():
    x = []
    y = []
    for d in dates_2019(combo3.get()):
        x.append(d.day)
        list7 = info_today(d)
        for i1 in list7:
            if i1.get('Name') == combo4.get():
                y.append(float(i1.get('Value') / i1.get('Nominal')))
    matplotlib.use('TkAgg')
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
    plot_widget = canvas.get_tk_widget()
    fig.clear()
    plt.plot(x, y)
    plt.grid()
    plot_widget.grid(row=3, column=2)


window = Tk()

window.title("Конвертер валют")
window.geometry("900x700")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Курсы валют")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="График")

list_combo1 = ['Рубль']
list1 = info_today()
for i in list1:
    list_combo1.append(i.get('Name'))

combo1 = ttk.Combobox(tab1, width=30)
combo1['values'] = list_combo1
combo1.current(0)
combo1.grid(column=0, row=0, padx=4, pady=3)
combo2 = ttk.Combobox(tab1, width=30)
combo2['values'] = list_combo1
combo2.current(0)
combo2.grid(column=1, row=0, padx=4, pady=3)

txt1 = Entry(tab1)
txt1.grid(column=0, row=1, padx=4, pady=3)
btn1 = Button(tab1, text='Конвертировать', command=clicked1, width=25)
btn1.grid(column=2, row=0, padx=4, pady=3)

lbl1 = Label(tab1, text='')
lbl1.grid(column=1, row=1, padx=4, pady=3)

combo3 = ttk.Combobox(tab2, width=30)
combo3.grid(column=0, row=0, padx=4, pady=3)

combo3['values'] = ['Январь 2019', 'Февраль 2019', 'Март 2019', 'Апрель 2019', 'Май 2019', 'Июнь 2019', 'Июль 2019',
                    'Август 2019', 'Сентябрь 2019', 'Октябрь 2019', 'Ноябрь 2019', 'Декабрь 2019']
combo3.current(0)
combo4 = ttk.Combobox(tab2, width=30)
del list_combo1[0]
combo4['values'] = list_combo1
combo4.current(0)
combo4.grid(column=0, row=1, padx=4, pady=3)
btn2 = Button(tab2, text='График', command=clicked2, width=25)
btn2.grid(column=0, row=2, padx=4, pady=3)

tab_control.pack(expand=True, fill=BOTH)
window.mainloop()
