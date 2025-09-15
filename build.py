from datetime import datetime
now = datetime.now().strftime("%H:%M:%S")

outfile = open('build.html','w')
outfile.write('foo '+now)
outfile.close()
