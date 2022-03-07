import pygame
import random
import time


pygame.init()
length = 800
length = 10* int(length/10)
#length = int(input("What size should the screen be:"))
width,height = length,length

BoardLength = length*0.8

Screen = pygame.display.set_mode((width,height))

class Board:
    def __init__(self):
        self.Length = BoardLength
        self.StartingX = ((width-self.Length)/2)
        self.StartingY = ((height-self.Length)/3)
        self.SquareLength = self.Length/8
        self.Light = 1
        self.color1 = (181,136,99)
        self.color2 = (240,217,181)
        
    def Draw(self):
        for i in range(0,64):
            pygame.draw.rect(Screen,self.Color(i),(self.Pos("X",i),self.Pos("Y",i),self.SquareLength,self.SquareLength))
            
    def Color(self,number):
        if (number % 8) == 0:
            self.SwapCol()
        if self.Light == 1:
            self.Light = self.Light * -1
            return self.color1
        else:
            self.Light = self.Light * -1
            return self.color2
    def SwapCol(self):
        if self.color1 == (181,136,99):
            self.color1 = (240,217,181)
            self.color2 = (181,136,99)
        else:
            self.color1 = (181,136,99)
            self.color2 = (240,217,181)
    def Pos(self,XY,number):
        if XY == "X" or XY == "x":
            return Board.StartingX + (number % 8)*Board.SquareLength
        elif XY == "Y" or XY == "y":
            return Board.StartingY + (int(number / 8)*Board.SquareLength)
    

class Pieces:
    def __init__(self,PieceType,X,Y):
        self.PieceTypeLoader = PieceType
        self.X = X
        self.Y = Y
        self.Locked = True
        self.IsDead = False
        self.HasMoved = False
        self.PotentialMoves = []
        self.LoadPiece()
    def LoadPiece(self):
        if self.PieceTypeLoader == "WRook":
            self.Piece = pygame.image.load('Pieces\WRook.png')
            self.Color = "White"
            self.PieceType = "Rook"
            self.rules = [[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)],[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)],[(0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7)],[(-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0)]]
        elif self.PieceTypeLoader == "WQueen":
            self.Piece = pygame.image.load('Pieces\WQueen.png')
            self.Color = "White"
            self.PieceType = "Queen"
            self.rules = [[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)],[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)],[(0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7)],[(-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0)],[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)],[(1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7)],[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7)],[(-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7)]]
        elif self.PieceTypeLoader == "WPawn":
            self.Piece = pygame.image.load('Pieces\WPawn.png')
            self.Color = "White"
            self.PieceType = "Pawn"
        elif self.PieceTypeLoader == "WKing":
            self.Piece = pygame.image.load('Pieces\WKing.png')
            self.Color = "White"
            self.PieceType = "King"
            self.rules = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        elif self.PieceTypeLoader == "WHorse":
            self.Piece = pygame.image.load('Pieces\WHorse.png')
            self.Color = "White"
            self.PieceType = "Horse"
            self.rules = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        elif self.PieceTypeLoader == "WBishop":
            self.Piece = pygame.image.load('Pieces\WBishop.png')
            self.Color = "White"
            self.PieceType = "Bishop"
            self.rules = [[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)],[(1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7)],[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7)],[(-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7)]]
        elif self.PieceTypeLoader == "BRook":
            self.Piece = pygame.image.load('Pieces\BRook.png')
            self.Color = "Black"
            self.PieceType = "Rook"
            self.rules = [[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)],[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)],[(0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7)],[(-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0)]]
        elif self.PieceTypeLoader == "BQueen":
            self.Piece = pygame.image.load('Pieces\BQueen.png')
            self.Color = "Black"
            self.PieceType = "Queen"
            self.rules = [[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)],[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)],[(0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7)],[(-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0)],[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)],[(1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7)],[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7)],[(-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7)]]
        elif self.PieceTypeLoader == "BPawn":
            self.Piece = pygame.image.load('Pieces\BPawn.png')
            self.Color = "Black"
            self.PieceType = "Pawn"
        elif self.PieceTypeLoader == "BKing":
            self.Piece = pygame.image.load('Pieces\BKing.png')
            self.Color = "Black"
            self.PieceType = "King"
            self.rules = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        elif self.PieceTypeLoader == "BHorse":
            self.Piece = pygame.image.load('Pieces\BHorse.png')
            self.Color = "Black"
            self.PieceType = "Horse"
            self.rules = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        elif self.PieceTypeLoader == "BBishop":
            self.Piece = pygame.image.load('Pieces\BBishop.png')
            self.Color = "Black"
            self.PieceType = "Bishop"
            self.rules = [[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)],[(1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7)],[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7)],[(-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7)]]
            self.MaxDistance = 7
        self.Piece = pygame.transform.scale(self.Piece,(Board.SquareLength,Board.SquareLength))
    def Draw(self):
        if self.IsDead == False:
            Screen.blit(self.Piece,(NumToCords("X",self.X),NumToCords("Y",self.Y)))
        else:
            return





    
    
