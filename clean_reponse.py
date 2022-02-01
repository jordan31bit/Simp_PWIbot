import math

class Handle_Responses :
    def cleanServerResp(latency) :
        tmp = ' '
        for x in latency :
            if type(x) == str :
                pass
            else :    
                x = math.trunc(x)
                x = str(x)
            tmp += ' ' + x + '\n'
        return(tmp)