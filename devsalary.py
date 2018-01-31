#Tool for staying motivated
#Outputs the salary range of developer jobs

#GlobalVar "d" is the primary dictionary
#d = {}

#Need better name for function than foo!
#Builds a dictionary for each position (argument: p) using zip method
#keys are salary ranges low, average, and high
#values harded coded for p, assigned using conditional statements
def foo(p):
	#this initial assignment of None prevents function being called incorrectly
	proper = "None"
	if "DevOps" in p:
                proper,low,average,high = "DevOps Engineer",105000,138000,152000
        if "MobileApp" in p:
                proper,low,average,high = "Mobile App Developer",66000,66000,11800
        if "Junior" in p:
                proper,low,average,high = "Junior Web Application Developer", 49000,78000,119000
	#quit function if variables not already defined
	if proper == "None": quit()
	#otherwise continue
	else:
		keys = ['low','average','high']
        	values = [low,average,high]
		#print proper
		x = dict(zip(keys,values))
		#returns dictionary object and proper name
		return x,proper

#foobar function named slightly better than foo
#iterates through dictionary keys (argument: k)
#calls foo to set values
def foobar(k):
	#p is position, d is dictionary
	for p in d:
		p,prop = foo(p) 
		#prop is the proper name of p
		#output statement here, enumerates value of key (k)
		print "Here is the %s salary for a %s: $%s" % (k,prop,str(p[k]))

#main function needs to check if running as main __init...
#args should use argparse
def main(arg):
	#start with simple list of positions
	positions = ('DevOps','MobileApp','Junior')
	#create dictionary from list
	d = dict.fromkeys(positions)
	#main argument becomes key to enumerate
	if arg == "low":foobar('low')
	if arg == "average": foobar('average')
	if arg == "high": foobar('high')
	


#global variables
positions = ('DevOps','MobileApp','Junior')
d = dict.fromkeys(positions)

mode = raw_input('mode:')
main(mode)
