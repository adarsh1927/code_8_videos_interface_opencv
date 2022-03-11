from distutils.spawn import spawn
import time
from imutils.video import FileVideoStream
import threading
import multiprocessing
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imageio
from socketClientver2 import crane31,crane32,crane33,crane34,crane11,crane12,crane14,crane15
window = tk.Tk()

win_width = window.winfo_screenwidth()
win_height = window.winfo_screenheight()
# define outer frame
o_f1_ph = (50/100)*win_height
o_f2_ph = (55/100)*win_height

o_labelfr1 = tk.LabelFrame(window, width=win_width, height=o_f1_ph, )
o_labelfr2 = tk.LabelFrame(window, width=win_width, height=o_f2_ph,)

o_labelfr1.grid(row=0, column=0, sticky='w')
o_labelfr2.grid(row=1, column=0, sticky='w')

# frame inside o_labelfr1
infms_fr1h = (47/100)*o_f1_ph

infr1 = tk.LabelFrame(o_labelfr1, width=win_width, height=infms_fr1h, )
infr2 = tk.LabelFrame(o_labelfr1, width=win_width, height=infms_fr1h, )

infr1.grid(row=0, column=0, sticky="w")
infr2.grid(row=1, column=0, sticky="w")

# frame inside infr1
fr_infrw = (47/100)*win_width
container1 = tk.LabelFrame(infr1, width=fr_infrw, height=infms_fr1h,text = "CRANE-31", labelanchor='n', bg= "#5f6161", fg="#fff491")
container1.grid(row=0, column=0)
container2 = tk.LabelFrame(infr1, width=fr_infrw, height=infms_fr1h,text = "CRANE-32", labelanchor='n', bg= "#5f6161", fg="#fff491")
container2.grid(row=0, column=1)

# frame inside infr2
container3 = tk.LabelFrame(infr2, width=fr_infrw, height=infms_fr1h,text = "CRANE-33", labelanchor='n', bg= "#5f6161", fg="#fff491")
container4 = tk.LabelFrame(infr2, width=fr_infrw, height=infms_fr1h,text = "CRANE-34", labelanchor='n', bg= "#5f6161", fg="#fff491")
container3.grid(row=0, column=0)
container4.grid(row=0, column=1)
# frame inside container 1
container_half = (48/100)*fr_infrw
v1 = tk.LabelFrame(container1, width=container_half,
                   height=infms_fr1h)
v2 = tk.LabelFrame(container1, width=container_half,
                   height=infms_fr1h)
v1.grid(row=0, column=0,sticky="nsew")
v2.grid(row=0, column=1,sticky="nsew")

# frame inside container2
v3 = tk.LabelFrame(container2, width=container_half,
                   height=infms_fr1h)
v4 = tk.LabelFrame(container2, width=container_half,
                   height=infms_fr1h)
v3.grid(row=0, column=0,sticky="nsew")
v4.grid(row=0, column=1,sticky="nsew")

# frame inside container3
v5 = tk.LabelFrame(container3, width=container_half,
                   height=infms_fr1h)
v6 = tk.LabelFrame(container3, width=container_half,
                   height=infms_fr1h)
v5.grid(row=0, column=0,sticky="nsew")
v6.grid(row=0, column=1,sticky="nsew")

# frame inside container4
v7 = tk.LabelFrame(container4, width=container_half,
                   height=infms_fr1h)
v8 = tk.LabelFrame(container4, width=container_half,
                   height=infms_fr1h)
v7.grid(row=0, column=0,sticky="nsew")
v8.grid(row=0, column=1,sticky="nsew")

# frame inside o_labelfr2
win_w_fr2 = win_width-85

fr2_in_h = (60/100)*o_f2_ph

inframe1_fr2 = tk.LabelFrame(o_labelfr2, width=win_w_fr2, height=fr2_in_h,)
inframe2_fr2 = tk.LabelFrame(o_labelfr2, width=win_w_fr2, height=fr2_in_h,)
inframe1_fr2.grid(row=0, column=0, sticky='nw')
inframe2_fr2.grid(row=1, column=0, sticky='nw')


# label for video
video1 = tk.Label(v1,text = "No Video")
video2 = tk.Label(v2,text = "No Video")
video3 = tk.Label(v3,text = "No Video")
video4 = tk.Label(v4,text = "No Video")
video5 = tk.Label(v5,text = "No Video")
video6 = tk.Label(v6,text = "No Video")
video7 = tk.Label(v7,text = "No Video")
video8 = tk.Label(v8,text = "No Video")
video1.grid()
video2.grid()
video3.grid()
video4.grid()
video5.grid()
video6.grid()
video7.grid()
video8.grid()

