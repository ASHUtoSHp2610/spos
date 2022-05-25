opcode_table = {
	"HALT" : '00',
	"ADD"  : '01',
	"SUB"  : '02',
	"MULT" : '03',
	"MOVER": '04',
	"MOVEM": '05',
	"COMP ": '06',
	"BC"   : '07', 
	"DIV"  : '08',
	"READ" : '09',
	"PRINT": '10'
}

register_table = {
	"AREG" : '1',
	"BREG" : '2',
	"CREG" : '3',
	"DREG" : '4'
}

conditional_code = {
	"LT" : '1',
	"LE" : '2',
	"GT" : '3',
	"GE" : '4',
	"EQ" : '5',
	"ANY": '6'	
}
assembler_derecitve = {
	"START": "",
	"END"  : "",
	"DC"   : "",
	"DS"   : ""
}

symbol_table = {}

literal_table = {}

LC = 000

with open("code.txt") as f:
	for line in f:
		words = line.strip('\n').split(' ')
		print words
		for i in words:
			if i in register_table:
				print (register_table[i]),
			elif i in conditional_code:
				print (conditional_code[i]),
			elif i in assembler_derecitve:
				if i =="START":
					LC = 100
				if i =="END":
					for j in literal_table:
						literal_table[j]=LC
						LC=LC+1


			elif i in opcode_table:
				print (opcode_table[i]),
			else:
				if i[0].isalpha():
					if i in symbol_table and symbol_table[i]!="":
						print(symbol_table[i]),
					else:
						if words[0]==i:
							symbol_table[i]=LC
						else:
							symbol_table[i]=""
							print "S{0}".format(symbol_table.keys().index(i)),
				if i[0]=="=":
					literal_table[i]=""
					print "L{0}".format(literal_table.keys().index(i)),

		print "		LC:",LC	
		if i!="START" and i!="END":
			LC += 1
		
		print
f=open('output.txt', 'w')
f=f.write('',symbol_table)
f.close
print symbol_table
print literal_table
