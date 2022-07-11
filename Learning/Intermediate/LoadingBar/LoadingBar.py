import time


green='\033[92m'
bold='\033[1m'

def minimal():

    for i in range(100):
        time.sleep(0.1)
        print(f"{green}{bold}{i}%{green}{bold}",end="\r")
    
    for i in range(100):
        time.sleep(0.1)
        print(f"{green}{bold}|{bold}{green}"*i,end="\r")


def basic():

    #! Not Working as expected!
    
    s='.'
    for i in range(100):
        time.sleep(0.1)
        if len(s)>10:
            s=str('.'*1)
        else:
            s='.'*(len(s)+1)

        print(f"{green}{bold}Now Loading.{s}{bold}{green}",end="\r")

    from tqdm import tqdm

    loop=tqdm(total=50,position=0,leave=False)
    for i in range(50):
        time.sleep(0.1)
        loop.set_description(f"{green}{bold}Loading: ".format(i))
        loop.update(1)
    loop.close()

    
def good():
    from tqdm.auto import tqdm
    for i in tqdm(range(int(9e6))):
        print("",end="\r")

def main():
    print("\n____LOADING BARS____\n")
    basic()    

if __name__=="__main__":
    main()

    
