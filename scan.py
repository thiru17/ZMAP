import subprocess
import time
import asyncio  
b=[]	
async def fscan():
	temp_list=[]
	ip=input("Enter the IP to scan:")
	for port in range(80,90):
		filename='result_'+str(port)+'.txt'
		
		p1=subprocess.Popen(['zmap','-p',str(port),str(ip),'-o',filename], stdout=subprocess.PIPE)
		await asyncio.sleep(0.25)
		output= p1.communicate()
		contents=open(filename,'r').read()
		if(len(contents)>0):
			temp_list.append(port)
	return temp_list
        

async def compare():	
    a=fscan()

    while True:
	    b=fscan()
	    a.sort()
	    b.sort()
	    if a == b:
		    print("Ports are Same No Difference Found")
	    else:
		    print("Ports are Different",a,b)
	
	
	    await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fscan())
    task2 = asyncio.create_task(compare())
   	
asyncio.run(main())  	

