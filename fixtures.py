#!/usr/bin/env python

import argparse
import colorama
from teams_prac import teams_list
from codes import code_dict1,code_dict2

def printCodes():
	''' Prints club codes '''
	print colorama.Fore.BLUE + colorama.Style.BRIGHT + '--------------------------------------------------------------------------------'
	for key in code_dict1:
		print "{:^80s}".format(colorama.Fore.WHITE + colorama.Style.BRIGHT + key + ' : ' +code_dict1[key])
	print colorama.Fore.BLUE + colorama.Style.BRIGHT + '--------------------------------------------------------------------------------'

def printMatches(club,l,h):
	''' Prints matches for a particular club code
		choose from (LIV, RMA, BAR, CHE, ARS) '''
	l1 = []
	if club in h.keys():
		club = h[club]
		l1.append(club)
	else:
		print "Enter Valid Club Code (RMA, BAR, LIV, ARS, CHE)"
	print '--------------------------------------------------------------------------------'
	for i in range(len(l)):
		if l[i].keys() == l1:
			break
	k = l[i]
	for matches in k[club]:
		if matches != k[club][-1]:
			print "{:^80s}".format('vs ' + matches[0]+' ' + matches[1]+' ' +matches[2] +'\n')
		else:
			print "{:^80s}".format('vs ' + matches[0]+' ' + matches[1]+' ' +matches[2]) 
	print '--------------------------------------------------------------------------------'
	
def versusClubs(club1,club2,l,h1):
	''' Prints matches between two clubs who play in the same league (of course)
		club1 should be one of (RMA, BAR, LIV, ARS, CHE),
		club2 can be a club which plays in the same league '''
	print '--------------------------------------------------------------------------------'
	if club1 in h1.keys():
		club1 = h1[club1]
		l1 = []
		l1.append(club1)
		count = 0
		for i in range(len(l)):
			if l[i].keys() == l1:
				break
		k = l[i]
	else:
		print "Enter Valid Code for first club"
	if club2 in h1.keys():
		club2 = h1[club2]
		for matches in k[club1]:
			if matches[0] == club2:
				count = count + 1
				if count != 2:
					print "{:^80s}".format(matches[1]+' ' + matches[2]) +'\n'
				else:
					print "{:^80s}".format(matches[1]+' ' +matches[2])
	else:
		print "Enter Valid Code for second club"	
	print '--------------------------------------------------------------------------------'

def main():
	parser = argparse.ArgumentParser()
	colorama.init()
	parser.add_argument('-c','--club', help="Filter matches to a " +\
        "specific club code.")
	parser.add_argument('-v', '--versus', help="Find matches between " +\
        "two clubs.",nargs=2)
	parser.add_argument('codes', nargs='?', default='', help="Print club codes")
	args = parser.parse_args()

	if args.codes == 'codes':
		printCodes()

	if args.club:
		printMatches(args.club,teams_list,code_dict2)

	if args.versus:
		versusClubs(args.versus[0],args.versus[1],teams_list,code_dict2)

if __name__ == "__main__":
	main()
	
	
	
 

