from distutils.spawn import spawn
import time
#from imutils.video import FileVideoStream
import threading
#import multiprocessing
import tkinter as tk
from PIL import Image, ImageTk
import cv2
#import imageio
from socketClientver2 import crane31,crane32,crane33,crane34,crane11,crane12,crane14,crane15



window = tk.Tk()

win_width = window.winfo_screenwidth()
win_height = window.winfo_screenheight()

# def take_info():
#     global win_width,win_height
#     window.update()
#     win_width = window.winfo_height()
#     win_height = window.winfo_width()
#     print(win_width,win_height)
#     window.after (1000,take_info)

# take = threading.Thread(target = take_info)
# take.daemon = True
# take.start()

window.rowconfigure([0],weight=3)
window.columnconfigure(0,weight=3)
# define outer frame

o_f1_ph = (70/100)*win_height
o_f2_ph = (30/100)*win_height

o_labelfr1 = tk.LabelFrame(window, width=win_width, height=o_f1_ph, )
o_labelfr2 = tk.LabelFrame(window, width=win_width, height=o_f2_ph,)

o_labelfr1.grid(row=0, column=0, sticky='nsew')
o_labelfr2.grid(row=1, column=0, sticky='nsew')
#configure
o_labelfr1.rowconfigure([0,1],weight=1)
o_labelfr1.columnconfigure([0],weight=1)

# frame inside o_labelfr1
infms_fr1h = (47/100)*o_f1_ph

infr1 = tk.LabelFrame(o_labelfr1, width=win_width, height=infms_fr1h )
infr2 = tk.LabelFrame(o_labelfr1, width=win_width, height=infms_fr1h )

infr1.grid(row=0, column=0, sticky="wens")
infr2.grid(row=1, column=0, sticky="wens")

infr1.rowconfigure(0,weight=1)
infr2.rowconfigure(0,weight=1)
infr1.columnconfigure([0,1],weight=1)
infr2.columnconfigure([0,1],weight=1)

# frame inside infr1
fr_infrw = (47/100)*win_width
container1 = tk.LabelFrame(infr1, width=fr_infrw, height=infms_fr1h,text = "CRANE-31", labelanchor='n', bg= "#5f6161", fg="#fff491")
container1.grid(row=0, column=0,sticky="nswe")
container2 = tk.LabelFrame(infr1, width=fr_infrw, height=infms_fr1h,text = "CRANE-32", labelanchor='n', bg= "#5f6161", fg="#fff491")
container2.grid(row=0, column=1,sticky="nswe")

container1.rowconfigure(0,weight=1)
container2.rowconfigure(0,weight=1)
container1.columnconfigure([0,1],weight=1)
container2.columnconfigure([0,1],weight=1)


# frame inside infr2
container3 = tk.LabelFrame(infr2, width=fr_infrw, height=infms_fr1h,text = "CRANE-33", labelanchor='n', bg= "#5f6161", fg="#fff491")
container4 = tk.LabelFrame(infr2, width=fr_infrw, height=infms_fr1h,text = "CRANE-34", labelanchor='n', bg= "#5f6161", fg="#fff491")
container3.grid(row=0, column=0,sticky="nswe")
container4.grid(row=0, column=1,sticky="nswe")

container3.rowconfigure(0,weight=1)
container4.rowconfigure(0,weight=1)
container3.columnconfigure([0,1],weight=1)
container4.columnconfigure([0,1],weight=1)


# frame inside container 1
container_half = (49/100)*fr_infrw#overall video cont. width 
v1 = tk.LabelFrame(container1, width=container_half,
                   height=infms_fr1h)
v2 = tk.LabelFrame(container1, width=container_half,
                   height=infms_fr1h)
v1.grid(row=0, column=0,sticky="nsew")
v2.grid(row=0, column=1,sticky="nsew")

v1.rowconfigure(0,weight=1)
v2.rowconfigure(0,weight=1)
v1.columnconfigure(0,weight=1)
v2.columnconfigure(0,weight=1)


