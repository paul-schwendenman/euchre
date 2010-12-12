import datetime
import inspect
import re
import sys

def main():
    # Print last run
    lastrun = 'Sun Jun 13 18:16:44 2010'
    print "Last Run <<%s>>" % lastrun
    
    # Read source code
    srcfile = inspect.getsourcefile(sys.modules[__name__])
    f = open(srcfile, 'r')
    src = f.read()
    f.close()

    # Modify timestamp
    timestamp = datetime.datetime.ctime(datetime.datetime.now())
    match = re.search("lastrun = '(.*)'", src)
    if match:
        src = src[:match.start(1)] + timestamp + src[match.end(1):]

    # Write source code
    f = open(srcfile, 'w')
    f.write(src)
    f.close()

if __name__ == '__main__':
    main()
