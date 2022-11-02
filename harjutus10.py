#M.Kuusemäe
#2.11.22
#harjutus10
import re

#sobilik parool
fh = open('h10.txt')
for line in fh:
    if re.search('[A-Z0-9]+[A-Z]{1}', line):
        print(line,end='')

print()
#sobilik ip
fh = open('h10.txt')
for line in fh:
    if re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', line):
        print(line,end='')
