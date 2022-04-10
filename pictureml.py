from array import *
import os
#writed by Tolunay Nehir


def x6ai_compare(file,model):
    mylist=[]
    mylist2=[]
    sonuclist=[]
    sonuclist2=[]
    sonuc=0
    sonuc2=0
    f = open(file, "r")
    m = open(model, "r")
    a=0
    b=0
    c=0
    d=0
    while(a<6):
        mc=m.readline()
        geciciarr=mc.split()
        #print(geciciarr)
        mylist.append(geciciarr)
        a=a+1
    #print(arr)
    print(mylist)
    while(b<6):
        fc=f.readline()
        geciciarr=fc.split(",")
        #print(geciciarr)
        mylist2.append(geciciarr)
        b=b+1
    print(mylist2)
    a=0
    while(a<6):
        sonuclist.append(int(mylist[a][0])*int(mylist2[a][0]))
        a=a+1
    print(sonuclist)
    while(c<6):
        sonuc+=sonuclist[c]
        c=c+1
    sonuc=sonuc/6
    b=0
    while(b<6):
        sonuclist2.append(int(mylist[b][1])*int(mylist2[b][1]))
        b=b+1
    print(sonuclist2)
    while(d<6):
        sonuc2+=sonuclist[d]
        d=d+1
    sonuc2=sonuc2/6
    print("Sonuc:")
    print(str((sonuc+sonuc2)/2))
        
    
    
    
        
    


def x12ai_compare(file,model):
    mylist=[]
    mylist2=[]
    sonuclist=[]
    sonuclist2=[]
    sonuc=0
    sonuc2=0
    f = open(file, "r")
    m = open(model, "r")
    a=0
    b=0
    c=0
    d=0
    while(a<12):
        mc=m.readline()
        geciciarr=mc.split()
        #print(geciciarr)
        mylist.append(geciciarr)
        a=a+1
    #print(arr)
    print(mylist)
    while(b<12):
        fc=f.readline()
        geciciarr=fc.split(",")
        #print(geciciarr)
        mylist2.append(geciciarr)
        b=b+1
    print(mylist2)
    a=0
    while(a<12):
        sonuclist.append(int(mylist[a][0])*int(mylist2[a][0]))
        a=a+1
    print(sonuclist)
    while(c<12):
        sonuc+=sonuclist[c]
        c=c+1
    sonuc=sonuc/12
    b=0
    while(b<12):
        sonuclist2.append(int(mylist[b][1])*int(mylist2[b][1]))
        b=b+1
    print(sonuclist2)
    while(d<12):
        sonuc2+=sonuclist[d]
        d=d+1
    sonuc2=sonuc2/12
    print("Sonuc:")
    print(str((sonuc+sonuc2)/2))


def x6ai_trainx4(dataset,model):
    m = open(dataset, "r")
    #line
    d1 =[]
    anadizi=[]
    d3=[]
    d4=[]
    d5=[]
    b=0
    while(b<6):
        mc=m.readline()
        geciciarr=mc.split("-")
        d1.append(geciciarr)
        b=b+1
    b=0
    m.readline()
    while(b<6):
        mc=m.readline()
        geciciarr=mc.split("-")
        d3.append(geciciarr)
        b=b+1
    b=0
    m.readline()
    while(b<6):
        mc=m.readline()
        geciciarr=mc.split("-")
        d4.append(geciciarr)
        b=b+1
    b=0
    m.readline()
    while(b<6):
        mc=m.readline()
        geciciarr=mc.split("-")
        d5.append(geciciarr)
        b=b+1
    print(d1)
    for i in range(0, len(d1)):
        gecici1=d1[i]
        gecici2=d3[i]
        gecici3=d4[i]
        gecici4=d5[i]
        anadizi.append(int(gecici1[0])*int(gecici2[0])*int(gecici3[0])*int(gecici4[0]))
        anadizi.append(int(gecici1[1])*int(gecici2[1])*int(gecici3[1])*int(gecici4[1]))
    print(anadizi)
    #print(len(anadizi))
    modelfile =open(model,"w")
    for i in range(0,12,2):
        modelfile.write(str(anadizi[i])+" "+str(anadizi[i+1])+"\n")
    print("Model Olusturuldu")
        
def model_x6(model):
    m = open(model, "w")
    a=0
    while(a<6):
        deger=input(a+".Deger1 giriniz:")
        deger2=input(a+".Deger2 giriniz:")
        m.write(deger+" "+deger2+"\n")
        a=a+1
def model_x12(model):
    m = open(model, "w")
    a=0
    while(a<12):
        deger=input(a+".Deger1 giriniz:")
        deger2=input(a+".Deger2 giriniz:")
        m.write(deger+" "+deger2+"\n")
        a=a+1

def x12ai_trainx4(dataset,model):
    m = open(dataset, "r")
    d1 =[]
    anadizi=[]
    d3=[]
    d4=[]
    d5=[]
    c1=[]
    c3=[]
    c4=[]
    c5=[]
    b=0
    while(b<12):
        mc=m.readline()
        geciciarr=mc.split("-")
        d1.append(geciciarr)
        b=b+1
    b=0
    m.readline()
    while(b<12):
        mc=m.readline()
        geciciarr=mc.split("-")
        d3.append(geciciarr)
        b=b+1
    b=0
    m.readline()
    while(b<12):
        mc=m.readline()
        geciciarr=mc.split("-")
        d4.append(geciciarr)
        b=b+1
    b=0
    m.readline()
    while(b<12):
        mc=m.readline()
        geciciarr=mc.split("-")
        d5.append(geciciarr)
        b=b+1
    #print(d1)
    for i in range(0, len(d1)):
        gecici1=d1[i]
        gecici2=d3[i]
        gecici3=d4[i]
        gecici4=d5[i]
        anadizi.append(int(gecici1[0])*int(gecici2[0])*int(gecici3[0])*int(gecici4[0]))
        anadizi.append(int(gecici1[1])*int(gecici2[1])*int(gecici3[1])*int(gecici4[1]))
    print(anadizi)
    modelfile =open(model,"w")
    for i in range(0,12,2):
        modelfile.write(str(anadizi[i])+" "+str(anadizi[i+1])+"\n")
    #print(len(anadizi))
    print("Model Olusturuldu")
            
            
