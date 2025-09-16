from datetime import datetime
now = datetime.now().strftime("%B %d %Y %H:%M:%S")

outfile = open('index.html','w')
outfile.write('Hello! This page last built automatically by a Github Pages workflow at: '+now)
outfile.close()
