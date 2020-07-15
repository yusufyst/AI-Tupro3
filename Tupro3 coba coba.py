# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:03:23 2018

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:19:57 2018

@author: USER
"""
import numpy as np


#code ngebaca data csv
file = np.genfromtxt('Datatupro3.csv',delimiter=',')
file = file[1:,1:]

#Fuzzysifikasi
#FungsibanyakFollowers
def kecilfollowers(followers):
    if (followers<=5000):
        return 1
    elif (followers<=20000):
        return (-(followers-20000)/(20000-5000))
    else:
        return 0

def mediumfollowers(followers):
    if (5000<followers<=20000):
        return ((followers-5000)/(20000-5000))
    elif (20000<followers<=70000):
        return (-(followers-70000)/(70000-20000))
    else:
        return 0

def besarfollowers(followers):
    if (followers<=70000):
        return 0
    elif (followers>90000):
        return 1
    else:
        return ((followers-70000)/(90000-70000))
#Fungsibanyakenggangement
def kecileng(eng):
    if (eng<=3):
        return 1
    elif (eng<5):
        return(-(eng-5)/(5-3))
    else:
        return 0

def mediumeng(eng):
    if (3<eng<=5):
        return (-(eng-3)/(5-3))
    elif (5<eng<7):
        return (-(eng-7)/(7-5))
    else:
        return 0

def besareng(eng):
    if (eng<=7):
        return 0
    elif (eng>9):
        return 1
    else:
        return ((eng-9)/(9-7))
    

kalkulasi = 0
hasil = []


#fungsiterpilih
def terpilihInflcr(kf,mf,bf,ke,me,be):
    terpilih = []
    terpilih.append(0)
    if (kf>0 and be>0):
        tidakTerpilih.append(min(kf,be))
    if (mf>0 and me>0):
        terpilih.append(min(mf,me))
    if (mf>0 and be>0):
        terpilih.append(min(mf,be))
    if (bf>0 and me>0):
        terpilih.append(min(bf,me))
    if (bf>0 and be>0):
        terpilih.append(min(bf,be))
    return max(terpilih)
    terpilih = terpilihInflcr(kf,mf,bf,ke,me,be)
    
#fungsitidakterpilihkadiINFLUENCER
def notTerpilihInflcr(kf,mf,bf,ke,me,be):
    tidakTerpilih = []
    tidakTerpilih.append(0)
    if (kf>0 and ke>0):
        tidakTerpilih.append(min(kf,ke))
    if (mf>0 and ke>0):
        tidakTerpilih.append(min(mf,ke))
    if (bf>0 and ke>0):
        tidakTerpilih.append(min(bf,ke))
    if (kf>0 and me>0):
        tidakTerpilih.append(min(kf,me))
    return max(tidakTerpilih)


for i in range(len(file)):
    followers = file[i][0]
    eng = file[i][1]
    terpilih = []
    tidakTerpilih =[]
    kf=kecilfollowers(followers)
    mf=mediumfollowers(followers)
    bf=besarfollowers(followers)
    ke=kecileng(eng)
    me=mediumeng(eng)
    be=besareng(eng)
    
    terpilih = terpilihInflcr(kf,mf,bf,ke,me,be)
    tidakTerpilih = notTerpilihInflcr(kf,mf,bf,ke,me,be)

#SEGENOinTheSKY
#Defuzytisifikasiasi
    sugenoskuy = ((terpilih*100)+(tidakTerpilih*58))/(terpilih+tidakTerpilih) >58
    if sugenoskuy:
        hasil.append(i+1)
        print("Influencer Terpilih,ialah ke-" + str(i+1))
        kalkulasi = kalkulasi+1
    else:
        print("Tidak Terpilih Jadi Infulencer :(")
print("maka " + str(kalkulasi) + " orang yang terpilih Jadi INFLUENCER")

#saveHasil
np.savetxt('HasilTupro3.csv',hasil, delimiter=',', fmt='%s')