class GameLoop:
    def __init__(self):
        self.Turn = 1
        self.IsPieceChosen = False
        self.SelectedPiece = "EMPTY"
        self.SelectedTarget = "EMPTY"
        self.OutOfScreen = (-1*Board.SquareLength,-1*Board.SquareLength)
        self.YellowBox = self.OutOfScreen
    def Clicked(self, pos):
        if self.IsPieceChosen == False:
            self.SelectedPiece = self.FindPiece(pos)
            if self.SelectedPiece == "No Piece":
                return
            if self.IsPieceCorrectColor() == True:
                self.IsPieceChosen = True
                self.YellowBox = (self.SelectedPiece.X,self.SelectedPiece.Y)
        else:
            self.SelectedTarget = self.FindPiece(pos)
            self.SelectedX = CordsToNum("X",pos[0])
            self.SelectedY = CordsToNum("Y",pos[1])
            if (pos[0]< Board.StartingX) or (pos[0]> Board.StartingX+BoardLength) or (pos[1] < Board.StartingY) or (pos[1] > Board.StartingY+BoardLength):
                return
            elif self.SelectedTarget == "No Piece":
                self.Enemy = False
                if self.LegalMove(pos) == True:
                    self.SelectedPiece.HasMoved = True
                    self.SelectedPiece.X = CordsToNum("X",pos[0])
                    self.SelectedPiece.Y = CordsToNum("Y",pos[1])
                    self.SelectedPiece = "EMPTY"
                    self.SelectedTarget = "EMPTY"
                    self.IsPieceChosen = False
                    self.YellowBox = self.OutOfScreen
                    self.Turn = self.Turn + 1
                    return
                else:
                    print("Illegal Move!")
                    self.SelectedPiece = "EMPTY"
                    self.SelectedTarget = "EMPTY"
                    self.IsPieceChosen = False
                    self.YellowBox = self.OutOfScreen
                    return
            elif self.SelectedTarget.Color == self.SelectedPiece.Color:
                self.SelectedPiece = self.SelectedTarget
                self.YellowBox = (self.SelectedPiece.X,self.SelectedPiece.Y)
                self.IsPieceChosen = True
                return
            else:
                self.Enemy = True
                if self.LegalMove(pos) == True:
                    self.SelectedPiece.HasMoved = True
                    self.SelectedTarget.X = -1
                    self.SelectedTarget.Y = -1
                    self.SelectedTarget.isDead = True
                    self.SelectedPiece.X = CordsToNum("X",pos[0])
                    self.SelectedPiece.Y = CordsToNum("Y",pos[1])
                    self.SelectedPiece = "EMPTY"
                    self.SelectedTarget = "EMPTY"
                    self.IsPieceChosen = False
                    self.YellowBox = self.OutOfScreen
                    self.Turn = self.Turn + 1
                    return
                else:
                    print("Illegal Move!")
                    self.SelectedPiece = "EMPTY"
                    self.IsPieceChosen = False
                    self.YellowBox = self.OutOfScreen
                    return


    def LegalMove(self,pos):
        self.NewX = CordsToNum("X",pos[0])
        self.NewY = CordsToNum("Y",pos[1])
        if self.SelectedPiece.PieceType == "Pawn":
            if self.SelectedPiece.Color == "White":
                self.XDis = self.NewX - self.SelectedPiece.X
                self.YDis = self.NewY - self.SelectedPiece.Y
                self.YForPawn = self.SelectedPiece.Y + 1
            else:
                self.XDis =  self.SelectedPiece.X - self.NewX
                self.YDis =  self.SelectedPiece.Y - self.NewY
                self.YForPawn = self.SelectedPiece.Y - 1
            if (self.XDis != 0):
                if self.Enemy == False:
                    return False
                elif (self.XDis == 1 or self.XDis == -1) and self.YDis == 1:
                    return True
                else:
                    return False
            else:
                if self.YDis == 1:
                    if self.Enemy == False:
                        return True
                    else:
                        return False
                elif (self.YDis == 2):
                    if self.BetterPieceFinder(self.SelectedPiece.X,self.YForPawn) == True:
                        return False
                    else:
                        if self.SelectedPiece.HasMoved == False:
                            return True
                        else:
                            return False
                    
                else:
                    return False
        elif self.SelectedPiece.PieceType == "Queen" or self.SelectedPiece.PieceType == "Bishop" or self.SelectedPiece.PieceType == "Rook":
            if self.SelectedPiece.Color == "White":
                self.XDis = self.NewX - self.SelectedPiece.X
                self.YDis = self.NewY - self.SelectedPiece.Y
            else:
                self.XDis =  self.SelectedPiece.X - self.NewX
                self.YDis =  self.SelectedPiece.Y - self.NewY
            for i in self.SelectedPiece.rules:
                sufficient = True
                for j in range(0,len(i)):
                    if i[j][0] == self.XDis and i[j][1] == self.YDis and sufficient == True:
                        return True
                    if self.SelectedPiece.Color == "White":
                        self.FindPieceLocation = self.BetterPieceFinder(self.SelectedPiece.X+i[j][0],self.SelectedPiece.Y+i[j][1])
                    else:
                        self.FindPieceLocation = self.BetterPieceFinder(self.SelectedPiece.X-i[j][0],self.SelectedPiece.Y-i[j][1])
                    if self.FindPieceLocation == True:
                        sufficient = False
            return False
        else:
            self.XDis = self.NewX - self.SelectedPiece.X
            self.YDis = self.NewY - self.SelectedPiece.Y
            for i in self.SelectedPiece.rules:
                if i[0] == self.XDis and i[1] == self.YDis:
                    return True
            else:
                return False
            
            
            
    def PlayerTurn(self):
        if (self.Turn % 2) != 0:
            return "White"
        else:
            return "Black"

    def FindPiece(self,POS):
        for i in Pieces:
            if i.X == CordsToNum("X",POS[0]) and i.Y == CordsToNum("Y",POS[1]):
                return i
        return "No Piece"
    def BetterPieceFinder(self,X,Y):
        for i in Pieces:
            if i.X == X and i.Y == Y:
                return True
        return False
    def IsPieceCorrectColor(self):
        if self.SelectedPiece.Color == self.PlayerTurn():
            return True
        else:
            return False
    def CreateYellowBox(self):
        pygame.draw.rect(Screen,(239, 245, 66),(NumToCords("X",self.YellowBox[0]),NumToCords("Y",self.YellowBox[1]),Board.SquareLength,Board.SquareLength))

