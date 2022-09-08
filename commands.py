import query_server

qs = query_server.MyClass

class Commands:
    async def whichCommand(message):
        if "ping" in message.lower() :
            return (await qs.pingServer())
        elif "price" in message.lower() :
            foo = [1,2,3,4,3]
            return(foo)
        elif "codes" in message.lower() :
            foo = [1,2,3,4,2]
            return(foo)
        elif "help" in message.lower() :
            foo = [0,0,0,0,4]
            return(foo)
        else :
            print(str(message) + " not a command")
            return