# frame inside container2
v3 = tk.LabelFrame(container2, width=container_half,
                   height=infms_fr1h)
v4 = tk.LabelFrame(container2, width=container_half,
                   height=infms_fr1h)
v3.grid(row=0, column=0,sticky="nsew")
v4.grid(row=0, column=1,sticky="nsew")

v3.rowconfigure(0,weight=1)
v4.rowconfigure(0,weight=1)
v3.columnconfigure(0,weight=1)
v4.columnconfigure(0,weight=1)
# frame inside container3
v5 = tk.LabelFrame(container3, width=container_half,
                   height=infms_fr1h)
v6 = tk.LabelFrame(container3, width=container_half,
                   height=infms_fr1h)
v5.grid(row=0, column=0,sticky="nsew")
v6.grid(row=0, column=1,sticky="nsew")

v5.rowconfigure(0,weight=1)
v6.rowconfigure(0,weight=1)
v5.columnconfigure(0,weight=1)
v6.columnconfigure(0,weight=1)

# frame inside container4
v7 = tk.LabelFrame(container4, width=container_half,
                   height=infms_fr1h)
v8 = tk.LabelFrame(container4, width=container_half,
                   height=infms_fr1h)
v7.grid(row=0, column=0,sticky="nsew")
v8.grid(row=0, column=1,sticky="nsew")

v7.rowconfigure(0,weight=1)
v8.rowconfigure(0,weight=1)
v7.columnconfigure(0,weight=1)
v8.columnconfigure(0,weight=1)
# label for video
video1 = tk.Label(v1,text = "No Video")
video2 = tk.Label(v2,text = "No Video")
video3 = tk.Label(v3,text = "No Video")
video4 = tk.Label(v4,text = "No Video")
video5 = tk.Label(v5,text = "No Video")
video6 = tk.Label(v6,text = "No Video")
video7 = tk.Label(v7,text = "No Video")
video8 = tk.Label(v8,text = "No Video")
video1.grid(sticky="we")
video2.grid(sticky="we")
video3.grid(sticky="we")
video4.grid(sticky="we")
video5.grid(sticky="we")
video6.grid(sticky="we")
video7.grid(sticky="we")
video8.grid(sticky="we")



#:::::::::::::::::::crain moving::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::


