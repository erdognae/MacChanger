import random
import subprocess
import re
import time

karakter=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

nmac=""

for i in range(12):
    nmac=nmac+random.choice(karakter)
    
resultss= subprocess.run("ifconfig eth0",stdout=subprocess.PIPE,shell=True,text=True)
#print(resultss.stdout)

oldmac= re.search("ether (.*?)txqueuelen",resultss.stdout).group(1).strip() # burda bilgisayarın mac dğeiştirilmeden önceki mac adresi çekilir

subprocess.check_output("ifconfig eth0 down",shell=True)
time.sleep(2)
subprocess.check_output("ifconfig eth0 hw ether "+nmac,shell=True) # newmac adresi eklenir ve aşağıdan NIC tekrar ayağa kaldırılır
time.sleep(2)
subprocess.check_output("ifconfig eth0 up",shell=True)
time.sleep(1)


print("Eski Mac:", oldmac,"Yeni Mac:",nmac, "olarak değiştirildi.")
