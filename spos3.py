'''

Problem Title : MacroPreprocessor Pass 1 
Problem Scope : To traverse the code once and find out the existing macros in
				the code and accordingly create MNT, PTAB, MDT Tables in the form of 
MNT TABLE : 
{
    "#PP": 3, 
    "#KP": 0, 
    "PTAB_PTR": "1", 
    "MACRO NAME": "EVAL"
}
PTAB TABLE
{
    "&X": "A", 
    "&Y": "B", 
    "&Z": "C"
}
MDT TABLE
{
    "EVAL": [
        [
            "ADD", 
            "AREG", 
            "P0"
        ], 
        [
            "MOVEM", 
            "AREG", 
            "P1"
        ], 
        [
            "SUB", 
            "AREG", 
            "P2"
        ]
    ]
}

'''
import json
MNT= {
	"MACRO NAME" : "",
	"#PP" : "",
	"#KP" : "",
	"PTAB_PTR" : "1",
}

PTAB = {	
}

MDT = {	
}

pp=0
kp=0
is_macro = 0

with open("macro.txt") as f:
	while True:
		line = f.readline()
		if line == '':
			break
	
		words = line.strip('\n').split(' ')
		if words[0] == "MACRO":
			is_macro = 1
			continue

		if is_macro == 1:
			
			words = line.strip('\n').split(' ')
			

			MAC_NAME = words[0]
			MNT["MACRO NAME"]=words[0]
				
			for i in words:
				if i[0]=='&' and i[-1]=='=':
					kp = kp + 1
				if i[0]=='&' and i[-1]!='=':
					pp = pp + 1
				if i[0] == '&':
					PTAB[i]= ""

			MNT["#PP"]=pp
			MNT["#KP"]=kp
	
			MDT[MAC_NAME] = []
			is_macro = 0

			while words[0]!='MEND':
				words = f.readline().strip('\n').split(' ')
				#print words
				MDT[MAC_NAME].append(words)
				
			MDT[MAC_NAME].pop()

		line = f.readline()
		words = f.readline().strip('\n').split(' ')
		#print words
		if words[0]==MAC_NAME:
			PTAB['&X'] = words[1]
			PTAB['&Y']=words[2]
			PTAB['&Z']=words[3]
		for L in MDT[MAC_NAME]:
			for i in range(len(L)):
				if L[i][0] == '&' :
					#print L[i]
					#print PTAB.keys().index(L[i])
					L[i] = 'P'+str(PTAB.keys().index(L[i]))

print "MNT TABLE : "
print json.dumps(MNT, indent = 4)

print "PTAB TABLE"
print json.dumps(PTAB, indent = 4)
print "MDT TABLE"
print json.dumps(MDT, indent = 4)

