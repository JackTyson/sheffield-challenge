import requests # Import requests framework for fetching data from SpaceX servers
import json

class sxLaunchDataLatest:
    def __init__(self):
        self.sxLatest = "https://api.spacexdata.com/v4/launches/latest"
        self.sxLP = "https://api.spacexdata.com/v4/launchpads/"
        self.sxCrew = "https://api.spacexdata.com/v4/crew/"
        self.sxRocket = "https://api.spacexdata.com/v4/rockets/"
        self.sxShips = "https://api.spacexdata.com/v4/ships/"

    def fetchLatest(self):
        data = json.loads(requests.get(self.sxLatest).content)
        if(data['crew'] == []):
            dataCrew = "This flight was unmanned."
        else:
            dataCrew = []
            for idx in data['crew']:
                tmp = json.loads(requests.get(self.sxCrew+idx).content)
                dataCrew.append(tmp['name']) # Add crew names to the temporary crew database variable
        dataLP = json.loads(requests.get(self.sxLP+data['launchpad']).content)
        dataLP = dataLP['full_name'] + ", " + dataLP['locality'] + ", " + dataLP['region']
        dataRocket = json.loads(requests.get(self.sxRocket+data['rocket']).content)
        dataRocket = dataRocket['name']
        dataShips = []
        for idx in data['ships']:
            tmp = json.loads(requests.get(self.sxShips+idx).content)
            dataShips.append(tmp['name'])
        return([dataCrew,dataLP,dataRocket,dataShips])

    def printSpaceXData(self,data):
        print("-----------------------------")
        print("| LATEST SPACEX FLIGHT DATA |")
        print("-----------------------------")
        print("Launch Site:", data[1])
        print("Rocket Name:", data[2])
        print("Crew information:", data[0])
        print("Ships Involved:", data[3])
        return

spaceX = sxLaunchDataLatest()
spaceX.printSpaceXData(spaceX.fetchLatest())
