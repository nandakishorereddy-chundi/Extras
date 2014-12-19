import random

""" Global variables for x and y co-ordinates of Pacman and Ghost """
xcoP=0
ycoP=0
xcoG=0
ycoG=0
score=0
expScore=0
fg=0
board=[['.' for x in xrange(36)] for x in xrange(16)]

def PrintBoard():
	""" Function for printing board """
	for x in xrange(16):
		if x!=0:
			print '\n'
		for y in xrange(36):
			print board[x][y],

def CoinsPosition():
	""" Insertion of 'C' in the board using rand function """
	cnt=40
	while cnt>0:
		a=random.randint(0,15)
		b=random.randint(0,35)
		if(board[a][b]=='.'):
			board[a][b]='C'
			cnt=cnt-1

def WallsPosition():
	""" Insertion of 'X' in the board using rand function """
	cnt=40
	while cnt>0:
		a=random.randint(0,15)
		b=random.randint(0,35)
		if(board[a][b]=='.'):
			board[a][b]='X'
			cnt=cnt-1

def SetPacman():
	""" Setting position of Pacman """
	fg=0
	global xcoP
	global ycoP
	while fg!=1:
		a=random.randint(0,15)
		b=random.randint(0,35)
		if(board[a][b]=='.'):
			board[a][b]='P'
			xcoP=a
			ycoP=b
			fg=1

def SetGhost():
	""" Setting position of Ghost """
	fg=0
	global xcoG
	global ycoG
	while fg!=1:
		a=random.randint(0,15)
		b=random.randint(0,35)
		if(board[a][b]!='C' and board[a][b]!='X' and board[a][b]!='P'):
			board[a][b]='G'
			xcoG=a
			ycoG=b
			fg=1

class Person:
	""" Person class which consists of CheckWall,CheckMove methods """
	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def CheckWall(self,move):
		""" CheckWall method returns true if wall is present and vice-versa """
		if(move=='w'):
			if(board[self.x-1][self.y]=='X'):
				return 0
			return 1
		elif(move=='s'):
			if(board[self.x+1][self.y]=='X'):
				return 0
			return 1
		elif(move=='d'):
			if(board[self.x][self.y+1]=='X'):
				return 0
			return 1
		elif(move=='a'):
			if(board[self.x][self.y-1]=='X'):
				return 0
			return 1

	def CheckMove(self,move):
		""" CheckMove method returns true if pacman or ghosts co-ordinates are with in the board or not """
		if(move=='w'):
			if(self.x==0):
				return 0
			return 1
		elif(move=='s'):
			if(self.x==15):
				return 0
			return 1
		elif(move=='d'):
			if(self.y==35):
				return 0
			return 1
		elif(move=='a'):
			if(self.y==0):
				return 0
			return 1

	""" Methods to move up,down,left,right """
	def MoveUp(self):
		self.x=self.x-1

	def MoveDown(self):
		self.x=self.x+1

	def MoveLeft(self):
		self.y=self.y-1

	def MoveRight(self):
		self.y=self.y+1

class Pacman(Person):
	""" Pacman is a class which is inherited from class Person """
	def __init__(self,x,y):
		Person.__init__(self,x,y)

	def CheckGhost(self,G):
		""" CheckGhost method returns true if game is over """
		if(P.x==G.x and P.y==G.y):
			return 1
		return 0

	def CheckCoin(self):
		""" CheckCoin method returns true if coin is present """
		if(board[self.x][self.y]=='C'):
			return 1
		return 0

	
