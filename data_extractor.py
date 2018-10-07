from decimal import *
import re
from operator import itemgetter
file = open('academic_report.txt',mode='r')
yeet = file.read()
file.close()

#getting total credits needed
#total = re.search(r"(?:[a-zA-Z'-]+[^a-zA-Z'-]+){0,10}units are required for the degree(?:[a-zA-Z'-]+[^a-zA-Z'-]+){0,10}",yeet)
GAs = re.findall(r'Not Satisfied Complete(.*?)GA',yeet)
if not GAs:
    GAs = 'Satisfied'
else:
    GAs = GAs[0].strip()
    
GNs = re.findall(r'Not Satisfied Complete(.*?)GN',yeet)
if not GNs:
    GNs = 'Satisfied'
else:
    GNs = GNs[0].strip()
GHs = re.findall(r'Not Satisfied Complete(.*?)GH',yeet)
if not GHs:
    GHs = 'Satisfied'
else:
    GHs = GHs[0].strip()
    
GSs = re.findall(r'Not Satisfied Complete(.*?)GS',yeet)
if not GSs:
    GSs = 'Satisfied'
else:
    GSs = GSs[0].strip()
    
GHAs = re.findall(r'Not Satisfied Complete(.*?)GHA',yeet)
if not GHAs:
    GHAs = 'Satisfied'
else:
    GHAs = GHAs[0].strip()
    
USs = re.findall(r'Not Satisfied Complete(.*?)US',yeet)
if not USs:
    USs = 'Satisfied'
else:
    USs = USs[0].strip()
    
ILs = re.findall(r'Not Satisfied Complete(.*?)IL',yeet)
if not ILs:
    ILs = 'Satisfied'
else:
    ILs = ILs[0].strip()
i=0
tri = ()
liss = (GNs,GAs,GHs,GSs,GHAs,USs)
liss
print(liss)
firebase.put('/Gen Eds',"Gen Eds", {'GN':GNs,'GA':GAs,'GH':GHs,'GS':GSs,'GHA':GHAs,'US':USs,'IL':ILs})



total = re.findall(' Units:(.*?)required,(.*?)used,(.*?)needed',yeet)
finished = max(total,key=itemgetter(1))
firebase.put('/Credits','credits',{'Total Needed':finished[0],'Completed':finished[1],'Needed':finished[2]})
