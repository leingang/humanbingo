#!/usr/bin/python
"""
  <rdf:Description about="bingo.py"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:foaf="http://xmlns.com/foaf/1.0"
    xmlns:dct="http://purl.org/dc/terms/"> 
    <dc:description>
      Generate a bingo card for Icebreaking
    </dc:description>
    <dc:creator>
      <foaf:Person>
	<foaf:name>Derek Bruff</foaf:name>
      </foaf:Person>
    </dc:creator>
    <dct:created>2005-02-04</dct:created>
    <dc:creator>
      <foaf:Person>
	<foaf:name>Matthew Leingang</foaf:name>
	<foaf:mbox_sha1sum>9a4b7887cf33bd8142613c0832ba2710d242999c</foaf:mbox_sha1sum>
      </foaf:Person>
    </dc:creator>
    <dct:created>2006-02-05</dct:created>
    <dct:modified>2007-06-23</dct:modified>
  </rdf:Description>
"""

import sys, getopt, re
import random

from xml.sax import ContentHandler, parse, ErrorHandler

class EventsParser(ContentHandler):

    def __init__(self,stream):
	self.stream = stream
	self.events={}
	self.events['Categories'] = []
	self.currentText=""
	self.currentCategory=""
	
    def startElement(self,name,attrs):
	self.context=name
	if (name=="category"):
	    self.currentCategory=attrs['name']
	    self.events['Categories'].append(self.currentCategory)
	    self.events[self.currentCategory] = []
    
    
    def characters(self,text):
	self.currentText += text

    def endElement(self,name):
	if (name=="event"):
	    self.events[self.currentCategory].append(stripWS(self.currentText))
	self.currentText=""




def stripWS(text):
    text = re.sub(re.compile(r"^\s*"),"",text)
    text = re.sub(re.compile(r"\s*$"),"",text)
    return text


class BingoCard:
    
    def __init__(self,events):
	"""Constructor"""
	self.events=events
	self.categories=self.events['Categories']
	self.cells=[]
	cellst=[]
	for category in self.categories:
	    cellst.append(random.sample(self.events[category],5))
	# transpose cells
	for i in range(0,5):
	    self.cells.append([None,None,None,None,None])
	    for j in range(0,5):
		self.cells[i][j] = cellst[j][i]
	self.cells[2][2]="wants to get an A in this class"


class BingoCardWriter:
    """Class to write Card to File"""
    
    def __init__(self,fileName):
	self.fileName=fileName
	  
    def write(self,card):
	"""Write card to file"""
	self.output=open(self.fileName,'w')
	self.output.writelines("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
  <head>
    <title>Name Bingo</title>
    <style type="text/css">
      h1 p th td {
        font-family: Papyrus;
      }
      h1 {
        text-align: Center;
	font-family: "Comic Sans MS"
      }

      #bingoCard {
        margin-left:auto; margin-right:auto;
      }

      #bingoCard,tr,td {
        font-family: "Comic Sans MS";	
      }

      #bingoCard th, #bingoCard td {
        width: 20%;
      }
    </style>
  </head>
<body>
  <h1>Name Bingo</h1>
  
  <p>Find people in the class (other than yourself) who match the descriptions in each box; write their name in the box.</p>

  <p>Try to fill as many boxes as possible (one box per person). Five in a row wins!</p>

  <table border="2" cellspacing="0" cellpadding="4" align="center" id="bingoCard">
  
""")
	# top row is categories
	categories = card.categories
	self.output.writelines("    <tr>\n")
	for category in categories:
	    self.output.writelines("      <th>%s</th>\n" % category)
	self.output.writelines("    </tr>\n")
	for row in card.cells:
	    self.output.writelines('    <tr>\n')
	    for cell in row:
		self.output.writelines('      <td width="120" height="120" align="center" valign="center">%s</td>\n' % cell)	
	    self.output.writelines("    </tr>\n")
	self.output.writelines("""  </table>
</body>
</html>
""")

	self.output.close()
	print >> sys.stderr, "Done!\n"

def usage():
    print main.__doc__

def main():
    """Usage bingo.py [options]"""

    try:
	opts, args = getopt.getopt(sys.argv[1:], "hn:", ["help", "number="])
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    n=1
    for o,a in opts:
	if o in ("-h","--help"):
	    usage()
	    sys.exit()
	if o in ("-n","--number"):
	    n=int(a)
    handler=EventsParser(sys.stdout)
    parse("events.xml",handler,handler)
 
    for i in range(1,n+1):
	outputFileName="card%02d.html" % i
	card=BingoCard(handler.events)
	writer=BingoCardWriter(outputFileName)
	writer.write(card)
	
if __name__== "__main__":
    main()
