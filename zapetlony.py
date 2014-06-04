import re
import sys
#import pars
from pars import *
plik = sys.argv[1]
stacyja = sys.argv[2]	#nazwa stacji
pracy = sys.argv[6]	#tryb pracy
debugu = sys.argv[7]	#tryb debugu
unix = sys.argv[3]	#unixtime
dzien = sys.argv[4]	#dzien lokalny
czas = sys.argv[5]	#czas lokalny
#sf = 			#save file
#sm = 			#save mode
slowniczekkoncowek = {'001TOR.jsp': 'jski', '002TOR.jsp': 'rzyny', '003TOR.jsp': 'packiego', '004TOR.jsp': 'torna', '005TOR.jsp': 'ejskie', '006TOR.jsp': 'sytecka', '007TOR.jsp': 'esco', '008TOR.jsp': 'arket', '009TOR.jsp': 'arket', '010TOR.jsp': 'wny', '011TOR.jsp': 'olicji', '012TOR.jsp': 'aciej'}
# ^ to tutaj to slowniczek koncowek, dzieki ktoremu bedzie mozna wyodrebnic sama liczbe rowerow, ktora jest jedyna liczba pomiedzy owa koncowka a "szt.".
#  i tak nie uzylem slowniczka, ale przynajmniej przypomnialem sobie dictionaries w pythonie
szt = '.*szt'

file = open(plik, 'r')
#save = open(sf, 'a')

par = pars(file.read(), stacyja)
rowery = par.rowery
#stacyja = par.stacyjka
stacjinazwa = stacyja
if rowery == 0:
	orzim = "estas neniu bicikloj"
elif rowery == -1:
	orzim = "okazis iun eraron, cxar gxi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto"
elif rowery <= 0:
	orzim = "okazis iun eraron, cxar gxi transdonas ke tie estas " + str(rowery) + " bicikloj - kaj tio estas negativa kvanto"
elif rowery == 1:
	orzim = "estas 1  biciklo"
elif rowery >= 2:
	if rowery <= 9:
		orzim = ("estas " + str(rowery) + "  bicikloj")
	if rowery >= 10:
		orzim = ("estas " + str(rowery) + " bicikloj")
else:
	orzim = ", ni ne scias kiom bicikloj estas tie, cxar dum la akiroprovon de la biciklokvanto okazis la eraro"
#La "if" super estos uzota pri la interfaco por homojn: modo 'f' kaj 'u'
if pracy == 'u':
	print dzien, czas, "Al la biciklastacio", stacjinazwa, orzim
elif pracy == 'l':
        print dzien, czas, "Al la biciklastacio", stacjinazwa, orzim
elif pracy == "p":
	print dzien, czas, stacjinazwa, rowery
elif pracy == "c":
	print unix, stacja, rowery
elif pracy == "m":
	print unix, stacjinazwa, rowery
else:
	print "Elektu labormodo u, l, p, c aux m se vi volas ke tiun programon funkcas."
	print "Plej eble ke la labormodo ", pracy, " estas malbona."
#if param1 == "p":
#	print "
#print "Czas: ", unix, " --  na stacji ", stacjinazwa, " jest ", rowery, " rowerow"
#print 'Na stacji ', stacyja, ' jest ', szt, ' rowerow miejskich.'


#tu bedzie jeszcze append do csvka
#EDIT: lub innej, sensowniejszej bazy danych

#tie estos ankaux append al la csv-o
#aux al alian, pli sencan datumbazon

file.close()
