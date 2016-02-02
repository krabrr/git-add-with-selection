#!/usr/bin/env python

import re
import sys
from subprocess import call
from subprocess import Popen
from subprocess import PIPE

p = Popen(['git', 'status'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output,err = p.communicate()
outputs = output.split('\n')
errors = err.split('\n')
outputs = outputs + errors

files = []
re1 = re.compile(r'[\t ]*(both )?modified:[\t ]*')
re2 = re.compile(r'[\t ]*deleted:[\t ]*');
re3 = re.compile(r'[\t ]+')
for output in outputs:
    if not re.match(r'\t', output):
        continue
    if re1.match(output):
        output = re1.sub('', output)
    elif re2.match(output):
        output = re2.sub('', output)
    elif re3.match(output):
        output = re3.sub('', output)
    if output == '':
        continue
    if output in files:
        continue
    files.append(output)

if len(files) == 0:
    print 'no files to add'
    sys.exit()
print '\nselect file indice to add:\n'

for idx in range(len(files)):
    print '['+str(idx)+'] '+str(files[idx])
print ''

inp = raw_input('indice: ')
idx_list = inp.split()
idx_list = [int(idx) for idx in idx_list]
result = [] 
for idx in idx_list:
    result.append(files[idx])

if len(result) == 0:
    sys.exit()

print 'select files:'
for file_name in result:
    print '\t'+file_name

call(['git', 'add']+result)
