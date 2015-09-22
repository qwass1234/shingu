import urllib
file=urllib.urlopen('http://www.korea.kr')
htmlcontents=file.read()
print htmlcontents
