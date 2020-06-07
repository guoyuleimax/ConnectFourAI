# Hw 10, pr2 for CS 5 gold, 2016
#
# The Board class from CS 5 Hw #10
# for use as a starting point for
# Hw#11, the Player class (and AI)
#

import random
import time

class Board:
    """A datatype representing a C4 board
       with an arbitrary number of rows and cols.
    """

    def __init__(self, width = 7, height = 6):
        """The constructor for objects of type Board."""
        self.width = width
        self.height = height
        self.data = [[' '] * width for r in range(height)]

        # do not need to return inside a constructor!


    def __repr2__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''         # the string to return
        for row in range(self.height):
            s += '|'   # add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '-' * (self.width * 2) + '-\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)


        return s

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''         # the string to return
        for row in range(self.height):
            s += '|'   # add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '--' * self.width # add the bottom of the board
        s += '-\n'

        for col in range(self.width):
            s += ' ' + str(col%10)

        s += '\n'
        return s       # the board is complete, return it

    def set_board(self, LoS):
        """This method returns a string representation
           for an object of type Board.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = LoS[row][col]

    def setBoard(self, moves, show = True):
        """Sets the board according to a string
           of turns (moves), starting with 'X'.
           If show == True, it prints each one.
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
            if show:
                print(self)

    def set(self, moves, show = True):
        """Sets the board according to a string
           of turns (moves), starting with 'X'.
           If show==True, it prints each one.
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
            if show:
                print(self)

    def clear(self):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def addMove(self, col, ox):
        """Adds checker ox into column col.
           Does not need to check for validity;
           allowsMove will do that.
        """
        row = self.height - 1
        while row >= 0:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            row -= 1


    def winsFor(self, ox):
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row+1][col+1] == ox and \
                   self.data[row+2][col+2] == ox and \
                   self.data[row+3][col+3] == ox:
                    return True

        return False



    def addMove2(self, col, ox):
        """Adds checker ox into column col.
           Does not need to check for validity;
           allowsMove will do that.
        """
        for row in range(self.height):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def delMove(self, col):
        """Removes the checker from column col."""
        for row in range(self.height):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return


    def allowsMove(self, col):
        """Returns True if a move to col is allowed
           in the board represented by self;
           returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '

    def isFull(self):
        """Returns True if the board is completely full."""
        for col in range(self.width):
            if self.allowsMove(col):
                return False
        return True

    def gameOver(self):
        """Returns True if the game is over."""
        if self.isFull() or self.winsFor('X') or self.winsFor('O'):
            return True
        return False

    def isOX(self, row, col, ox):
        """Checks if the spot at row, col is legal and ox."""
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.data[row][col] == ox:
                    return True
        return False

    def winsFor(self, ox):
        """Checks if the board self is a win for ox."""
        for row in range(self.height):
            for col in range(self.width):
                if self.isOX(row, col, ox) and \
                   self.isOX(row+1, col, ox) and \
                   self.isOX(row+2, col, ox) and \
                   self.isOX(row+3, col, ox):
                    return True
                if self.isOX(row, col, ox) and \
                   self.isOX(row, col+1, ox) and \
                   self.isOX(row, col+2, ox) and \
                   self.isOX(row, col+3, ox):
                    return True
                if self.isOX(row, col, ox) and \
                   self.isOX(row+1, col+1, ox) and \
                   self.isOX(row+2, col+2, ox) and \
                   self.isOX(row+3, col+3, ox):
                    return True
                if self.isOX(row, col, ox) and \
                   self.isOX(row+1, col-1, ox) and \
                   self.isOX(row+2, col-2, ox) and \
                   self.isOX(row+3, col-3, ox):
                    return True
        return False

# Here is a version of hostGame for use in your Board class
#
# it simply alternates moves in the game and checks if
# the game is over at each move


    def hostGame(self):
        """Hosts a game of Connect Four."""

        nextCheckerToMove = 'X'

        while True:
            # print the board
            print(self)

            # get the next move from the human player...
            col = -1
            while not self.allowsMove(col):
                col = int(input('Next col for ' + nextCheckerToMove + ': '))
            self.addMove(col, nextCheckerToMove)

            # check if the game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'

        print('Come back soon 4 more!')



    def playGame(self, px, po, ss = False):
        """Plays a game of Connect Four.
            p1 and p2 are objects of type Player OR
            the string 'human'.
            If ss is True, it will "show scores" each time.
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = px

        while True:

            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = int(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            self.addMove(col, nextCheckerToMove)

            # check if game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = po
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = px

        print('Come back 4 more!')

    ###
    # Extention for our own game
    ###

    def playGameOwn(self, px, po, ss = False):
        """Plays a game of Connect Four.
            p1 and p2 are objects of type Player OR
            the string 'human'.
            If ss is True, it will "show scores" each time.

            Variance: 
            when 10 moves are made, the board will automatically change
            the top chess piences in each column from X to O or O to X;
            No change made for an empty column
        """

        print()
        print('Welcome to a different Connect 4 program!')
        print()
        time.sleep(2)
        

        nextCheckerToMove = 'X'
        nextPlayerToMove = px
        count = 0 # Establish a counter

        while True:

            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = int(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            self.addMove(col, nextCheckerToMove)
            count += 1
            if count == 10:
                for col in range(self.width):
                    for row in range(self.height):
                        if self.data[row][col] == ' ':
                            continue
                        else:
                            if self.data[row][col] == 'X':
                                self.delMove(col)
                                self.addMove(col,'O')
                            else:
                                self.delMove(col)
                                self.addMove(col,'X')
                            break
                count = 0
            

            # check if game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = po
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = px

        print('Come back 4 more!')

class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """ returns the other kind of checker or playing piece
        """
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'

    def scoreBoard(self,b):
        """Returns a single float value representing of the score of b (a board)"""
        if b.winsFor(self.ox) == True:
            return 100.0
        elif b.winsFor(self.oppCh()) == True:
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self,scores):
        """returns the col num of the highest score
           for a tie, returns the col num appropriate to the players' tbk type
        """
        smax = max(scores)
        L = []
        for n in range(len(scores)):
            if scores[n] == smax:
                L += [n]
        if len(L) == 1:
            return L[0]
        else:
            if self.tbt == 'LEFT':
                return L[0]
            elif self.tbt == 'RIGHT':
                return L[-1]
            else:
                x = random.choice(range(len(L)))
                return L[x]
    
    def scoresFor(self,b):
        """returns a list of scores, with the cth score representing the goodness of
           the input board after the player moves to column c
        """
        scores = [50]*b.width
        for col in range(b.width):
            if b.allowsMove(col) == False:
                scores[col] = -1.0
            elif b.winsFor(self.ox) == True:
                scores[col] = 100
            elif b.winsFor(self.oppCh()) == True:
                scores[col] = 0
            else:
                if self.ply == 0:
                    continue
                else:
                    b.addMove(col,self.ox)
                    if b.winsFor(self.ox) == True:
                        scores[col] = 100
                    elif b.winsFor(self.oppCh()) == True:
                        scores[col] = 0
                    else:
                        op = Player(self.oppCh(),self.tbt,self.ply-1)
                        scoresop = op.scoresFor(b) # 7 scores for op
                        maxsop = max(scoresop)
                        scores[col]=100-maxsop
                    b.delMove(col)
        return scores

    def nextMove(self,b):
        """ returns an integer of col number that the calling object chooses to move on
        """
        return self.tiebreakMove(self.scoresFor(b))

    





            

    

    