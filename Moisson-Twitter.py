#twit.py
#coding: utf-8

#on importe le module csv pour pouvoir consigner les résultats dans un fichier csv
import csv
#on importe le module json pour pouvoir lire l'API
import json
#on importe le module twitter pour pouvoir traiter avec le site
import twitter
#Puis à partir d'un fichier nommé accesstwit contenant les accès donnés par la partie développeur de Twitter on importe tous les codes nécessaires pour pouvoir intéragir avec l'API
from accesstwit import APIkey, APIsecretkey, Token, Tokensecret

#La variable t détermine notre trousseau de clé pour accéder à l'API twitter. Elle réunit tous les codes récupérés dans notre fichier accesstwit.
t = twitter.Api(consumer_key=APIkey,
	consumer_secret=APIsecretkey,
	access_token_key=Token,
	access_token_secret=Tokensecret,
	tweet_mode="extended"
	)

#La variable onCherche détermine le terme que l'on va vouloir retrouver dans notre moissonage de données. Dans le cas présent, tous les tweets qui vont nous intéresser seront ceux contenant le mot "Trump".
onCherche = input("Trump")

#La variable tweets nous permet de lancer notre recherche au moyen du module .GetSearch. Elle va nous rapporter les 500 derniers tweets en json contenant le mot "Trump"
tweets = t.GetSearch(term = onCherche,count = 500,result_type = "recent",return_json = True)

#Modifie l'affichage des résultats afin de le rendre plus lisible
print(json.dumps(tweets, indent=2, sort_keys=True))

#Cette boucle va nous permettre de sélectionner les données que l'onveut dans les résultats obtenus grace à la variable t. 
for tweet in tweets["statuses"]:
	print("Date/heure ", tweet["created_at"])
	print("Contenu ", tweet["full_text"])
	print("Pseudo ", tweet["user"]["name"])
	print("Retweets ", tweet["retweet_count"])
	print("P'tits coeurs ", tweet["favorite_count"])
	print("*"*60)
	