
######################################################################
# URL:  https://github.com/alberanid/imdbpy                          #
# install-best: pip install git+https://github.com/alberanid/imdbpy  #
# install: pip install imdbpy                                        #
######################################################################

# Davide Alberani's most excellent module
from imdb import IMDb

import datetime
import sys

# lindsay wagner '0905993'
# burt lancaster '0000044'
# helen hunt     '0000166'
strPersonID = '0000166'

# command line arg processing

#https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
if len(sys.argv) < 2:
  print("\nThis version of the script requires a personID.\n")
  # https://stackoverflow.com/questions/3376534/how-do-i-halt-execution-in-a-python-script
  sys.exit()
elif sys.argv[1] == '':
  print("\nUsing Helen Hunt as default.")
  actorID = strPersonID
else:
  actorID = sys.argv[1]

# fetch an actor's filmography and dump to web page with checkmark support
def Create_Actor_Filmography(imdbID):
	
  # create an instance of the IMDb class
  objIMDB = IMDb()
  
  # open the file
  objWebPage = open(r"Filmography.htm", "w")
  
  # get a person - say, Lindsay Wagner ('0905993'). We just want the films object
  objActor = objIMDB.get_person(imdbID, info=['filmography'])
  
  # beginning tags
	
  objWebPage.writelines('<!DOCTYPE html>' + '\n\n')
  objWebPage.writelines('<html xml:lang="en-US" dir="ltr" lang="en-US"' + '\n\n')
  objWebPage.writelines('<head>' + '\n')
  objWebPage.writelines('\t<title>' + objActor['name'] + ' - Filmography</title>' + '\n')	
  objWebPage.writelines('\t<meta http-equiv="Pragma" content="no-cache">' + '\n')
  objWebPage.writelines('\t<meta http-equiv="Cache-control" content="no-cache">' + '\n')
  objWebPage.writelines('\t<meta charset="utf-8">' + '\n')
  objWebPage.writelines('</head>' + '\n\n')
  objWebPage.writelines('<body>' + '\n\n')
  
  # Header
  objWebPage.writelines('\t<h2 style="text-decoration: underline;">' + objActor['name'] + '</h2>\n')
  objWebPage.writelines('\t<address>last updated ' + datetime.datetime.now().strftime("%x") + '</address><br>\n\n')
	
  # Table
  objWebPage.writelines('\t<table border="1">' '\n')
  objWebPage.writelines('\t\t<tr><th>Obtained</th><th>Movie</th></tr>\n')
  
  # Movie List
  for job in objActor['filmography'].keys():
    for movie in objActor['filmography'][job]:
      # movie['year'] won't work if it's a TV series, we just want movies anyway (actress, self) and (job == "actress")
      if (movie['kind'] == 'movie' or movie['kind'] == 'tv movie') and (job == "actress" or job == "actor"): 
        try: 
          objWebPage.writelines('\t\t<tr><td>&nbsp;</td><td>')
          objWebPage.writelines('%s [role: %s] (%s)' % (movie['title'], movie.currentRole, movie['year'])) 
          objWebPage.writelines('</td></tr>\n')
        except:
          objWebPage.writelines('%s [role: %s] [%s]' % (movie['title'], movie.currentRole, 'In Production')) 
          objWebPage.writelines('</td></tr>\n')
  
  # ending tags
  objWebPage.writelines('\t</table>\n\n')
  objWebPage.writelines('</body>\n')
  objWebPage.writelines('</html>\n')
  
  # close the file
  objWebPage.close()
  
  print('\nCreated ' + objActor['name'] + ' filmography web page.\n')

# call the function
Create_Actor_Filmography(actorID)