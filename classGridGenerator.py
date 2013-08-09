import datetime
import calendar

print "<html><head><title>Calendar 2013</title>"
print "<style type=\"text/css\">"
print "<!-- Styling for the half hour blocks -->"
print ".halfhourblock  {     "
#print "   font-size: large;"
#print "   padding: 0.25em 0.25em;"  
print "   text-align: center;"
print "   vertical-align: top;"
print "}"
print "table td {"
print "   height: 40px;"
print "   width: 150px;"
print "}"

print "</style>"
print "</head>"
print "<body>"

print"<table border=\"1\">"
print"\t<thead>"
print"\t\t<tr>"
print"\t\t\t<th colspan=\"8\">Class Schedule"
print"\t\t\t</th>"
print"\t\t</tr>"

print"\t\t<tr>"
#header to label times
print "\t\t\t<th>"
print "\t\t\t\t time"
print "\t\t\t</th>"

#headers for each day of week
for day in calendar.day_abbr:
   print "\t\t\t<th>"
   print "\t\t\t\t"+day
   print "\t\t\t</th>"

print"\t\t</tr>"


print"\t</thead>"
print"\t<tbody>"


##cells in half-hour increments

endTime = datetime.time(22,0)
t = datetime.time(8,0)
fullDate = datetime.datetime(100, 1, 1, t.hour, t.minute, t.second)
timeDelta = datetime.timedelta(minutes=30)

timeLabelBlocks = []

counter = 0
while t < endTime:
   timeHTMLStr =  "\t\t\t<td>\n"
   timeHTMLStr += "\t\t\t\t<span class=\"halfhourblock\">\n"
   timeHTMLStr += "\t\t\t\t\t"
   timeHTMLStr += '{:%I:%M %p}'.format(t)
   timeHTMLStr += "\n"
   timeHTMLStr += "\t\t\t\t</span>\n"
   timeHTMLStr += "\t\t\t</td>"
 
   timeLabelBlocks.append(timeHTMLStr)

   #print 'The {} is {:%I:%M %p}.'.format("time", t)
   fullDate += timeDelta
   t = fullDate.time()

   counter +=1
   if counter > 100:
      break
#print"\t\t<tr>"
#print"\t\t\t<td>"
#print"\t\t\t\t<span class=\"halfhourblock\">"
#print"\t\t\t\t\t08:00am"
#print"\t\t\t\t</span>"
#print"\t\t\t</td>"

#print"\t\t</tr>"

#Spit out HTML code for time grid
for timeLabel in timeLabelBlocks:
   print"\t\t<tr>"
   print timeLabel
   
   for emptyCellNum in range(7):
      print"\t\t\t<td>"
      print"\t\t\t\t<span class=\"halfhourblock\">"
      print"\t\t\t\t\t<stuff>"
      print"\t\t\t\t</span>"
      print"\t\t\t</td>"


   print"\t\t</tr>"

print"\t</tbody>"

print"\t</table>"

print"</body>"
print"</html>"
