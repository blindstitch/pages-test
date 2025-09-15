from datetime import datetime
now = datetime.now().strftime("%H:%M:%S")

outfile = open('index.html','w')
outfile.write('Hello! This page last built at: '+now)
outfile.close()
