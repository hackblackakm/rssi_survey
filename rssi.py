import sys
import subprocess
import time
import argparse
import datetime

parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0', help='wlan interface ( default : wlan0)')
args = parser.parse_args()

f = open('output','a')

print >> f, datetime.datetime.now()
while True:
	cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True, stdout=subprocess.PIPE)
	for line in cmd.stdout:
		if 'Link Quality' in line:
			print >> f, line.lstrip(' '),
		elif 'Not-associated' in line:
			print >> f, 'No signal'
	time.sleep(3)
	
f.close()