import chess as ch
import random as rd

def chess_notation_to_row_col(chess_notation):
    """
    Convert chess notation in the format of 'e2e4' to row and column numbers.
    Returns a tuple of integers in the format (start_row, start_col, end_row, end_col).
    """
    column_dict = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }
    start_col = column_dict[chess_notation[0]]
    start_row = int(chess_notation[1]) - 1
    end_col = column_dict[chess_notation[2]]
    end_row = int(chess_notation[3]) - 1
    return (start_row, start_col, end_row, end_col)


class Engine:

    def __init__(self, board, maxDepth, color):
        self.board=board
        self.color=color
        self.maxDepth=maxDepth
    
    def getBestMove(self):

        move = self.engine(None, 1);

        print("Selected move:", move , type(move))

        move_str = move.uci()
        print("move type : ",type(move_str))
        start_row, start_col, end_row, end_col = chess_notation_to_row_col(move_str)
        print("Notation in algebric format : ")
        print(start_row + 1, start_col + 1)  # Output: 2, 5
        print(end_row + 1, end_col + 1)  # Output: 4, 5

        return move


    def evalFunct(self):
        compt = 0
        #Sums up the material values
        for i in range(64):
            compt+=self.squareResPoints(ch.SQUARES[i])
        compt += self.mateOpportunity() + self.openning() + 0.001*rd.random()
        return compt

    def mateOpportunity(self):
        if (self.board.legal_moves.count()==0):
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0

    #to make the engine developp in the first moves
    def openning(self):
        if (self.board.fullmove_number<10):
            if (self.board.turn == self.color):
                return 1/30 * self.board.legal_moves.count()
            else:
                return -1/30 * self.board.legal_moves.count()
        else:
            return 0

    #Takes a square as input and 
    #returns the corresponding Hans Berliner's
    #system value of it's resident
    def squareResPoints(self, square):
        pieceValue = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

        if (self.board.color_at(square)!=self.color):
            return -pieceValue
        else:
            return pieceValue

        
    def engine(self, candidate, depth):
        
        #reached max depth of search or no possible moves
        if ( depth == self.maxDepth
        or self.board.legal_moves.count() == 0):
            return self.evalFunct()
        
        else:
            #get list of legal moves of the current position
            moveListe = list(self.board.legal_moves)
            
            #initialise newCandidate
            newCandidate = None
            #(uneven depth means engine's turn)
            if(depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")
            
            #analyse board after deeper moves
            for i in moveListe:

                #Play move i
                self.board.push(i)

                #Get value of move i (by exploring the repercussions)
                value = self.engine(newCandidate, depth + 1) 

                #Basic minmax algorithm:
                #if maximizing (engine's turn)
                if(value > newCandidate and depth % 2 != 0):
                    #need to save move played by the engine
                    if (depth == 1):
                        move=i
                    newCandidate = value
                #if minimizing (human player's turn)
                elif(value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                #Alpha-beta prunning cuts: 
                #(if previous move was made by the engine)
                if (candidate != None
                 and value < candidate
                 and depth % 2 == 0):
                    self.board.pop()
                    break
                #(if previous move was made by the human player)
                elif (candidate != None 
                and value > candidate 
                and depth % 2 != 0):
                    self.board.pop()
                    break
                
                #Undo last move
                self.board.pop()

            #Return result
            if (depth>1):
                #eturn value of a move in the tree
                return newCandidate
            else:
                #return the move (only on first move)
                return move