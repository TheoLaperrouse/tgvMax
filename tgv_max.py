import urllib.request, json

def prepare_url(date,origine, destination):
    url = f"https://ressources.data.sncf.com/api/records/1.0/search/?dataset=tgvmax&sort=date"
    url += "&refine.origine=" + origine
    url += "&refine.destination=" + destination
    url += "&refine.date=" + date
    return url

def search_train(data):
    nb_train = len(data["records"])
    for i in range(0, nb_train):
        if (data["records"][i]["fields"]["od_happy_card"] == "OUI"):
            hour = data["records"][i]["fields"]["heure_depart"]
            date = data["records"][i]["fields"]["date"]
            origine = data["records"][i]["fields"]["origine"]
            destination = data["records"][i]["fields"]["destination"]
            print(f'{origine} vers {destination} : {date} à {hour}')

def loop_train(origine,destination,mois):
    for i in range(1,30):
            date = f"{mois}{i}"
            url = prepare_url(date, origine, destination)
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            search_train(data)

def main():
    mois = "2022%2F07%2F"
    loop_train("PARIS+(intramuros)","RENNES",mois)
    loop_train("METZ+VILLE","PARIS+(intramuros)","2022%2F07%2F",mois)
    
    

if __name__ == '__main__':
    main()