#becuase when video not comming then label will shrink
container1.columnconfigure([0,1],minsize=container_half+6,weight=1)
container1.rowconfigure(0,minsize=infms_fr1h,weight=1) 

container2.columnconfigure([0,1],minsize=container_half+6,weight=1)
container2.rowconfigure(0,minsize=infms_fr1h,weight=1)

container3.columnconfigure([0,1],minsize=container_half+6,weight=1)
container3.rowconfigure(0,minsize=infms_fr1h,weight=1)

container4.columnconfigure([0,1],minsize=container_half+6,weight=1)
container4.rowconfigure(0,minsize=infms_fr1h,weight=1)

# take videos:
url1 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url2 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url3 = "rtsp://admin:$Admin123@192.168.1.103/cam/realmonitor?channel=1&subtype=1"
url4 = "rtsp://admin:$Admin123@192.168.1.103/cam/realmonitor?channel=1&subtype=1"
url5 = "rtsp://admin:$Admin123@192.168.1.105/cam/realmonitor?channel=1&subtype=1"
url6 = "rtsp://admin:$Admin123@192.168.1.105/cam/realmonitor?channel=1&subtype=1"
url7 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url8 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"

frwidth = int(container_half)      #-((5/100)*container_half))
frheight = infms_fr1h

# def stream(ip,label):
#     vid = cv2.VideoCapture(ip)
#     while True:
#         ret, frame = vid.read()
#         if ret:
#             width = frame.shape[1]
#             height = frame.shape[0]
#             per_width = frwidth*(100/width)
#             per_height = frheight*(100/height)
#             if width > height:
#                 frame = cv2.resize(frame,(int(frwidth),int((per_height/100)*height)))
#             else:
#                 frame = cv2.resize(frame,((per_width/100)*width),frheight)
#             frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame)
#             img = ImageTk.PhotoImage(image = img)
#             label.configure(image= img) 
#             label.image = img
        

# thread1 = threading.Thread(target=stream, args=[url1, video1])
# thread2 = threading.Thread(target=stream, args=[url2, video2])
# thread3 = threading.Thread(target=stream, args=[url3, video3])
# thread4 = threading.Thread(target=stream, args=[url4, video4])
# thread5 = threading.Thread(target=stream, args=[url5, video5])
# thread6 = threading.Thread(target=stream, args=[url6, video6])
# thread7 = threading.Thread(target=stream, args=[url7, video7])
# thread8 = threading.Thread(target=stream, args=[url8, video8])


# thread1.daemon = 1
# thread2.daemon = 2
# thread3.daemon = 3
# thread4.daemon = 4
# thread5.daemon = 5
# thread6.daemon = 6
# thread7.daemon = 7
# thread8.daemon = 8

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()

#:::::::::::::::::::crain moving::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::

c_width = win_w_fr2
c_height = fr2_in_h - (35/100)*fr2_in_h
# one_4_w = c_width/4
t_marg = 10
b_marg = 85
l_marg, r_marg = 10, 90

lt = int(((r_marg/100)*c_width)-((l_marg/100)*c_width))

ct = int(((b_marg/100)*c_height)-((t_marg/100)*c_height))

#  create canvas
canvas = tk.Canvas(inframe1_fr2, width=c_width, height=c_height, bg="#454545")
canvas.grid(row=0, column=0, sticky="nswe")

# two parralel lines
canvas.create_line(((l_marg/100)*c_width), int((t_marg / 100)*c_height),
                   ((r_marg/100)*c_width), int((t_marg / 100)*c_height), width=5, fill="#C19A6B")
canvas.create_line(((l_marg/100)*c_width), int((b_marg / 100)*c_height),
                   ((r_marg/100)*c_width), int((b_marg / 100)*c_height), width=5, fill="#C19A6B")

# crain ct matching line
ctl1 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                          3000, ((t_marg / 100)*c_height), fill="#f1df92", width=1,)

ctl2 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                          3000, ((t_marg / 100)*c_height), fill="#4da6ff", width=1,)

ctl3 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                          3000, ((t_marg / 100)*c_height), fill="#66ff99", width=1,)

ctl4 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                          3000, ((t_marg / 100)*c_height), fill="#ff3333", width=1,)


