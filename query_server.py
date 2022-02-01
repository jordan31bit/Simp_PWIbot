from ctypes import sizeof
import socket
import time
import math
import clean_reponse

server = ["pwieast2.perfectworld.com", "pwiwest4.perfectworld.com", "pwigc2.perfectworld.com", "pwieu3.en.perfectworld.eu"]
port = 29000

class MyClass:
    
    def bob(foo):
        print(foo)
        return
    
    async def pingServer():
        latency = []
        try:
            for x in server :
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    try :
                        startTime = time.time()
                        soc.connect((x, port))
                        response = soc.recv(1024)
                        endTime = time.time()
                        totalTime = endTime - startTime
                        latency.append(totalTime * 1000)
                        print(response)
                        soc.close()
                    except :
                        print(x+" is down 🔴")
                        latency.append("🔴")
        except:
            soc.close()
            return("Error: I broke :(")
        soc.close()
        latency.append(1)
        # clean = clean_reponse.Handle_Responses
        # latency = clean.cleanServerResp(latency)
        return(latency)

    async def getBlessings() :
        # return a list of mixed data types
        return

    async def autoCheckLatency() :
        print("I'm in here!!!!!")
        state = 0 # 0 assumed up, 1 server is up, 2 server is down
        tmp = state
        qs = MyClass
        list = await qs.pingServer()
        for x in list :
            if type(x) in list == str :
                tmp = ++tmp
                if state != tmp :
                    return(list)
                else :
                    time.sleep(3)
            else :
                tmp = state
                time.sleep(3)