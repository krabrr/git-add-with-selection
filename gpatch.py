#!/usr/bin/env python
import os
import sys
import subprocess

filename = 'fix.patch'
if len(sys.argv) <= 2:
    p = subprocess.Popen(['git', 'log', '-1'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    output = output.split('\n')[0]
    outputs = output.split()
    if len(outputs) == 2:
        commit_version = outputs[1]
        prev_version = commit_version+'~1'
    else:
        print 'Error: cannot get commit version'
        sys.exit()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
elif len(sys.argv) <= 4:
    prev_version = sys.argv[1]
    commit_version = sys.argv[2]
    if len(sys.argv) == 4:
        filename = sys.argv[3]

print 'prev version: '+prev_version
print 'current version: '+commit_version

p = subprocess.Popen(['git', 'diff', prev_version, commit_version], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
print output
out = open(os.path.expanduser('~/' + filename), 'w')
out.write(output)
out.close()


