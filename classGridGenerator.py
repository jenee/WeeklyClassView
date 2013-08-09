import datetime

print "<html><head><title>Calendar 2013</title>"
print "<style type=\"text/css\">"
print "<!-- Styling for the half hour blocks -->"
print ".halfhourblock  {     "
print "   font-size: large;"
print "   padding: 0.25em 0.25em;"  
print "   text-align: right;"
print "   vertical-align: top;"
print "}"
print "table td {"
print "   height: 40px;"
print "   width: 100px;"
print "}"

print "</style>"
print "</head>"
print "<body>"

print"<table border=\"1\">"
print"\t<thead>"
print"\t\t<th>Class Schedule"
print"\t\t</th>"
print"\t</thead>"
print"\t<tbody>"

#headers for each day of week
print"\t\t<tr>"
print"\t\t</tr>"

##cells in half-hour increments
print"\t\t<tr>"
print"\t\t\t<td>"

endTime = datetime.time(22,0)
t = datetime.time(8,0)
fullDate = datetime.datetime(100, 1, 1, t.hour, t.minute, t.second)
timeDelta = datetime.timedelta(minutes=30)

counter = 0
while t < endTime:
   print 'The {} is {:%I:%M %p}.'.format("time", t)
   fullDate += timeDelta
   t = fullDate.time()

   counter +=1
   if counter > 100:
      break
print"\t\t\t\t<span class=\"halfhourblock\">"
print"\t\t\t\t\t08:00am"
print"\t\t\t\t</span>"
print"\t\t\t</td>"

print"\t\t</tr>"



print"\t</tbody>"

print"\t</table>"

print"</body>"
print"</html>"
