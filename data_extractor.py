import re
file = open('academic_report.txt',mode='r')
yeet = file.read()
file.close()

GAs = re.findall(r'Not Satisfied Complete(.*?)GA',yeet)
if not GAs:
    GAs = 'Satisfied'
else:
    GAs = GAs[0]
                 
GNs = re.findall(r'Not Satisfied Complete(.*?)GN',yeet)
if not GNs:
    GNs = 'Satisfied'
else:
    GNs = GNs[0]
                 
GHs = re.findall(r'Not Satisfied Complete(.*?)GH',yeet)
if not GHs:
    GHs = 'Satisfied'
else:
    GHs = GHs[0]
                 
GSs = re.findall(r'Not Satisfied Complete(.*?)GS',yeet)
if not GSs:
   GSs = 'Satisfied'
else:
    GSs = GSs[0]

GHAs = re.findall(r'Not Satisfied Complete(.*?)GHA',yeet)
if not GHAs:
    GHAs = 'Satisfied'
else:
    GHAs = GHAs[0]    
    
USs = re.findall(r'Not Satisfied Complete(.*?)US',yeet)
if not USs:\n",
    USs = 'Satisfied'
else:
    USs = USs[0]

ILs = re.findall(r'Not Satisfied Complete(.*?)IL',yeet)
if not ILs:
    ILs = 'Satisfied'
else:
    ILs = ILs[0]
                 
liss = (GNs,GAs,GHs,GSs,GHAs,USs)
print(liss)

#getting the total number of credits needed for the major, how many you've taken, and how many you still need
total = re.findall(' Units:(.*?)required,(.*?)used,(.*?)needed',yeet)
max(total,key=itemgetter(1))
