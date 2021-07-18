
######################################################################
# URL:  https://github.com/alberanid/imdbpy                          #
# install-best: pip install git+https://github.com/alberanid/imdbpy  #
# install: pip install imdbpy                                        #
######################################################################

from imdb import IMDb

# lindsay wagner '0905993'
# burt lancaster '0000044'
# helen hunt     '0000166'
strLPersonID = '0000166'

# create an instance of the IMDb class
objIMDB = IMDb()

# open the file
objTextFile = open(r"MovieList.txt", "w")

# get a person - say, Lindsay Wagner. We just want the films object
objActor = objIMDB.get_person(strLPersonID , info=['filmography'])
 
# Header
print('Filmography for:  ' + objActor['name'])
print('--------------------------------\n')
objTextFile.writelines('Filmography for:  ' + objActor['name'] + '\n')
objTextFile.writelines('--------------------------------\n\n')

# Movie List
for job in objActor['filmography'].keys():
	for movie in objActor['filmography'][job]:
		# movie['year'] won't work if it's a TV series, we just want movies anyway (actress, self) and (job == "actress")
		if (movie['kind'] == 'movie' or movie['kind'] == 'tv movie') and (job == "actress" or job == "actor"): 
			try: 
				print('\t%s (role: %s) [%s]' % (movie['title'], movie.currentRole, movie['year']))
				objTextFile.writelines('\t%s (role: %s) [%s]' % (movie['title'], movie.currentRole, movie['year']))
				objTextFile.writelines('\n')
			except:
				print('\t%s %s' % (movie['title'], '[In Production]'))
				objTextFile.writelines('\t%s %s' % (movie['title'], '[In Production]'))
				objTextFile.writelines('\n')
				
# close the file
objTextFile.close()

print("Done.")