def NumToCords(XY,number):
    if number == -1:
        return -1 * Board.SquareLength
    if XY == "X" or XY == "x":
        return Board.StartingX + number*Board.SquareLength - Board.SquareLength
    elif XY == "Y" or XY == "y":
        return (BoardLength + Board.StartingY) - number * Board.SquareLength
    
def CordsToNum(XY,number):
    if XY == "X" or XY == "x":
        number = number - Board.StartingX
        if number < 0 or number >= BoardLength:
            return -1
        else:
            return int(number/(BoardLength/8)) + 1
    if XY == "Y" or XY == "y":
        number = number - Board.StartingY
        if number < 0 or number > BoardLength:
            return -1
        else:
            return 8 - int(number/(BoardLength/8))

Board = Board()
BRook1 = Pieces("BRook",1,8)
BHorse1 = Pieces("BHorse",2,8)
BBishop1 = Pieces("BBishop",3,8)
BQueen = Pieces("BQueen",4,8)
BKing = Pieces("BKing",5,8)
BBishop2 = Pieces("BBishop",6,8)
BHorse2 = Pieces("BHorse",7,8)
BRook2 = Pieces("BRook",8,8)
BPawn1 = Pieces("BPawn",1,7)
BPawn2 = Pieces("BPawn",2,7)
BPawn3 = Pieces("BPawn",3,7)
BPawn4 = Pieces("BPawn",4,7)
BPawn5 = Pieces("BPawn",5,7)
BPawn6 = Pieces("BPawn",6,7)
BPawn7 = Pieces("BPawn",7,7)
BPawn8 = Pieces("BPawn",8,7)
WRook1 = Pieces("WRook",1,1)
WHorse1 = Pieces("WHorse",2,1)
WBishop1 = Pieces("WBishop",3,1)
WQueen = Pieces("WQueen",4,1)
WKing = Pieces("WKing",5,1)
WBishop2 = Pieces("WBishop",6,1)
WHorse2 = Pieces("WHorse",7,1)
WRook2 = Pieces("WRook",8,1)
WPawn1 = Pieces("WPawn",1,2)
WPawn2 = Pieces("WPawn",2,2)
WPawn3 = Pieces("WPawn",3,2)
WPawn4 = Pieces("WPawn",4,2)
WPawn5 = Pieces("WPawn",5,2)
WPawn6 = Pieces("WPawn",6,2)
WPawn7 = Pieces("WPawn",7,2)
WPawn8 = Pieces("WPawn",8,2)

Game = GameLoop()

Pieces = [BRook1,BHorse1,BBishop1,BQueen,BKing,BBishop2,BHorse2,BRook2,BPawn1,BPawn2,BPawn3,BPawn4,BPawn5,BPawn6,BPawn7,BPawn8,WRook1,WHorse1,WBishop1,WQueen,WKing,WBishop2,WHorse2,WRook2,WPawn1,WPawn2,WPawn3,WPawn4,WPawn5,WPawn6,WPawn7,WPawn8]

def DrawAllPieces():
    for x in Pieces:
        x.Draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                Game.Clicked(pygame.mouse.get_pos())
        Screen.fill((72, 71, 67))
        Board.Draw()
        Game.CreateYellowBox()
        DrawAllPieces()
        pygame.display.update()



        
