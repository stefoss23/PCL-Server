import requests
import multiprocessing
import subprocess


def serv():
   subprocess.run(['timeout', '6s', 'python3', 'manage.py', 'runserver'])
   print("--- Server finished")
   
   
p1 = multiprocessing.Process(target=serv)

p1.start()

print("--- Server has started")

p1.join()

print("--- Process finished")