# crain lines

c_l1_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#f1df92")
c_l1_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#f1df92")

c_l2_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#4da6ff")
c_l2_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#4da6ff")


c_l3_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#66ff99")
c_l3_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#66ff99")

c_l4_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
c_l4_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                          (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#ff3333")



# crain rect
c1 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                             (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#9e8515")

c2 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                             (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#004d99")

c3 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                             (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#009933")

c4 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                             (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#990000")


# Crane Text
t1 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                        * c_height), text="1", font="arial 12 bold", fill="white")
t2 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                        * c_height), text="2", font="arial 12 bold", fill="white")
t3 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                        * c_height), text="3", font="arial 12 bold", fill="white")
t4 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                        * c_height), text="4", font="arial 12 bold", fill="white")

#put ct here when found from server
####################################

totalct = 400
totallt = 600

parralel_line_lenght = ((r_marg/100)*c_width)-((l_marg/100)*c_width)
plldiv4 = ""

for i in range(ct):
    if i % 10 == 0:
        if i != 0:
            canvas.create_line(((l_marg/100)*c_width)-40, i+((t_marg/100)*c_height),
                               ((l_marg/100)*c_width)-30, i+((t_marg/100)*c_height), fill="white")

            canvas.create_text(((l_marg/100)*c_width)-20, i+((t_marg/100)*c_height),
                               font="arial 10", text=int(int((i*((100/ct))/100)*totalct)), fill="white")


canvas.create_text((l_marg/100)*c_width, ((b_marg/100)*c_height) +
                   14, text="Lt", font=" Times 14", fill="#C19A6B")

for i in range(lt):
    if i % 50 == 0:
        if i != 0:
            canvas.create_line(i+((l_marg/100)*c_width), (b_marg/100)*c_height,
                               i+((l_marg/100)*c_width), (b_marg/100)*c_height+5, fill="#EE9A4D")

            canvas.create_text(i+((l_marg/100)*c_width), ((b_marg/100)*c_height)+14,
                               text=int((i*((100/lt))/100)*totallt), font="arial 14")


head_lt1 = tk.Label(inframe2_fr2, text="Lt")
head_ct1 = tk.Label(inframe2_fr2, text="Ct")
head_lt2 = tk.Label(inframe2_fr2, text="Lt")
head_ct2 = tk.Label(inframe2_fr2, text="Ct")
head_lt1.grid(row=0, column=1)
head_ct1.grid(row=0, column=2)
head_lt2.grid(row=0, column=4)
head_ct2.grid(row=0, column=5)
c_name1 = tk.Label(inframe2_fr2, text="crane1", padx = 100, anchor="e")
c_name2 = tk.Label(inframe2_fr2, text="crane2", padx = 100, anchor="e")
c_name3 = tk.Label(inframe2_fr2, text="crane3", padx = 100, anchor="e")
c_name4 = tk.Label(inframe2_fr2, text="crane4", padx = 100, anchor="e")
c_name1.grid(row=1, column=0)
c_name2.grid(row=2, column=0)
c_name3.grid(row=1, column=3)
c_name4.grid(row=2, column=3)


inframe2_fr2.columnconfigure([1,2,4,5], minsize=60, weight=1)
inframe2_fr2.columnconfigure([0,3], minsize=20, weight=1)

# 1
showlt1 = tk.Label(inframe2_fr2, )
showct1 = tk.Label(inframe2_fr2, )
showlt1.grid(row=1, column=1)
showct1.grid(row=1, column=2)

c1_previous_lt = 0
c1_previous_ct = 0


def func_for_c31():
    global c1_previous_lt, c1_previous_ct
    inp_per_Tct = int(crane31()[0])*(100/totalct)  # persent of total ct
    v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
    inp_per_Tlt = int(crane31()[1])*(100/totallt)  # persent of total lt
    v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt

    showlt1["text"] = crane31()[0]
    showct1["text"] = crane31()[1]

    canvas.move(c1, v_o_per_lt - c1_previous_lt, v_o_per_ct - c1_previous_ct)
    canvas.move(c_l1_1, v_o_per_lt - c1_previous_lt, 0)
    canvas.move(c_l1_2, v_o_per_lt - c1_previous_lt, 0)
    canvas.move(t1, v_o_per_lt - c1_previous_lt, v_o_per_ct - c1_previous_ct)
    canvas.move(ctl1, 0, v_o_per_ct - c1_previous_ct)
    c1_previous_ct = v_o_per_ct
    c1_previous_lt = v_o_per_lt

    window.after(100,func_for_c31)
    #window.mainloop()


