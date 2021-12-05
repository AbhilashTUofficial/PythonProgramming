import time
import asyncio


async def process():


    for i in range(60):
        time.sleep(0.4)

        open('Learning/Intermediate/LoadingBar/file.txt',"w").write(f'{i}') 


async def readProgress():
    print(open('Learning/Intermediate/LoadingBar/file.txt',"r").read()) 


async def basic():
    while True:
        time.sleep(1)
        asyncio.create_task(process())
        asyncio.create_task(readProgress())




if __name__=="__main__":
    asyncio.run(basic())

    
