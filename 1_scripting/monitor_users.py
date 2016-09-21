import argparse
import commands
import sys

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='checks number of logged in users')
	parser.add_argument('-c','--critical', help='enter the value for critical limit', nargs='?', const=10)
	parser.add_argument('-w','--warning',  help='enter the value for warning limit', nargs='?', const=5)
	args = parser.parse_args()
	x= commands.getstatusoutput("users | tr ' ' '\n' | sort -u | wc -l")
	if args.critical is None:
		args.critical = 10
	if args.warning is None:
		args.warning = 5
	print args.warning
	(co, res) = x
	resf=int(res)
	if resf >=  args.critical:
		print "we are critical"
		sys.exit(2)
	elif resf <= args.warning:
		print " we are ok"
		sys.exit(0)
	elif (resf >= args.warning and resf < args.critical):
		print "we are warning"
		sys.exit(1)
	else:
		print "Unkown"
		sys.exit(3)
