import asyncio
import time


class Basic:

    async def func():
        time.sleep(1)
        print("Function")
        

    async def main():
        print("start")
        asyncio.create_task(Basic.func())
        print("Finished")


if __name__=="__main__":
    #* Run order: Start -> Finished -> Function    
    asyncio.run(Basic.main())