class Ghost(Person):
	""" Ghost is a class which is inherited from class Person """
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.fg=0
		self.fg_next=0
		self.fg_prev=0

	def MoveGhost(self,P):
		""" MoveGhost is a method to move multiple ghosts """
		self.fg=0
		while(self.fg!=1):
			move=random.randint(1,4)
			if(move==1):
				if(self.CheckMove('w')!=0 and self.CheckWall('w')!=0):
					if(board[self.x-1][self.y]=='C'):
						self.fg_next=1
					else:
					 	self.fg_next=0
					if(self.fg_prev==1):
						board[self.x][self.y]='C'
					else:
					 	board[self.x][self.y]='.'
					self.fg_prev=self.fg_next
					self.MoveUp()
					board[self.x][self.y]='G'
					self.fg=1
			elif(move==2):
				if(self.CheckMove('s')!=0 and self.CheckWall('s')!=0):
					if(board[self.x+1][self.y]=='C'):
						self.fg_next=1
					else:
					 	self.fg_next=0
		 			if(self.fg_prev==1):
						board[self.x][self.y]='C'
					else:
				 		board[self.x][self.y]='.'	
					self.fg_prev=self.fg_next
					self.MoveDown()
					board[self.x][self.y]='G'
					self.fg=1
			elif(move==3):
				if(self.CheckMove('d')!=0 and self.CheckWall('d')!=0):
		 			if(board[self.x][self.y+1]=='C'):
						self.fg_next=1
					else:
					 	self.fg_next=0
					if(self.fg_prev==1):
						board[self.x][self.y]='C'
					else:
					 	board[self.x][self.y]='.'
					self.fg_prev=self.fg_next
		 			self.MoveRight()
					board[self.x][self.y]='G'
					self.fg=1
			elif(move==4):
				if(self.CheckMove('a')!=0 and self.CheckWall('a')!=0):
					if(board[self.x][self.y-1]=='C'):
						self.fg_next=1
					else:
				 		self.fg_next=0
					if(self.fg_prev==1):
						board[self.x][self.y]='C'
					else:
					 	board[self.x][self.y]='.'
					self.fg_prev=self.fg_next
			 		self.MoveLeft()
					board[self.x][self.y]='G'
					self.fg=1
			if((P.CheckGhost(self)==1)):
				board[self.x][self.y]=":("
				PrintBoard()
				print '\n'
				print "The game is over"
				print "score = {}".format(score)	
				break


def PlayGame(P,G1,G2,G3,G4):
	""" Function for playing game """
	global expScore
	global fg
	global score
	expScore=expScore+40
	fg=0
	PrintBoard()
	print '\n'
	while(1):
		print "Enter input:",
		inp=raw_input()
		if(inp=='w'):
			if(P.CheckMove('w')==0 or P.CheckWall('w')==0):
				print "-------------------------------------------cannot move, choose other choice-------------------------------------------"
			else:
			 	board[P.x][P.y]='.'
			 	P.MoveUp()
				if(P.CheckCoin()==1):
					score=score+1
			 	board[P.x][P.y]='P'
		elif(inp=='s'):
			if(P.CheckMove('s')==0 or P.CheckWall('s')==0):
				print "-------------------------------------------cannot move, choose other choice-------------------------------------------"
			else:
			 	board[P.x][P.y]='.'
		 		P.MoveDown()
				if(P.CheckCoin()==1):
					score=score+1
			 	board[P.x][P.y]='P'
		elif(inp=='d'):
			if(P.CheckMove('d')==0 or P.CheckWall('d')==0):
				print "-------------------------------------------cannot move, choose other choice-------------------------------------------"
			else:	
			 	board[P.x][P.y]='.'
			 	P.MoveRight()
				if(P.CheckCoin()==1):
					score=score+1
			 	board[P.x][P.y]='P'
		elif(inp=='a'):
			if(P.CheckMove('a')==0 or P.CheckWall('a')==0):
				print "-------------------------------------------cannot move, choose other choice-------------------------------------------"
			else:
			 	board[P.x][P.y]='.'
			 	P.MoveLeft()
				if(P.CheckCoin()==1):
					score=score+1
			 	board[P.x][P.y]='P'
		if((P.CheckGhost(G1)==1 or P.CheckGhost(G2)==1 or P.CheckGhost(G3)==1 or P.CheckGhost(G4)==1) or inp=='q' or expScore==score):
			if(inp=='q'):
				print "------------------------------------------- Quited Forcefully-------------------------------------------"
			elif(expScore==score):
				print "------------------------------------------- Game Restarts-------------------------------------------"
				fg=1
			else:
				board[P.x][P.y]=":("
				PrintBoard()
				print '\n'
				print "------------------------------------------- The Game is Over-------------------------------------------"
				print "score = {}".format(score)
			break
		
		""" Ghost Moves """
		G1.MoveGhost(P)
		G2.MoveGhost(P)
		G3.MoveGhost(P)
		G4.MoveGhost(P)
		PrintBoard()
		print '\n'
		print "score = {}".format(score)
		xcoP=P.x
		ycoP=P.y
if __name__ == '__main__' :
	WallsPosition()
	SetPacman()
	P=Pacman(xcoP,ycoP)
	SetGhost()
	G1=Ghost(xcoG,ycoG)
	SetGhost()
	G2=Ghost(xcoG,ycoG)
	SetGhost()
	G3=Ghost(xcoG,ycoG)
	SetGhost()
	G4=Ghost(xcoG,ycoG)
	""" while loop for re-starting game """
	while(1):
		CoinsPosition()
		PlayGame(P,G1,G2,G3,G4)
		if(fg==0):
			break
