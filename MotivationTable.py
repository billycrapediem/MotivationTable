import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("Motivation Table  作业动力表")  # 标题
root.geometry("700x680+200+10")  # 大小和位置

#第一行
Label(root, text="   ").grid(row=0,column=0)
Label(root, text="MISSIONS").grid(row=0,column=1)
Label(root, text="DIFFICULTY").grid(row=0,column=2)
Label(root, text="INTEREST LEVEL").grid(row=0,column=3)
Label(root, text="TIME（Minites）").grid(row=0,column=4)

#第二行 
Label(root, text="序  号").grid(row=1,column=0)
Label(root, text="作业任务").grid(row=1,column=1)
Label(root, text="作业难易程度").grid(row=1,column=2)
Label(root, text="作业兴趣度").grid(row=1,column=3)
Label(root, text="完成作业所需时间（分钟）").grid(row=1,column=4)

#作业序号
Label(root, text="  第一项作业  ").grid(row=2,column=0)
Label(root, text="  第二项作业  ").grid(row=3,column=0)
Label(root, text="  第三项作业  ").grid(row=4,column=0)
Label(root, text="  第四项作业  ").grid(row=5,column=0)
Label(root, text="  第五项作业  ").grid(row=6,column=0)
Label(root, text="  第六项作业  ").grid(row=7,column=0)
Label(root, text="  第七项作业  ").grid(row=8,column=0)
Label(root, text="  第八项作业  ").grid(row=9,column=0)
Label(root, text="  第九项作业  ").grid(row=10,column=0)
Label(root, text="  第十项作业  ").grid(row=11,column=0)


tasklist= [" "]*10
dd=[" "]*10
d=[0]*10
inst=[" "]*10
instt=[0]*10
t=[" "]*10
templist=[]
list=[]

#任务
task1 = tk.Entry(root)
task1.grid(row=2,column=1,sticky=W)
task2 = tk.Entry(root)
task2.grid(row=3,column=1,sticky=W)
task3 = tk.Entry(root)
task3.grid(row=4,column=1,sticky=W)
task4 = tk.Entry(root)
task4.grid(row=5,column=1,sticky=W)
task5 = tk.Entry(root)
task5.grid(row=6,column=1,sticky=W)
task6 = tk.Entry(root)
task6.grid(row=7,column=1,sticky=W)
task7 = tk.Entry(root)
task7.grid(row=8,column=1,sticky=W)
task8 = tk.Entry(root)
task8.grid(row=9,column=1,sticky=W)
task9 = tk.Entry(root)
task9.grid(row=10,column=1,sticky=W)
task10 = tk.Entry(root)
task10.grid(row=11,column=1,sticky=W)




#作业难度
diff1 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff1.grid(row=2,column=2)
diff2 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff2.grid(row=3,column=2)
diff3 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff3.grid(row=4,column=2)
diff4 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff4.grid(row=5,column=2)
diff5 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff5.grid(row=6,column=2)
diff6 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff6.grid(row=7,column=2)
diff7 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff7.grid(row=8,column=2)
diff8 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff8.grid(row=9,column=2)
diff9 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff9.grid(row=10,column=2)
diff10 = tk.Spinbox(root,justify='center',values=("非常容易","比较容易","一般","比较难","非常难"))
diff10.grid(row=11,column=2)


#作业兴趣度
interest1 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest1.grid(row=2,column=3)
interest2 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest2.grid(row=3,column=3)
interest3 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest3.grid(row=4,column=3)
interest4 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest4.grid(row=5,column=3)
interest5 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest5.grid(row=6,column=3)
interest6 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest6.grid(row=7,column=3)
interest7 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest7.grid(row=8,column=3)
interest8 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest8.grid(row=9,column=3)
interest9 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest9.grid(row=10,column=3)
interest10 = tk.Spinbox(root,justify='center',values=("我喜欢","一般","我不喜欢"))
interest10.grid(row=11,column=3)

#作业消耗时间
time1 = tk.Entry(root)
time1.grid(row=2,column=4)
time2 = tk.Entry(root)
time2.grid(row=3,column=4)
time3 = tk.Entry(root)
time3.grid(row=4,column=4)
time4 = tk.Entry(root)
time4.grid(row=5,column=4)
time5 = tk.Entry(root)
time5.grid(row=6,column=4)
time6 = tk.Entry(root)
time6.grid(row=7,column=4)
time7 = tk.Entry(root)
time7.grid(row=8,column=4)
time8 = tk.Entry(root)
time8.grid(row=9,column=4)
time9 = tk.Entry(root)
time9.grid(row=10,column=4)
time10 = tk.Entry(root)
time10.grid(row=11,column=4)



