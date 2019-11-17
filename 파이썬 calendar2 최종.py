import calendar
import tkinter as tk
from inspect import v
from tkinter import *
from datetime import datetime
import tkinter.messagebox
import csv
#import pandas as pd csv파일 이용시 사용하는 라이브러리
from korean_lunar_calendar import KoreanLunarCalendar #음력이용시 사용하는 패키지


now = datetime.now()

calendarWindow = tk.Tk()  # TK달력 화면만들기.
calendarWindow.title("달력")




class calendar1:  # 달력그리기 클래스
    def __init__(self):
        self.year = now.year
        self.month = now.month
        self.setup(self.year, self.month)
        
    weekDay = ("일", "월", "화", "수", "목", "금", "토")  # 요일들  tuple 자료형식
    setname={"허윤미","달력"}#set 자료형식
    season={1:'겨울',2:'겨울',3:'봄',4:'봄',5:'봄',6:'여름',7:'여름',8:'여름',9:'가을',10:'가을',11:'겨울',12:'겨울'}#dictionary 자료형식

    def clear(self):#화면 내용지우기
        mylist = calendarWindow.grid_slaves()
        for i in mylist:
            i.destroy()

    def prevF(self):#이전달로 이동하는 버튼
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        self.clear()
        self.setup(self.year,self.month)
        print("이전버튼")
    def nexF(self):#다음달로 이동하는 버튼
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1
        self.clear()
        self.setup(self.year, self.month)
        print("이후버튼")
        
    def csvf(self):  # csv파일내용 쉘 통해서 보여주는 버튼
        self.f = open('D:\\birthdayfile.CSV', 'r')
        self.lines = csv.reader(self.f)
        i=0
        for line1 in self.lines:
            if i > 2 and i < 30:
                print(line1)
            i+=1

    def setup (self,year,month):
        rangeLength = calendar.monthrange(year, month)  # 월의 끝날 구하기.tuple 자료형식"<class 'tuple'>"
    # frame을 2개로 나누어서 관리 위에는 사진 아래는 날짜
        frame1 = tk.Frame(calendarWindow)
        frame1.grid(row=0)
        frame2 = tk.Frame(calendarWindow)
        frame2.grid(row=1)

    # frame1에 이미지 넣기
        photo = PhotoImage(file="D:\\teddy.gif")
        w = Label(frame1, image=photo)
        w.grid(row=0)

        prevM = Button(frame2, text="이전달", fg="blue", font="Times 10 bold",command=self.prevF,width=5).grid(row=0,column=1)#이전달 버튼
        tk.Label(frame2, text=(year), fg = "red",font = "Times 12 bold").grid(row=0,column=0) #연 표시
        tk.Label(frame2, text=(month), fg="red", font="Times 15 bold").grid(row=0, column=3) #월 표시
        nextM = Button(frame2, text="다음달", fg="blue", font="Times 10 bold",command=self.nexF,width=5).grid(row=0,column=5)#다음달 버튼
        showCsv = Button(frame2, text="SHOW", fg="orange", font="Times 10 bold", command=self.csvf, width=5).grid(row=0,
                                                                                                           column=6)  # csv파일 보여주는 버튼

        list=[]

        i=0
        for val1, weekbutton in enumerate(self.weekDay):#요일그리기
            tk.Button(frame2, text=self.weekDay[val1],fg='green',width=5).grid(row=2,column=i)
            i+=1

        count=1
        rows=2
        columns=0
        sum=rangeLength[1] + rangeLength[0]+1
        # print(sum)
        if(sum==38):
            sum=31
        ccc=rangeLength[0]
        v = tk.IntVar()
        lunarCalendar=KoreanLunarCalendar()

        def dateButtonF():
            self.f = open('D:\\birthdayfile.CSV', 'r')
            self.lines = csv.reader(self.f)
            
            print("버튼함수, 버튼에 해당하는 날짜는 " + str(v.get()))
            lunarCalendar.setSolarDate(self.year,self.month,v.get())
            print("음력날짜는: "+lunarCalendar.LunarIsoFormat())
            
            i = 0
            birlist=[]
            for line in self.lines:
                if i>2 and i < 30:
                    if (int(line[3])%100==int(v.get()) and (int(line[3])%10000-int(line[3])%100)/100==self.month):
                        birlist.append(str(line[1]))
                i+=1
            tk.messagebox.showinfo("음력날짜",('클릭한 날짜의 음력\n',lunarCalendar.LunarIsoFormat(),'\n생일인 사람 수와 이름\n',birlist,len(birlist),'명'))
            
            
            
            

        # 날짜그리기
        for startDate in range(sum):
            if (startDate % 7 == 0):
                rows = rows + 1
            if(startDate<=ccc and ccc!=6):
                tk.Button(frame2,text=" ",width=5,height=2).grid(row=rows,column=columns)
            else:
                tk.Radiobutton(frame2, text=count,command=dateButtonF,indicatoron=0,variable=v,value=count,width=5,height=2).grid(row=rows,column=columns)
                count=count+1
            columns+=1
            if(columns==7):
                columns=0

        namecard=tk.Label(frame1,text=self.setname,fg="red", font="Times 7 bold").grid(row=1)
        seasoncard=tk.Label(frame1,text=self.season.get(month),fg='pink',font="Time 15 bold").grid(row=2)


        calendarWindow.mainloop()
        self.f.close()



calendar1()
