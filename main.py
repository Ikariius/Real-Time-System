from task1 import * 
from task2 import *
from scheduler import *
import time

scheduler = Scheduler()
scheduler.SCH_Init()

task1 =Task1()
task2 =Task2()

scheduler.SCH_Add_Task(task1.Task1_Run,1000,2000)
scheduler.SCH_Add_Task(task2.Task2_Run,2000,4000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)