# 2
showlt2 = tk.Label(inframe2_fr2, )
showct2 = tk.Label(inframe2_fr2, )
showlt2.grid(row=2, column=1)
showct2.grid(row=2, column=2)

c2_previous_lt = 0
c2_previous_ct = 0


def func_for_c32():
    global c2_previous_lt, c2_previous_ct
    inp_per_Tct = int(crane32()[0])*(100/totalct)  # persent of total ct
    v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
    inp_per_Tlt = int(crane32()[1])*(100/totallt)  # persent of total lt
    v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt

    showlt2["text"] = crane32()[0]
    showct2["text"] = crane32()[1]

    canvas.move(c2, v_o_per_lt - c2_previous_lt, v_o_per_ct - c2_previous_ct)
    canvas.move(c_l2_1, v_o_per_lt - c2_previous_lt, 0)
    canvas.move(c_l2_2, v_o_per_lt - c2_previous_lt, 0)
    canvas.move(t2, v_o_per_lt - c2_previous_lt, v_o_per_ct - c2_previous_ct)
    canvas.move(ctl2, 0, v_o_per_ct - c2_previous_ct)

    c2_previous_ct = v_o_per_ct
    c2_previous_lt = v_o_per_lt
    window.after(100,func_for_c32)
    #window.mainloop()

# 3
showlt3 = tk.Label(inframe2_fr2, )
showct3 = tk.Label(inframe2_fr2, )
showlt3.grid(row=1, column=4)
showct3.grid(row=1, column=5)

c3_previous_lt = 0
c3_previous_ct = 0


def func_for_c33():
    global c3_previous_lt, c3_previous_ct
    inp_per_Tct = int(crane33()[0])*(100/totalct)  # persent of total ct
    v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
    inp_per_Tlt = int(crane33()[1])*(100/totallt)  # persent of total lt
    v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt

    showlt3["text"] = crane33()[0]
    showct3["text"] = crane33()[1]

    canvas.move(c3, v_o_per_lt - c3_previous_lt, v_o_per_ct - c3_previous_ct)
    canvas.move(c_l3_1, v_o_per_lt - c3_previous_lt, 0)
    canvas.move(c_l3_2, v_o_per_lt - c3_previous_lt, 0)
    canvas.move(t3, v_o_per_lt - c3_previous_lt, v_o_per_ct - c3_previous_ct)
    canvas.move(ctl3, 0, v_o_per_ct - c3_previous_ct)
    c3_previous_ct = v_o_per_ct
    c3_previous_lt = v_o_per_lt
    window.after(100,func_for_c33)
    #window.mainloop()

# 4
showlt4 = tk.Label(inframe2_fr2, )
showct4 = tk.Label(inframe2_fr2, )
showlt4.grid(row=2, column=4)
showct4.grid(row=2, column=5)

c4_previous_lt = 0
c4_previous_ct = 0


def func_for_c34():
    global c4_previous_lt, c4_previous_ct
    inp_per_Tct = int(crane34()[0])*(100/totalct)  # persent of total ct
    v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
    inp_per_Tlt = int(crane34()[1])*(100/totallt)  # persent of total lt
    v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt

    showlt4["text"] = crane34()[0]
    showct4["text"] = crane34()[1]

    canvas.move(c4, v_o_per_lt - c4_previous_lt, v_o_per_ct - c4_previous_ct)
    canvas.move(c_l4_1, v_o_per_lt - c4_previous_lt, 0)
    canvas.move(c_l4_2, v_o_per_lt - c4_previous_lt, 0)
    canvas.move(t4, v_o_per_lt - c4_previous_lt, v_o_per_ct - c4_previous_ct)
    canvas.move(ctl4, 0, v_o_per_ct - c4_previous_ct)

    c4_previous_ct = v_o_per_ct
    c4_previous_lt = v_o_per_lt
    window.after(100,func_for_c34)
    #window.mainloop()



c31thread =threading.Thread(target = func_for_c31())
c31thread.daemon = True
c31thread.start()

c32thread =threading.Thread(target = func_for_c32())
c32thread.daemon = True
c32thread.start()

c33thread =threading.Thread(target = func_for_c33())
c33thread.daemon = True
c33thread.start()

c34thread =threading.Thread(target = func_for_c34())
c34thread.daemon = True
c34thread.start()


window.mainloop()


