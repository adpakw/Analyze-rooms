from tkinter import *
import os


window = 0
D = 100


def choose_room():
    select = list(room_list.curselection())
    select.reverse()
    file = open('Rooms\{}.txt'.format(room_list.get(select)), 'r')
    textf = file.read()
    global dangers
    dangers = Label(main_window, text=textf)
    dangers.place(x=1000, y=90)
    file = open('Rooms\{}.txt'.format(room_list.get(select)), 'r')
    for index, line in enumerate(file):
        if index == 1:
            a = line
            break
    flag = 0
    wd = ''
    lg = ''
    for j in list(a):
        if j == ' ':
           flag += 1
        if flag == 1:
            wd += j
        elif flag == 3:
            lg += j
    wd = int(wd)
    lg = int(lg)
    if wd == lg:
        room_rect.create_rectangle(0, 0, 500, 500, fill='white', outline='white')
        room_rect.create_rectangle(25, 25, 475, 475)
        room_rect.create_line(475, 400, 500, 475)
    elif wd < lg:
        room_rect.create_rectangle(0, 0, 500, 500, fill='white', outline='white')
        room_rect.create_rectangle(100, 25, 400, 475)
        room_rect.create_line(400, 400, 450, 450)
    elif wd > lg:
        room_rect.create_rectangle(0, 0, 500, 500, fill='white', outline='white')
        room_rect.create_rectangle(25, 100, 475, 400)
        room_rect.create_line(475, 300, 500, 380)



def del_list():
    select = list(room_list.curselection())
    select.reverse()
    for i in select:
        os.remove('Rooms\{}.txt'.format(room_list.get(select)))
        room_list.delete(i)


def add():
    file = open('Rooms\{}.txt'.format(n.get()), 'w')
    file.write('Название помещения: ' + '{}'.format(n.get()) + '\n'+ 'Ширина: '+'{}'.format(wdth.get())+' Длина: '+\
               '{}'.format(lngth.get()) + '\nКоличество окон: ' + '{}'.format(w.get()) + '\n')
    if wsecr.get() == True:
        file.write('Окна защищены' + '\n')
    elif wsecr.get() == False:
        file.write('Окна не защищены' + '\n')
    if obser.get() == 0:
        file.write("Находится под наблюдением защищенного устройства" + "\n")
    elif obser.get() == 1:
        file.write("Находится под наблюдением незащищенного устройства" + "\n")
    elif obser.get() == 2:
        file.write('Не находится под наблюдением' + '\n')
    if acs.get() == 0:
        file.write("Нет доступа для 3-х лиц" + "\n")
    elif acs.get() == 1:
        file.write("Есть доступ для проверенных 3-х лиц" + "\n")
    elif acs.get() == 2:
        file.write('Не ограничен доступ для 3-х лиц' + '\n')
    if ren.get() == 0:
        file.write('Ремонт был недавно, персонал надежный' + '\n')
    elif ren.get() == 1:
        file.write('Ремонт был недавно, персонал ненадежный' + '\n')
    elif ren.get() == 2:
        file.write('Ремонта недавно не было' + '\n')
    file.write('Периметр: ' + '{}'.format(2*(int(lngth.get())+int(wdth.get()))) + '\n')
    if infr.get():
        file.write('Помехи есть' + '\n')
    else:
        file.write('Помех нет' + '\n')
    if wall.get():
        file.write('Стенки тонкие' + '\n')
    else:
        file.write('Стенки толстые' + '\n')
    if nbr.get():
        file.write('Cоседние помещения под контролем' + '\n')
    else:
        file.write('Cоседние помещения не под контролем' + '\n')
    if chk.get():
        file.write('Периодические проверки проходят' + '\n')
    else:
        file.write('Периодические проверки не проходят' + '\n')
    file.write('Уровень речевого сигнала: '+'{}\n'.format(vol.get()))
    if fcheck.get() == True:
        file.write('\nПомещение защищено\n')
    else:
        file.write('\nУгрозы\nУдаленная прослушка:\n')
        if D <= (int(vol.get())-int(infr.get())-2*(int(lngth.get())+int(wdth.get()))):
            file.write("Есть угроза\nВизуальная прослушка:\n")
        else:
            file.write("Нет угрозы\nВизуальная прослушка:\n")
        if w.get() == '0':
            file.write('Нет угроз для прослушки через окна\nПодслушивающие устройства:\n')
        elif w.get() != '0':
            if wsecr.get() == True:
                file.write('Нет угроз для прослушки через окна\nПодслушивающие устройства:\n')
            elif wsecr.get() == False:
                file.write('Есть угроза прослушки через окна, защитите окна!\nПодслушивающие устройства:\n')
        if obser.get() == 0 or obser.get() == 2:
            file.write('Угроз наблюдения нет\n')
        elif obser.get() == 1:
            file.write('Есть угроза наблюдения, защитите устройства наблюдения!\n')
        if acs.get() == 0:
            file.write('Угроз от 3-х лиц нет\n')
        elif acs.get() == 1 or acs.get() == 2:
            file.write('Есть угроза от 3-х лиц, защитите помещение от 3-х лиц!\n')
        if ren.get() == 0 or ren.get() == 2:
            file.write('Угроз со стороны персонала нет\n')
        elif ren.get() == 1:
            file.write('Есть угроза со стороны персонала, проверьте персонал!\n')
    file.close()
    heading.destroy()
    name.destroy()
    n.destroy()
    width.destroy()
    wdth.destroy()
    length.destroy()
    lngth.destroy()
    windows.destroy()
    w.destroy()
    wsec.destroy()
    wsecr1.destroy()
    wsecr2.destroy()
    observation.destroy()
    obs1.destroy()
    obs2.destroy()
    obs3.destroy()
    access.destroy()
    acs1.destroy()
    acs2.destroy()
    acs3.destroy()
    renovation.destroy()
    ren1.destroy()
    ren2.destroy()
    ren3.destroy()
    interference.destroy()
    infr.destroy()
    walls.destroy()
    wall1.destroy()
    wall2.destroy()
    neighbors.destroy()
    nbr1.destroy()
    nbr2.destroy()
    checks.destroy()
    chk1.destroy()
    chk2.destroy()
    full_check.destroy()
    fcheck1.destroy()
    fcheck2.destroy()
    volume.destroy()
    vol.destroy()
    add_room_button.destroy()
    white_window.destroy()
    main_menu()