window.update()
c_width = window.winfo_width()
c_height = int((20/100)*window.winfo_height())
def canvas_s():
    global c_width, c_height
    window.update()
    c_width = window.winfo_width()
    c_height = (20/100)*window.winfo_height() # here height of canvas controlled
    # one_4_w = c_width/4
    t_marg = 10
    b_marg = 60
    l_marg, r_marg = 10, 90

    lt = int(((r_marg/100)*c_width)-((l_marg/100)*c_width))

    ct = int(((b_marg/100)*c_height)-((t_marg/100)*c_height))

    #  create canvas
    canvas = tk.Canvas(o_labelfr2, width=c_width, height=c_height, bg="#454545")
    canvas.grid(row=0, column=0, sticky="nswe")

    # two parralel lines
    canvas.create_line(((l_marg/100)*c_width), int((t_marg / 100)*c_height),
                    ((r_marg/100)*c_width), int((t_marg / 100)*c_height), width=5, fill="#C19A6B")
    canvas.create_line(((l_marg/100)*c_width), int((b_marg / 100)*c_height),
                    ((r_marg/100)*c_width), int((b_marg / 100)*c_height), width=5, fill="#C19A6B")

    # crain horizontal lines for ct lookup
    ctl31 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="#f1df92", width=1,)

    ctl32 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="#4da6ff", width=1,)

    ctl33 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="#66ff99", width=1,)

    ctl34 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="#ff3333", width=1,)

    ctl11 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="", width=1,)
                            
    ctl12 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="", width=1,)

    ctl14 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="", width=1,)

    ctl15 = canvas.create_line(-3000, ((t_marg / 100)*c_height),
                            3000, ((t_marg / 100)*c_height), fill="", width=1,)

    # crain lines

    c_l31_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#f1df92")
    c_l31_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#f1df92")

    c_l32_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#4da6ff")
    c_l32_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#4da6ff")


    c_l33_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#66ff99")
    c_l33_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#66ff99")

    c_l34_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
    c_l34_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#ff3333")

    c_l11_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
    c_l11_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
        

    c_l12_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
    c_l12_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#ff3333")

    c_l14_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
    c_l14_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#ff3333")


    c_l15_1 = canvas.create_line((l_marg/100)*c_width-15, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width-15, int((b_marg / 100)*c_height), width=3, fill="#ff3333")
    c_l15_2 = canvas.create_line((l_marg/100)*c_width+16, int((t_marg / 100)*c_height),
                            (l_marg/100)*c_width+16, int((b_marg / 100)*c_height), width=3, fill="#ff3333")



    # crain rect
    c31 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#9e8515")

    c32 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#004d99")

    c33 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#009933")

    c34 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#990000")

    c11 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#009933")

    c12 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#009933")

    c14 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#009933")

    c15 = canvas.create_rectangle((l_marg/100)*c_width-18, ((t_marg / 100)*c_height)-8,
                                (l_marg/100)*c_width+18, ((t_marg / 100)*c_height)+8, fill="#009933")



    # Crane Text
    t31 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="1", font="arial 12 bold", fill="white")
    t32 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="2", font="arial 12 bold", fill="white")
    t33 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="3", font="arial 12 bold", fill="white")
    t34 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="4", font="arial 12 bold", fill="white")
    t11 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="1", font="arial 12 bold", fill="white")
    t12 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="1", font="arial 12 bold", fill="white")
    t14 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="1", font="arial 12 bold", fill="white")
    t15 = canvas.create_text((l_marg/100)*c_width, ((t_marg / 100)
                            * c_height), text="1", font="arial 12 bold", fill="white")


    #put ct here when found from server
    ####################################

    totalct = 35
    totallt = 600

    parralel_line_lenght = ((r_marg/100)*c_width)-((l_marg/100)*c_width)
    plldiv4 = ""

    for i in range(ct):
        if i % 10 == 0:
            if i != 0:
                canvas.create_line(((l_marg/100)*c_width)-((5/100)*c_width), i+((t_marg/100)*c_height),
                                ((l_marg/100)*c_width)-((4/100)*c_width), i+((t_marg/100)*c_height), fill="white")

                canvas.create_text(((l_marg/100)*c_width)-((3/100)*c_width), i+((t_marg/100)*c_height),
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
    window.after(2000,canvas_s)

canv = threading.Thread(target = canvas_s)
canv.daemon = True
canv.start()

# # take videos:
url1 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url2 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url3 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url4 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url5 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url6 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url7 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"
url8 = "rtsp://admin:$Admin123@192.168.1.100/cam/realmonitor?channel=1&subtype=1"

def stream(ip,label):
    vid = cv2.VideoCapture(ip)
    while True:
        window.update()
        frwidth = (30/100)*window.winfo_width()
        frheight = (30/100)*(window.winfo_height()-c_height)

        ret, frame = vid.read()
        if ret:
            width = frame.shape[1]
            height = frame.shape[0]
            per_width = frwidth*(100/width)
            per_height = frheight*(100/height)
            if width > height:
                frame = cv2.resize(frame,(int(frwidth),int((per_height/100)*height)))
            else:
                frame = cv2.resize(frame,((per_width/100)*width),frheight)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image = img)
            label.configure(image= img) 
            label.image = img
        

thread1 = threading.Thread(target=stream, args=[url1, video1])
thread2 = threading.Thread(target=stream, args=[url2, video2])
thread3 = threading.Thread(target=stream, args=[url3, video3])
thread4 = threading.Thread(target=stream, args=[url4, video4])
thread5 = threading.Thread(target=stream, args=[url5, video5])
thread6 = threading.Thread(target=stream, args=[url6, video6])
thread7 = threading.Thread(target=stream, args=[url7, video7])
thread8 = threading.Thread(target=stream, args=[url8, video8])


