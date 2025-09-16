from datetime import datetime
import zoneinfo

now = datetime.now(zoneinfo.ZoneInfo("America/New_York")).strftime("%B %d %Y %H:%M:%S")

out = f'''
Hello! This page last built automatically by a Github Pages workflow at: {now}
<br>
<br>
See the repository at <a href="https://github.com/blindstitch/pages-test">https://github.com/blindstitch/pages-test</a> for page source.
outfile = open('index.html','w')
outfile.write(')
outfile.close()
