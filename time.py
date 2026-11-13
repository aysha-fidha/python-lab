class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        sec = self.__second+other.__second
        minu=self.__minute+other.__minute+sec //60
        hr=self.__hour+other.__hour+minu//60
        return Time(hr%24,minu%60,sec%60)
    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")
t1=Time(10,40,30)
t2=Time(2,50,45)
t3=t1+t2
t3.display()