thread1.daemon = 1
thread2.daemon = 2
thread3.daemon = 3
thread4.daemon = 4
thread5.daemon = 5
thread6.daemon = 6
thread7.daemon = 7
thread8.daemon = 8

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()


# # 31

# c31_previous_lt = 0
# c31_previous_ct = 0


# def func_for_c31():
#     global c31_previous_lt, c31_previous_ct
#     inp_per_Tct = int(crane31()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane31()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c31, v_o_per_lt - c31_previous_lt, v_o_per_ct - c31_previous_ct)
#     canvas.move(c_l31_1, v_o_per_lt - c31_previous_lt, 0)
#     canvas.move(c_l31_2, v_o_per_lt - c31_previous_lt, 0)
#     canvas.move(t31, v_o_per_lt - c31_previous_lt, v_o_per_ct - c31_previous_ct)
#     canvas.move(ctl31, 0, v_o_per_ct - c31_previous_ct)
#     c31_previous_ct = v_o_per_ct
#     c31_previous_lt = v_o_per_lt

#   


# # 32

# c32_previous_lt = 0
# c32_previous_ct = 0


# def func_for_c32():
#     global c32_previous_lt, c32_previous_ct
#     inp_per_Tct = int(crane32()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane32()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c32, v_o_per_lt - c32_previous_lt, v_o_per_ct - c32_previous_ct)
#     canvas.move(c_l32_1, v_o_per_lt - c32_previous_lt, 0)
#     canvas.move(c_l32_2, v_o_per_lt - c32_previous_lt, 0)
#     canvas.move(t32, v_o_per_lt - c32_previous_lt, v_o_per_ct - c32_previous_ct)
#     canvas.move(ctl32, 0, v_o_per_ct - c32_previous_ct)

#     c32_previous_ct = v_o_per_ct
#     c32_previous_lt = v_o_per_lt
#     

# # 33

# c33_previous_lt = 0
# c33_previous_ct = 0


# def func_for_c33():
#     global c33_previous_lt, c33_previous_ct
#     inp_per_Tct = int(crane33()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane33()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c33, v_o_per_lt - c33_previous_lt, v_o_per_ct - c33_previous_ct)
#     canvas.move(c_l33_1, v_o_per_lt - c33_previous_lt, 0)
#     canvas.move(c_l33_2, v_o_per_lt - c33_previous_lt, 0)
#     canvas.move(t33, v_o_per_lt - c33_previous_lt, v_o_per_ct - c33_previous_ct)
#     canvas.move(ctl33, 0, v_o_per_ct - c33_previous_ct)
#     c33_previous_ct = v_o_per_ct
#     c33_previous_lt = v_o_per_lt
#     

# # 34

# c34_previous_lt = 0
# c34_previous_ct = 0


# def func_for_c34():
#     global c34_previous_lt, c34_previous_ct
#     inp_per_Tct = int(crane34()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane34()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c34, v_o_per_lt - c34_previous_lt, v_o_per_ct - c34_previous_ct)
#     canvas.move(c_l34_1, v_o_per_lt - c34_previous_lt, 0)
#     canvas.move(c_l34_2, v_o_per_lt - c34_previous_lt, 0)
#     canvas.move(t34, v_o_per_lt - c34_previous_lt, v_o_per_ct - c34_previous_ct)
#     canvas.move(ctl34, 0, v_o_per_ct - c34_previous_ct)

#     c34_previous_ct = v_o_per_ct
#     c34_previous_lt = v_o_per_lt
#    


# # 11

# c11_previous_lt = 0
# c11_previous_ct = 0


