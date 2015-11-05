f = open("D:/yesterday.txt",'r')
yesterday_lyric=""
while 1:
    line = f.readline()
    if not line: break
    yesterday_lyric = yesterday_lyric + line.strip() + "\b"
f.close()
n1_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
n2_of_yesterday = yesterday_lyric.upper().count("Yesterday")
n3_of_yesterday = yesterday_lyric.upper().count("yesterday")
print "Number of A Word 'YESTERDAY'", n1_of_yesterday
print "Number of A Word 'Yesterday'", n2_of_yesterday
print "Number of A Word 'yesterday'", n3_of_yesterday


