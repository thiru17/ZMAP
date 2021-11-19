import asyncio
from time import time, sleep
import os, sys


async def scan1(p):
  
  proc = await asyncio.create_subprocess_exec(
     'zmap','-p',str(p),'164.68.126.176','-o',str(p),
     stdout=asyncio.subprocess.PIPE,
     stderr=asyncio.subprocess.PIPE)
  #print ("_____port no : {0}  scan completed_____".format(p))

def scan2():
  global list1
  list1 = []
  #sleep(1)
  for a in range(1,65535):
    if (os.path.isfile("{}".format(a)) == True):
      if (os.stat(str(a)).st_size != 0):
        list1.append(a)
        os.remove(str(a))
      else:
        os.remove(str(a))
  #print (list1)


def scan0():
    for i in range(21,200):
      loop = asyncio.get_event_loop()
      loop.run_until_complete(scan1(i))
      #asyncio.run(scan1(i))
    #print ("--------------------------------------------------------")
    print ("\nOpened ports in below list")
    scan2()


if __name__ == '__main__':
  scan0()
  l1 = list1
  print(l1)

  while True:
    sleep(30 - time() % 30)
    scan0()
    l2 = list1
    print(l2)
    compare1 = set(l1) - set(l2)
    compare2 = set(l2) - set(l1)
    out1 = list(compare1)
    out2 = list(compare2)
    if out1:
      print("\nALERT--->these ports are recently closed{0}".format(out1))
    if out2:
      print("\nALERT--->these ports are recently opened{0}".format(out2))
    l1 = l2
