import requests
import ast
ptag=raw_input("player tag ")
url=[]
url.append('https://api.clashofclans.com/v1/players/%23')
pta=ptag[1:]
url.append(str(pta))
finurl=''.join(url)
r=requests.get(finurl, headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE2NTNjMjY0LWVjNmYtNDNmZi1hNzA5LTE4OGUyYzZjNzRhNSIsImlhdCI6MTUwMjQwNzQ4Nywic3ViIjoiZGV2ZWxvcGVyLzJkOWUzNWJjLWM3OWEtM2FmYS0yOWMwLWUxNTRmZDMyMDE2OSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExMy4xOTcuOS4xOTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.6btrlgDUE3Lv3mOWlD3mXJz9Jxday_KJZaRtuI0t-qYAmcZ02vMvTQkk02l-zLkrObeF3uNSrm9W-4aRfb6i3g'})
playerinfo=ast.literal_eval(r.text)
print(r.text)
league=playerinfo['league']
heroes=playerinfo["heroes"]
print("Your name is "+playerinfo["name"])
print("Your Town Hall Level is "+str(playerinfo["townHallLevel"]))
print("Your league is "+league["name"])
print("Your player tag is "+playerinfo["tag"])
bk=heroes[0]
aq=heroes[1]
print("Your Barbarian King's level is "+str(bk["level"]) +" out of "+str(bk["maxLevel"]))
print("Your Archer Queens's level is "+str(aq["level"]) +" out of "+str(aq["maxLevel"]))
if len(heroes) == 3:
    gw=heroes[2]
    print("Your Grand Wardens's level is "+str(gw["level"]) +" out of "+str(gw["maxLevel"]))
else:
    print("You dont have the Grand Warden.")
clan=playerinfo["clan"]
print("Your clans name is "+clan["name"] +" and you are a "+playerinfo["role"])
if league["name"] == "Legend League":
    legstats=playerinfo["legendStatistics"]
    curseason=legstats["currentSeason"]
    print("You are currently #"+str(curseason["rank"])+" in the world, with "+str(curseason["trophies"])+" Trophies.")
else:
    print("git gud skrub and get into legend league")
