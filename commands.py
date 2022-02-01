import query_server

qs = query_server.MyClass

class Commands:
    async def whichCommand(message):
        if "ping" in message :
            return(await qs.pingServer())
        elif "price" in message :
            foo = [1,2,3,4,3]
            return(foo)
        elif "codes" in message :
            foo = [1,2,3,4,2]
            return(foo)
        elif "help" in message :
            foo = [0,0,0,0,0]
            return(foo)
        else :
            print(str(message) + " not a command")
            return