#Static Table
OPCODE_TABLE = {
	"HALT"	:'00',
	"ADD"	:'01',
	"SUB"	:'02',
	"MULT"	:'03',
	"MOVER"	:'04',
	"MOVEM"	:'05',
	"COMP "	:'06',
	"BC"	:'07', #JUMP
	"DIV"	:'08',
	"READ"	:'09',
	"PRINT"	:'10'
}

REGISTER_TABLE = {
	"AREG"	:'1',
	"BREG"	:'2',
	"CREG"	:'3',
	"DREG"	:'4'
}

CONDITIONALS = {
	"LT" :'1',
	"LE" :'2',
	"GT" :'3',
	"GE" :'4',
	"EQ" :'5',
	"ANY":'6'
}

ASSEMBLER_DIR = {
	"START" : 'NULL',
	"END"	: 'NULL',
}

DECLARATIVES = {
	"DS" : 'NULL',
	"DC" : 'NULL'
}

#Dynamic Tables
SYMBOL_TABLE = [[],[]]
LITERAL_TABLE = {}


def CHECK(word):
	'''
	CHECKS IF THE WORD IS A REGISTER/CONDITIONAL/SYMBOL.
	'''
	if word in REGISTER_TABLE:
		return REGISTER_TABLE[word]
			
	elif word in CONDITIONALS:
		return CONDITIONALS[word]

	elif word[0] == '=' :
		if word in LITERAL_TABLE:
			return LITERAL_TABLE[word]
		else:
			LITERAL_TABLE[word] = "L"+str((len(LITERAL_TABLE)+1))
			return LITERAL_TABLE[word]

	else:
		#If present return
		if word in SYMBOL_TABLE[0]:
			idx  = SYMBOL_TABLE[0].index(word)
			return SYMBOL_TABLE[1][idx]
		else:
			SYMBOL_TABLE[0].append(word)
			SYMBOL_TABLE[1].append("S"+str((len(SYMBOL_TABLE[0])+1)))
			return SYMBOL_TABLE[1][-1]

LC = 000
with open("code.txt") as f, open(".output1.txt", "w+") as out:
	for line in f:
		line = line.strip('\n').split(' ')
		IC  = ["" for _ in range(len(line))]
		
		# if line[0][-1] == ':' :
		# 	print()
		# 	print(*line, sep='\t')
		# else:
		# 	print("\n   ",*line, sep='\t')


		#If first word is a LABEL
		if line[0][-1] == ':' :
			SYMBOL_TABLE[0].append(line[0][:-1])
			SYMBOL_TABLE[1].append(LC)
			line.pop(0)


		#If first word is an opcode
		if line[0] in OPCODE_TABLE:
			LC+=1
			IC[0] = OPCODE_TABLE[line[0]]
			#To check HALT opcode as length is 1
			if len(line) > 1:
				IC[1] = CHECK(line[1])
				if len(line) == 3:
					IC[2] = CHECK(line[2])

			IC.insert(0,LC)
			#print(*IC, sep='\t')
			print(*IC, sep='\t', file = out)


		#Else if Assembler Directive
		elif line[0] in ASSEMBLER_DIR:
			if line[0] == 'START':
				if len(line) == 1:
					LC = 0
				else:
					LC = int(line[1]) - 1

		#To avoid index out of range.
		if len(line) == 3:
			#For declartive Statements
			if line[1] in DECLARATIVES:
				LC+=1
				if line[0] in SYMBOL_TABLE[0]:
					idx = SYMBOL_TABLE[0].index(line[0])
					SYMBOL_TABLE[1][idx] = LC
				else:
					SYMBOL_TABLE[0].append(line[0])
					SYMBOL_TABLE[1].append(LC)
				
		if line[0] == 'ORIGIN':
			LC = int(line[1]) - 1


# print("\n\nSYMBOL_TABLE = ", SYMBOL_TABLE)
# print("LITERAL_TABLE = ", LITERAL_TABLE)
# print("LC = ", LC)
