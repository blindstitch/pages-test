from datetime import datetime
import zoneinfo

now = datetime.now(zoneinfo.ZoneInfo("America/New_York")).strftime("%B %d %Y %H:%M:%S")

outfile = open('index.html','w')
outfile.write('Hello! This page last built automatically by a Github Pages workflow at: '+now)
outfile.close()
