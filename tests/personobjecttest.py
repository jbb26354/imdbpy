
# URL:  https://github.com/alberanid/imdbpy
# install-best: pip install git+https://github.com/alberanid/imdbpy
# install: pip install imdbpy

import json
from imdb import IMDb
 
# create an instance of the IMDb class
objIMDB = IMDb()
 
# get a person - say, Lindsay Wagner. We just want the films object
objActor = objIMDB.get_person('0905993', info=['filmography'])
 
# print the name of the actor
print('Filmography for:  ' + objActor['name'])
print('--------------------------------\n')

#print(objIMDB.get_person_infoset())
#objActor.infoset2keys
#print(objActor.get('filmography'))
#for film in objActor.get('filmography'): print(film)

# The filmography item is a dictionary that can be treated as an object.
# So, we just want the films where Lindsay was an actress in. This finally
# gets what we want - almost.
# objFilms = objActor.get('filmography')
# objActress = objFilms.get('actress')
# for film in objActress: print(film)

for job in objActor['filmography'].keys():
	print('# Job: ', job)
	for movie in objActor['filmography'][job]:
		if(movie['kind'] == "movie"):
			print('\t%s %s (role: %s) [%s]' % (movie.movieID, movie['title'], movie.currentRole, movie['year']))

print('--------------------------')
print('\t%s (%s)' % (objActor['filmography']['actress'][0]['title'], objActor['filmography']['actress'][0]['year']))
print('\t%s (%s)' % (objActor['filmography']['actress'][1]['title'], objActor['filmography']['actress'][1]['year']))
print('\t%s (%s)' % (objActor['filmography']['actress'][2]['title'], objActor['filmography']['actress'][2]['year']))
print('\t%s (%s)' % (objActor['filmography']['actress'][3]['title'], objActor['filmography']['actress'][3]['year']))
print('\t%s (%s)' % (objActor['filmography']['actress'][4], movie['kind']))
print('\t%s (%s)' % (objActor['filmography']['actress'][5]['title'], objActor['filmography']['actress'][5]['year']))
print('--------------------------')
print(objActor['filmography'].keys())		
print(objActor['filmography']['actress'][10].keys())
print('--------------------------')
print(len(objActor['filmography']['actress'])-1)
print('--------------------------')
for UH in range(len(objActor['filmography']['actress'])-1):
	#print(uh)
	print('\t%s (%s)' % (objActor['filmography']['actress'][UH]['title'], objActor['filmography']['actress'][UH]['year']))