def gettask():
    
    tasklist[0]=task1.get()
    tasklist[1]=task2.get()
    tasklist[2]=task3.get()
    tasklist[3]=task4.get()
    tasklist[4]=task5.get()
    tasklist[5]=task6.get()
    tasklist[6]=task7.get()
    tasklist[7]=task8.get()
    tasklist[8]=task9.get()
    tasklist[9]=task10.get()
    
    
    dd[0]=diff1.get()
    dd[1]=diff2.get()
    dd[2]=diff3.get()
    dd[3]=diff4.get()
    dd[4]=diff5.get()
    dd[5]=diff6.get()
    dd[6]=diff7.get()
    dd[7]=diff8.get()
    dd[8]=diff9.get()
    dd[9]=diff10.get()

    inst[0]=interest1.get()
    inst[1]=interest2.get()
    inst[2]=interest3.get()
    inst[3]=interest4.get()
    inst[4]=interest5.get()
    inst[5]=interest6.get()
    inst[6]=interest7.get()
    inst[7]=interest8.get()
    inst[8]=interest9.get()
    inst[9]=interest10.get()
    
    t[0]=time1.get()
    t[1]=time2.get()
    t[2]=time3.get()
    t[3]=time4.get()
    t[4]=time5.get()
    t[5]=time6.get()
    t[6]=time7.get()
    t[7]=time8.get()
    t[8]=time9.get()
    t[9]=time10.get()


    for i in range(10):
        if (dd[i]=="非常难"):
            d[i]=1
        elif (dd[i]=="比较难"):
            d[i]=2
        elif (dd[i]=="一般"):
            d[i]=3
        elif (dd[i]=="比较容易"):
            d[i]=4
        else :
            d[i]=5

    for i in range(10):
        if (inst[i]=="我喜欢"):
            instt[i]=3
        elif (inst[i]=="一般"):
            instt[i]=2
        else :
            instt[i]=1
            
    for i in range(10):
        templist=[]
        if (tasklist[i].find("*")==-1):
            templist.append(tasklist[i])
            templist.append(d[i])
            templist.append(instt[i])
            templist.append(int(t[i]))
            list.append(templist)
            tasknum=i+1
        else :
            tasknum=i
            break

    list.sort(key=lambda s:s[3])              
    list.sort(key=lambda s:s[2],reverse=TRUE)
    list.sort(key=lambda s:s[1],reverse=TRUE) 

    
    #x=PrettyTable(["作业序号","作业任务","耗时（分钟）"])
    #for i in range(tasknum):
     #   x.add_row([i+1,list[i][0],list[i][3]])
        
    #print(x)
    Label(root, text="          ").grid(row=38,column=1)
    Label(root, text="          ").grid(row=39,column=1)
    Label(root, text="作 业 任 务 表 TO-DO LIST").grid(row=40,column=2)
    Label(root, text="-------------").grid(row=41,column=1)
    Label(root, text="-------------").grid(row=41,column=2)
    Label(root, text="-------------").grid(row=41,column=3)
    Label(root, text="作业序号").grid(row=42,column=1)
    Label(root, text="作业任务").grid(row=42,column=2)
    Label(root, text="时间（分钟）").grid(row=42,column=3)



    for i in range(tasknum):
        j=43+i
        Label(root, text=str(i+1)).grid(row=j,column=1)
        Label(root, text=list[i][0]).grid(row=j,column=2)
        Label(root, text=str(list[i][3])).grid(row=j,column=3)
        
   
Label(root, text="       ").grid(row=18,column=1)

Label(root, text=" 注意：如果您的作业任务").grid(row=19,column=1)
Label(root, text=" 不足十项，请在最后作业的").grid(row=19,column=2)
Label(root, text=" 下一项作业任务中填入 * 。").grid(row=19,column=3)
Label(root, text="       ").grid(row=20,column=1)
btn1=tk.Button(text='提  交',command=gettask)
btn1.grid(row=21,column=2)


# Label(root, text="学业时间表").grid(row=20,column=0)
root.mainloop()
