
######################################################################
# URL:  https://github.com/alberanid/imdbpy                          #
# install-best: pip install git+https://github.com/alberanid/imdbpy  #
# install: pip install imdbpy                                        #
######################################################################

from imdb import IMDb
 
# create an instance of the IMDb class
objIMDB = IMDb()

# burt lancaster '0000044'
# lindsay wagner '0905993'
# helen hunt     '0000166'
strPersonID = '0000166'

objActor = objIMDB.get_person(strPersonID, info=['filmography'])
 
# Header
print('Filmography for:  ' + objActor['name'])
print('--------------------------------\n')

# Movie List
for job in objActor['filmography'].keys():
	for movie in objActor['filmography'][job]:
		# movie['year'] won't work if it's a TV series, we just want movies anyway (actress, self) and (job == "actress")
		if movie['kind'] == "movie" and (job == "actress" or job == "actor"): 
			try: 
				print('\t%s (role: %s) [%s]' % (movie['title'], movie.currentRole, movie['year']))
			except:
				print('\t%s %s' % (movie['title'], '[In Production]'))
			