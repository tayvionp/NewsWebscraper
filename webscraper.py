import urllib2
from bs4 import BeautifulSoup

keywords = ["bitcoin", "btc", "Security","Attack", "Breach","Cyber","trojan","cve", "crypto", "exploit"
            "Ransomware","Botnet","Worm","Hack","Flaw", "Risk","Danger","malware","infected" ]
newsFile = open('securitynews.txt', 'w')

def HackerNews():
    darkReading = ['https://www.darkreading.com/attacks-breaches.asp','https://www.darkreading.com/application-security.asp',
               'https://www.darkreading.com/vulnerabilities-threats.asp', 'https://www.darkreading.com/endpoint-security.asp',
               'https://www.darkreading.com/IoT.asp','https://www.darkreading.com/vulnerabilities-threats.asp'
               ]

    for link in darkReading:
       request = urllib2.Request(link)
       request.add_header('User-Agent', 'Mozilla 5.0')
       websitecontent = urllib2.urlopen(request).read()
       soup = BeautifulSoup(websitecontent, 'html.parser')

       headers = soup.findAll('header', {'class' : 'strong medium'})

       for h in headers:
           a = h.find("a")

           output = []

           for keyword in keywords:
               if keyword.upper() in a["title"].upper():
                   if (a["title"], a["href"]) not in output:
                       output.append((a["title"], a["href"]))

                       for link in output:
                           newsFile.write("Title: " + a["title"] + " \nLink: " "https://darkreading.com" + a["href"] + "\n")

HackerNews()