# def func_for_c11():
#     global c11_previous_lt, c11_previous_ct
#     inp_per_Tct = int(crane11()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane11()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c11, v_o_per_lt - c11_previous_lt, v_o_per_ct - c11_previous_ct)
#     canvas.move(c_l11_1, v_o_per_lt - c11_previous_lt, 0)
#     canvas.move(c_l11_2, v_o_per_lt - c11_previous_lt, 0)
#     canvas.move(t11, v_o_per_lt - c11_previous_lt, v_o_per_ct - c11_previous_ct)
#     canvas.move(ctl11, 0, v_o_per_ct - c11_previous_ct)

#     c11_previous_ct = v_o_per_ct
#     c11_previous_lt = v_o_per_lt
#     


# # 12

# c12_previous_lt = 0
# c12_previous_ct = 0


# def func_for_c12():
#     global c12_previous_lt, c12_previous_ct
#     inp_per_Tct = int(crane12()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane12()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c12, v_o_per_lt - c12_previous_lt, v_o_per_ct - c12_previous_ct)
#     canvas.move(c_l12_1, v_o_per_lt - c12_previous_lt, 0)
#     canvas.move(c_l12_2, v_o_per_lt - c12_previous_lt, 0)
#     canvas.move(t12, v_o_per_lt - c12_previous_lt, v_o_per_ct - c12_previous_ct)
#     canvas.move(ctl12, 0, v_o_per_ct - c12_previous_ct)

#     c12_previous_ct = v_o_per_ct
#     c12_previous_lt = v_o_per_lt
#     

# # 14

# c14_previous_lt = 0
# c14_previous_ct = 0


# def func_for_c14():
#     global c14_previous_lt, c14_previous_ct
#     inp_per_Tct = int(crane14()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane14()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c14, v_o_per_lt - c14_previous_lt, v_o_per_ct - c14_previous_ct)
#     canvas.move(c_l14_1, v_o_per_lt - c14_previous_lt, 0)
#     canvas.move(c_l14_2, v_o_per_lt - c14_previous_lt, 0)
#     canvas.move(t14, v_o_per_lt - c14_previous_lt, v_o_per_ct - c14_previous_ct)
#     canvas.move(ctl14, 0, v_o_per_ct - c14_previous_ct)

#     c14_previous_ct = v_o_per_ct
#     c14_previous_lt = v_o_per_lt
#     

# # 15

# c15_previous_lt = 0
# c15_previous_ct = 0


# def func_for_c15():
#     global c15_previous_lt, c15_previous_ct
#     inp_per_Tct = int(crane15()[0])*(100/totalct)  # persent of total ct
#     v_o_per_ct = (inp_per_Tct/100)*ct  # inp_per % of ct
#     inp_per_Tlt = int(crane15()[1])*(100/totallt)  # persent of total lt
#     v_o_per_lt = (inp_per_Tlt/100)*lt  # inp_per % of lt


#     canvas.move(c15, v_o_per_lt - c15_previous_lt, v_o_per_ct - c15_previous_ct)
#     canvas.move(c_l15_1, v_o_per_lt - c15_previous_lt, 0)
#     canvas.move(c_l15_2, v_o_per_lt - c15_previous_lt, 0)
#     canvas.move(t15, v_o_per_lt - c15_previous_lt, v_o_per_ct - c15_previous_ct)
#     canvas.move(ctl15, 0, v_o_per_ct - c15_previous_ct)

#     c15_previous_ct = v_o_per_ct
#     c15_previous_lt = v_o_per_lt
#     




















# c31thread =threading.Thread(target = func_for_c31())
# c31thread.daemon = True
# c31thread.start()

# c32thread =threading.Thread(target = func_for_c32())
# c32thread.daemon = True
# c32thread.start()

# c33thread =threading.Thread(target = func_for_c33())
# c33thread.daemon = True
# c33thread.start()

# c34thread =threading.Thread(target = func_for_c34())
# c34thread.daemon = True
# c34thread.start()


window.mainloop()


