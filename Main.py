import ChessEngine as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    # play a move for a human player
    def playHumanMove(self):
        try:
            # display legal moves for the player
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")
            # get the player's move
            play = input("Your move: ")
            # allow the player to undo their last move
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            # push the player's move to the board
            self.board.push_san(play)
        except:
            # if there is an error, try again
            self.playHumanMove()

    # play a move for the game engine
    def playEngineMove(self, maxDepth, color):
        # create an engine object and get the best move
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())
      

    # start a new game
    def startGame(self):
        # get the color the human player wants to play as
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        # get the max depth for the engine's search
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Choose depth: """))
        # if the human player is playing as black
        if color=="b":
            # continue playing moves until there is a checkmate
            while (self.board.is_checkmate()==False):
                print("The engine is thinking...")
                # get the engine's move
                self.playEngineMove(maxDepth, ch.WHITE)
                # print the board and wait for the player's move
                print(self.board)
                self.playHumanMove()
                print(self.board)
            # print the final board and outcome
            print(self.board)
            print(self.board.outcome())    
        # if the human player is playing as white
        elif color=="w":
            # continue playing moves until there is a checkmate
            while (self.board.is_checkmate()==False):
                # print the board and wait for the player's move
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                # get the engine's move
                self.playEngineMove(maxDepth, ch.BLACK)
            # print the final board and outcome
            print(self.board)
            print(self.board.outcome())
        # reset the board for another game
        self.board.reset
        # start another game
        self.startGame()

# create a new board and start the game
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()