def main_menu():
    global room_list_heading
    room_list_heading = Label(main_window, text='Список комнат', font=('Arial', 15), fg='white', bg='black')
    room_list_heading.place(x=20, y=30)
    global room_list
    room_list = Listbox(main_window, width=55, height=30)
    room_list.place(x=20, y=60)
    for i in os.listdir('Rooms'):
        i = i[:-4]
        room_list.insert(0, i)
    global choose
    choose = Button(main_window, text='Выбрать', command=choose_room)
    choose.place(x=20, y=550)
    global delete_button
    delete_button = Button(main_window, text='Удалить', command=del_list)
    delete_button.place(x=90, y=550)
    global add_button
    add_button = Button(main_window, text="Добавить помещение...", command=add_menu)
    add_button.place(x=20, y=580)
    global room_rect
    room_rect = Canvas(main_window, width=500, height=500, bg='white')
    room_rect.place(x=450, y=50)
    global scheme
    scheme = Label(main_window, text='Схема помещения', font=('Arial', 15), fg='white', bg='black')
    scheme.place(x=450, y=25)



def add_menu():
    scheme.destroy()
    room_list_heading.destroy()
    room_list.destroy()
    choose.destroy()
    delete_button.destroy()
    add_button.destroy()
    room_rect.destroy()
    global white_window
    white_window = Canvas(main_window, width=1350, height=650, bg='lightgrey')
    white_window.place(x=0, y=0)
    global heading
    heading = Label(main_window, text="Введите данные помещения", font=('Arial', 15), fg='white', bg='black')
    heading.place(x=5, y=5)
    global name
    name = Label(main_window, text="Введите название помещения:", font=('Arial', 10), bg='lightgrey')
    name.place(x=15, y=45)
    global n
    n = Entry(main_window, width=30)
    n.place(x=210, y=45)
    global width
    width = Label(main_window, text='Ширина:', font=('Arial', 10), bg='lightgrey')
    width.place(x=15, y=70)
    global wdth
    wdth = Entry(main_window, width=5)
    wdth.place(x=75, y=70)
    global length
    length = Label(main_window, text='Длина:', font=('Arial', 10), bg='lightgrey')
    length.place(x=120, y=70)
    global lngth
    lngth = Entry(main_window, width=5)
    lngth.place(x=170, y=70)
    global windows
    windows = Label(main_window, text='Количество окон:', font=('Arial', 10), bg='lightgrey')
    windows.place(x=15, y=95)
    global w
    w = Entry(main_window, width=5)
    w.place(x=125, y=95)
    global wsec
    wsec = Label(main_window, text='Защищены окна или нет?', font=('Arial', 10), bg='lightgrey')
    wsec.place(x=15, y=115)
    global wsecr
    global wsecr1
    global wsecr2
    wsecr = BooleanVar()
    wsecr.set(False)
    wsecr1 = Radiobutton(main_window, text='Да', variable=wsecr, value=True, bg='lightgrey')
    wsecr2 = Radiobutton(main_window, text='Нет', variable=wsecr, value=False, bg='lightgrey')
    wsecr1.place(x=15, y=135)
    wsecr2.place(x=55, y=135)
    global observation
    observation = Label(main_window, text='Находится под наблюдением?', font=('Arial', 10), bg='lightgrey')
    observation.place(x=15, y=160)
    global obser
    global obs1
    global obs2
    global obs3
    obser = IntVar()
    obser.set(2)
    obs1 = Radiobutton(main_window, text='Да, под наблюдением защищенного устройства', variable=obser, value=0, bg='lightgrey')
    obs2 = Radiobutton(main_window, text='Да, под наблюдением незащищенного устройства', variable=obser, value=1, bg='lightgrey')
    obs3 = Radiobutton(main_window, text='Нет', variable=obser, value=2, bg='lightgrey')
    obs1.place(x=15, y=180)
    obs2.place(x=15, y=200)
    obs3.place(x=15, y=220)
    global access
    access = Label(main_window, text='Ограничен ли доступ для 3-х лиц?', font=('Arial', 10), bg='lightgrey')
    access.place(x=15, y=245)
    global acs
    global acs1
    global acs2
    global acs3
    acs = IntVar()
    acs.set(2)
    acs1 = Radiobutton(main_window, text='Да', variable=acs, value=0, bg='lightgrey')
    acs2 = Radiobutton(main_window, text='Неограничен', variable=acs, value=1, bg='lightgrey')
    acs3 = Radiobutton(main_window, text='Не ограничен только для проверенных', variable=acs, value=2, bg='lightgrey')
    acs1.place(x=15, y=265)
    acs2.place(x=15, y=285)
    acs3.place(x=15, y=305)
    global renovation
    renovation = Label(main_window, text='Был ли недавно ремонт?', font=('Arial', 10), bg='lightgrey')
    renovation.place(x=15, y=330)
    global ren
    global ren1
    global ren2
    global ren3
    ren = IntVar()
    ren.set(2)
    ren1 = Radiobutton(main_window, text='Да, надежный персонал', variable=ren, value=0, bg='lightgrey')
    ren2 = Radiobutton(main_window, text='Да, ненадежный персонал', variable=ren, value=1, bg='lightgrey')
    ren3 = Radiobutton(main_window, text='Нет', variable=ren, value=2, bg='lightgrey')
    ren1.place(x=15, y=350)
    ren2.place(x=180, y=350)
    ren3.place(x=350, y=350)
    global interference
    interference = Label(main_window, text='Уровень помех:', font=('Arial', 10), bg='lightgrey')
    interference.place(x=15, y=375)
    global infr
    infr = Entry(main_window, width=5)
    infr.place(x=115, y=375)
    global walls
    walls = Label(main_window, text='Тонкие стенки?', font=('Arial', 10), bg='lightgrey')
    walls.place(x=15, y=400)
    global wall
    global wall1
    global wall2
    wall = BooleanVar()
    wall.set(False)
    wall1 = Radiobutton(main_window, text='Да', variable=wall, value=True, bg='lightgrey')
    wall2 = Radiobutton(main_window, text='Нет', variable=wall, value=False, bg='lightgrey')
    wall1.place(x=15, y=420)
    wall2.place(x=55, y=420)
    global neighbors
    neighbors = Label(main_window, text='Под контролем ли соседние помещения?', font=('Arial', 10), bg='lightgrey')
    neighbors.place(x=15, y=445)
    global nbr
    global nbr1
    global nbr2
    nbr = BooleanVar()
    nbr.set(False)
    nbr1 = Radiobutton(main_window, text='Да', variable=nbr, value=True, bg='lightgrey')
    nbr2 = Radiobutton(main_window, text='Нет', variable=nbr, value=False, bg='lightgrey')
    nbr1.place(x=15, y=465)
    nbr2.place(x=55, y=465)
    global checks
    checks = Label(main_window, text='Происходят ли периодические проверки?', font=('Arial', 10), bg='lightgrey')
    checks.place(x=15, y=490)
    global chk
    global chk1
    global chk2
    chk = BooleanVar()
    chk.set(False)
    chk1 = Radiobutton(main_window, text='Да', variable=chk, value=True, bg='lightgrey')
    chk2 = Radiobutton(main_window, text='Нет', variable=chk, value=False, bg='lightgrey')
    chk1.place(x=15, y=510)
    chk2.place(x=55, y=510)
    global full_check
    full_check = Label(main_window, text='Производилась ли полная проверка?', font=('Arial', 10), bg='lightgrey')
    full_check.place(x=15, y=535)
    global fcheck
    global fcheck1
    global fcheck2
    fcheck = BooleanVar()
    fcheck.set(False)
    fcheck1 = Radiobutton(main_window, text='Да', variable=fcheck, value=True, bg='lightgrey')
    fcheck2 = Radiobutton(main_window, text='Нет', variable=fcheck, value=False, bg='lightgrey')
    fcheck1.place(x=15, y=555)
    fcheck2.place(x=55, y=555)
    global volume
    volume = Label(main_window, text='Уровень речевого сигнала:', font=('Arial', 10), bg='lightgrey')
    volume.place(x=15, y=580)
    global vol
    vol = Entry(main_window, width=15)
    vol.place(x=185, y=580)
    global add_room_button
    add_room_button = Button(main_window, text='Добавить помещение', command=add)
    add_room_button.place(x=15, y=610)



main_window = Tk()
main_window.title("Анализ помещения на безопасность")
main_window.geometry("1350x650")
if window == 0:
    main_menu()
main_window.mainloop()