
######################################################################
# URL:  https://github.com/alberanid/imdbpy                          #
# install-best: pip install git+https://github.com/alberanid/imdbpy  #
# install: pip install imdbpy                                        #
######################################################################

from imdb import IMDb

# lindsay wagner '0905993'
# burt lancaster '0000044'
# helen hunt     '0000166'
# anne heche     '0000162'
# john travolta  '0000237'
# rock hudson    '0001369'
# peter o'toole  '0000564'
# anthony quayle '0703033'
strPersonID = '0703033'

# create an instance of the IMDb class
objIMDB = IMDb()
 
# get a person. We just want the films object
objActor = objIMDB.get_person(strPersonID, info=['filmography'])
 
# print the name of the actor
print('Filmography for:  ' + objActor['name'])
print('--------------------------------\n')

for job in objActor['filmography'].keys():
	for movie in objActor['filmography'][job]:
		# movie['year'] won't work if it's a TV series, we just want movies anyway (actress, self) 
		# (movie['kind'] == 'movie' or movie['kind'] == 'tv movie') and 
		if (job == "actress" or job == "actor"):
			try:
				print('\t%s: %s (as: %s) [%s]' % (movie['kind'], movie['title'], movie.currentRole, movie['year']))
			except:
				print('\t%s: %s %s' % (movie['kind'], movie['title'], '[In Production]'))				
				