import sys
import subprocess

proc1 = subprocess.Popen("git describe --tags", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out = proc1.communicate()

if proc1.returncode != 0:
    sys.stdout.write("fourbars must install from cloned folder. make sure .git folder exists\n")
    sys.stdout.write(out[1])
    raise SystemExit(32)



v = out[0].decode('ascii').replace('\n', '')

if v.startswith('v.'):
    v = v[2:]
elif v.startswith('v'):
    v = v[1:]
li = v.split('.')
lii = li[1].split('-')
if len(lii) == 3:
    v = '{0}.{1}.{2}'.format(li[0],lii[0],lii[1])
else:
    v = '{0}.{1}'.format(li[0], li[1])

print (v)
