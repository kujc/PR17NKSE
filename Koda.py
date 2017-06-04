from csv import DictReader
import pandas as pa

def fileReaderSmucNesrece():
    fp = open("evidencanesrecnasmuciscihV1.csv", "rt", encoding=" utf -8 ")
    reader = DictReader(fp)
    return [line for line in reader]

SmucNes = fileReaderSmucNesrece()
SmucNes = pa.DataFrame(SmucNes)
titles = []

for i in SmucNes:
    titles.append(i)


def tf(t):  #naredi Da/Ne v True/False
    st = 0
    for i in SmucNes[t]:
        if i == 'Da':
            SmucNes.set_value(st, t, "True")
        elif i == "Ne":
            SmucNes.set_value(st, t, "False")
        else:
            SmucNes.set_value(st, t, "")
        st += 1


def optimize():  #klici vseh optimizacij

    num = [3, 4, 5, 13, 14, 15]
    for i in num:
        tf(titles[i])    #vse stolpce z Da/Ne  spremeni z metodo tf()

    num2 = [9, 16, 17, 19, 20]
    for i in num2:
        udA(titles[i])

    timeInterval(titles[2]) # čas
    temperatura(titles[18]) # temperatura


def udA(t):    #Polja imajo število na začetku vrstice , metoda pusti samo številke in se znebi vsega ostalega
    dic = {}
    temp = []  #ustvari seznam če bo split našel samo 1 vredno da bo še vedno seznam
    st = 0
    for i in SmucNes[t]:
        if len(i) > 0:
            temp = i.split(" ", 1)
            if temp[0] not in dic:
                if temp[0] == 25:  #posebna vrednost v enem stolpcu "10.vzrok" id =9
                    dic[25] = 'ostalo'
                elif temp[0] == 'NOÈNA':  # vrenem id=16
                    dic[7] = 'Nocna'
                else:
                    if len(temp) > 1:
                        dic[temp[0]] = temp[1]

            if temp[0].isdigit():
                SmucNes.set_value(st, t, temp[0])
            else:
                for i in dic:
                    if temp[0] == dic[i]:
                        SmucNes.set_value(st, t, i)
                SmucNes.set_value(st, t, "")
        else:
            SmucNes.set_value(st, t, "")

        st += 1


def timeInterval(t): #Daj čas na intervale 30min

    temp = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30",
          "03:00", "03:30", "04:00", "04:30", "05:00", "05:30",
          "06:00", "06:30", "07:00", "07:30", "08:00", "08:30",
          "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
          "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
          "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
          "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
          "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
    st = 0
    for d in SmucNes[t]:
        if len(d) > 0:
            s = d.split(":")
            s[0] = int(s[0])
            s[1] = int(s[1])
            i = s[0]*2
            if s[1] >= 30:
                i += 1
            SmucNes.set_value(st, t, temp[i])
        st += 1


def temperatura(t): #Odstrani temperature nad 40 in pod 40
    st=0
    for i in SmucNes[t]:
        if len(i) > 0 and (int(i) > 40 or int(i) < -40):
            SmucNes.set_value(st, t, None)
        st += 1


def zapisidat():
    SmucNes.to_csv("Output.csv")

