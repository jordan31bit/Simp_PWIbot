import discord
import commands
import clean_reponse
com = commands.Commands

class APIDiscord(discord.Client) :

    async def genericBuilder(self, titleBuilder, descriptionBuilder, fieldName1, fieldValue1, fieldName2, latency) :
        embed = discord.Embed()
        embed.title=titleBuilder
        embed.description=descriptionBuilder
        embed.add_field(name=fieldName1, value=fieldValue1, inline=True)
        embed.add_field(name=fieldName2, value=latency, inline=True)
        return(embed)

    async def helpMenuBuilder(self, titleBuilder, descriptionBuilder, fieldName1, fieldName2, fieldValue1, fieldValue2, fieldValue3, fieldValue4, fieldValue5, fieldValue6, fieldValue7, fieldValue8) :
        tmp = fieldValue1+'\n'+fieldValue2+'\n'+fieldValue3+'\n'+fieldValue8
        tmp2 = fieldValue4+'\n'+fieldValue5+'\n'+fieldValue6+'\n'+fieldValue7
        embed = discord.Embed()
        embed.title=titleBuilder
        embed.description=descriptionBuilder
        embed.add_field(name=fieldName1, value=tmp, inline=True)
        embed.add_field(name=fieldName2, value=tmp2, inline=True)
        return(embed)

    async def pingResponseBuilder(testing) :
        embed = discord.Embed()
        embed.title="PWI Server Check"
        embed.description="Lists ping, thus signifies that server is up or down "
        embed.add_field(name="Server", value="Tideswell \n Etherblade \n Twilight Temple \n DawnGlory", inline=True)
        embed.add_field(name="Latency", value=testing, inline=True)
        return(embed)

    async def determineWhat(self, list) :
        if list[4] == 1 :
            #send to cleaners get str back of latency
            clean = clean_reponse.Handle_Responses
            list.pop(4)
            foo = ""
            foo = clean.cleanServerResp(list)
            titleBuilder = "PWI Server Check"
            descriptionBuilder = "This lists the ping for each server. If server is down a red circle will appear next to server name."
            fieldName1 = "Server"
            fieldValue1 = "Tideswell \n Etherblade \n Twilight Temple \n DawnGlory"
            fieldName2 = "Latency"
            embed = await self.genericBuilder(titleBuilder, descriptionBuilder, fieldName1, fieldValue1, fieldName2, foo)
            return(embed)
        elif list[4] == 2 :
            titleBuilder = "PWI Blessings Codes"
            descriptionBuilder = "Jones' Blessing = 30 Att levels & O'malley's Blessing = 15 Att and Def levels."
            fieldName1 = "Jone's Blessing"
            fieldValue1 = 'fkNu6Sni'
            fieldName2 = "O'malley's Blessing"
            fieldValue2 = 'dRp86qzN'
            embed = await self.genericBuilder(titleBuilder, descriptionBuilder, fieldName1, fieldValue1, fieldName2, fieldValue2)
            return(embed)
        elif list[4] == 3 :
            titleBuilder = "PWI Price Checking (Not Working Yet)"
            descriptionBuilder = "This will query pwcats in order to perform search and obtain needed info."
            fieldName1 = "Item"
            fieldValue1 = 'item1'
            fieldName2 = "Price"
            fieldValue2 = '1,000,000.00' + ' gold coins'
            embed = await self.genericBuilder(titleBuilder, descriptionBuilder, fieldName1, fieldValue1, fieldName2, fieldValue2)
            return(embed)
        elif list[4] == 4 :
            titleBuilder = "Simp PWI Bot Help"
            descriptionBuilder = "Below is the avaiable commands. Also, check out my Git repo https://github.com/jordan31bit/Simp_PWIbot/tree/master"
            fieldName1 = "Commands"
            fieldValue1 = 'help'
            fieldValue2 = 'ping'
            fieldValue3 = 'price'
            fieldName2 = "Description"
            fieldValue4 = 'Displays this menu.'
            fieldValue5 = 'Checks to see if servers are online, then returns the latency.'
            fieldValue6 = 'Searches PWCats and returns the item info you searched for.'
            fieldValue7 = 'Displays the Blessings codes from PWI.'
            fieldValue8 = 'codes'
            embed = await self.helpMenuBuilder(titleBuilder, descriptionBuilder, fieldName1, fieldName2, fieldValue1, fieldValue2, fieldValue3, fieldValue4, fieldValue5, fieldValue6, fieldValue7, fieldValue8)
            return(embed)