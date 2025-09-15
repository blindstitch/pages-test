from datetime import datetime
now = datetime.now().strftime("%H:%M:%S")

outfile = open('index.html','w')
outfile.write('foo karls cool'+now)
outfile.close()
