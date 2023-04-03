import requests, os
res = requests.get('https://www.nwcfl.com/noformat-fixtures.php')
res.status_code
os.chdir('T:\\Coding\\NWCFL')
playFile = open('NWCFLFixtures.txt', 'wb')
                               
for chunk in res.iter_content(1):
    playFile.write(chunk)

res.close()
