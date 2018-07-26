#!/usr/bin/python
import os
import time

def run(cmd):
        print (cmd)
	os.system(cmd)

def work_1():
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')

def work_2():
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')

def work_4():
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')
	os.system('start-stop-daemon --background --exec /home/pi/tfm/a.py --start')

def kill_work():
        run('start-stop-daemon --name a.py --stop')


def to_600MHz():
	os.system('sudo cpufreq-set -r -g userspace')
	os.system('sudo cpufreq-set -r -f 600MHz')

def to_1400MHz():
	os.system('sudo cpufreq-set -r -g userspace')
	os.system('sudo cpufreq-set -r -f 1.4GHz')


while(True):
	#Raspi      R3   R1   R5    R6   R2   R4
	#work 0:    O    O    O     O    O    O
	#work 1:    X    O    X     X    O    O
	#work 2:    X    O    X     O    O    X
	#work 3:    X    O    X     O    O    O

	#work 4:    X    O    O     X    O    X
	#work 5:    O    O    X     X    O    O
	#work 6:    X    O    O     O    O    X
	#work 7:    O    O    X     O    O    O

	#work 8:    O    O    X     X    O    X
	#work 9:    X    O    O     X    O    O
	#work 10:   O    O    X     O    O    X
	#work 11:   X    O    O     O    O    O

	#work 12:   X    O    X     X    O    X
	#work 13:   O    O    O     X    O    O
	#work 14:   O    O    O     O    O    X
	#work 15:   O    O    O     X    O    X

	#CPU to 600 MHz
	to_600MHz()

	#work 0 - 35 min
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_4()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90)

	#work 1 - 30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 2  -  40 min
	time.sleep(2400) 


	#work 3  -  35 min
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_4()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90)

	#work 4 - 35 min
	time.sleep(2100) 


	#work 5 - 30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 6  -  40 min
	time.sleep(2400) 

	#work 7  -  35 min
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_4()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90)

	#work 8 - 35 min
	time.sleep(2100) 


	#work 9 - 30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 10  -  40 min

	time.sleep(2400) 


	#work 11  -  35 min
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_4()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90)

	#work 12 - 35 min
	time.sleep(2100) 


	#work 13 - 30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 14  -  40 min
	time.sleep(2400) 


	#work 15  -  35 min
	time.sleep(2100)


	#Raspi      R3   R1   R5    R6   R2   R4
	#work 0:    O    O    O     O    O    O
	#work 1:    X    O    X     X    O    O
	#work 2:    X    O    X     O    O    X
	#work 3:    O    O    O     X    O    O

	#work 4:    O    O    X     O    O    O
	#work 5:    X    O    O     O    O    X
	#work 6:    X    O    O     X    O    O
	#work 7:    X    O    O     X    O    X

	#work 8:    O    O    X     X    O    X
	#work 9:    O    O    X     X    O    O
	#work 10:   O    O    X     O    O    X
	#work 11:   X    O    X     O    O    O

	#work 12:   O    O    O     X    O    X
	#work 13:   X    O    O     O    O    O
	#work 14:   O    O    O     O    O    X
	#work 15:   X    O    X     X    O    X

	#CPU to 1.4 GHz 
	to_1400MHz()

	#work 0  -  40 min
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_4()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120)  

	#work 1  -  30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 2  -  35 min
	time.sleep(2100)

	#work 3  -  40 min
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_4()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 

	#work 4  -  40 min
 	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_4()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120)

	#work 5  -  30 min
	time.sleep(2400)

	#work 6  -  35 min
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_4()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_2()
	time.sleep(330) 
	kill_work()
	time.sleep(90) 
	work_1()
	time.sleep(330) 
	kill_work()
	time.sleep(90)

	#work 7  -  40 min
	time.sleep(2400)

	#work 8  -  40 min
	time.sleep(2400) 

	#work 9  -  30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 10  -  35 min
	time.sleep(2100)

	#work 11  -  40 min
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_4()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_2()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work_1()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 

	#work 12  -  40 min
	time.sleep(2400) 

	#work 13  -  30 min
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_4()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_2()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work_1()
	time.sleep(300) 
	kill_work()
	time.sleep(60)	

	#work 14  -  35 min
	time.sleep(2100)

	#work 15  -  40 min
	time.sleep(2400)



