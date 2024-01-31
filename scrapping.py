# import requests
# import json

# url = 'https://offer.cdn.betclic.fr/api/pub/v4/events?application=2&countrycode=us&fetchMultipleDefaultMarkets=false&language=fr&limit=20&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate'
# response = requests.get(url)
# data = json.loads(response.text)

# # Parcourir chaque match dans la liste
# for match in data:
#     id_match = match.get('id')
#     nom_joueur = match.get('name')
#     date_match = match.get('date')
#     sport_joue = match.get('competition', {}).get('sport', {}).get('name')
#     competition_name = match['competition']['name']
#     if 'contestants' in match and len(match['contestants']) >= 2:
#         team_one = match['contestants'][0]['name'] 
#         team_two = match['contestants'][1]['name'] 

#     # if id_match and nom_joueur and date_match and sport_joue:
#         print(f"ID: {id_match}, Nom: {nom_joueur}, Date: {date_match}, Sport: {sport_joue}, Competition: {competition_name}, Equipe à domicile: {team_one}, Equipe à l'extérieur: {team_two}")


# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

import requests
import json

url = 'https://offer.cdn.betclic.fr/api/pub/v4/events?application=2&countrycode=us&fetchMultipleDefaultMarkets=false&language=fr&limit=20&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate'
response = requests.get(url)
data = json.loads(response.text)

# Liste pour stocker les données extraites
extracted_data = []

for match in data:
    # Extraction des données
    extracted_info = {
        "ID": match.get('id'),
        "Nom": match.get('name'),
        "Date": match.get('date'),
        "Sport": match.get('competition', {}).get('sport', {}).get('name'),
        "Competition": match.get('competition', {}).get('name')
    }

    if 'contestants' in match and len(match['contestants']) >= 2:
        extracted_info["Equipe a domicile"] = match['contestants'][0]['name']
        extracted_info["Equipe a l'exterieur"] = match['contestants'][1]['name']

    extracted_data.append(extracted_info)

# Enregistrement des données extraites dans un fichier JSON
with open('data.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)
