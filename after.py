
def function1():
    #found the lt/ct
    count = co1()
    #check the lt/ct
    print("func1",count)
    if count <= 3:
        #send appropriate ip and label for playing video
        mp = threading.Thread(target= typing, args=(label1,"100"))
        mp.start()
    if count >3:
        mp = threading.Thread(target= typing, args=(label1,"103"))
        mp.start()
    root.after(2000,function1)
    

#for other crane
# def function2():
#     count = co2()
#     print("func2",count)
#     if count <= 7:
#         typing(label2,"104")
#     if count >7:
#         typing(label2,"105")
#     root.after(2000,function2)
###########
function1()
#function2()
###########
root.mainloop()

#after every certain second cheack for crane data 
#if crane data found then check which camera to be switch
#according to lt or ct camera need to switch 













# thread = threading.Thread(target=typing,args=(label1,ip))
#     thread.daemon = True
#     thread.start()