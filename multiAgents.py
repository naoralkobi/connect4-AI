"""
Introduction to Artificial Intelligence, 89570, Bar Ilan University, ISRAEL

Student name: Naor Alkobi
Student ID: 315679985

"""

# multiAgents.py
# --------------
# Attribution Information: part of the code were created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# http://ai.berkeley.edu.
# We thank them for that! :)


import random, util, math

from connect4 import Agent, GameState


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all oMinmaxAgent your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth='2'):
        self.index = 1 # agent is always index 1
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class BestRandom(MultiAgentSearchAgent):

    def getAction(self, gameState):

        return gameState.pick_best_move()


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 1)
    """

    def min_max_decision(self, gameState):
        valid_location = gameState.getLegalActions()
        best_score = -math.inf
        best_col = random.choice(valid_location)

        for col in valid_location:

            # Create a copy of the game state
            self.depth -= 1
            gameState.switch_turn(gameState.get_piece_player())
            temp_state = gameState.generateSuccessor(gameState.get_piece_player(), col)
            score, move = self.min_max_decision(temp_state)


            if type(score) is tuple:
                score = score[0]
            if score > best_score:
                best_score = score
                best_col = col
        return best_score, best_col



    def getAction(self, gameState):
        """
        Returns self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent

        geameState.generateSuccessor(agentIndex, action):
        Returns the successor game stat after an agent takes an action

        gameState.isWin():
        Returns whether or not the game state is a winning state for the current turn player

        gameState.isLose():
        Returns whether or not the game state is a losing state for the current turn player

        gameState.is_terminal()
        Return whether or not that state is terminal
        """

        if gameState.is_terminal() or self.depth == 0:
            print("current score is + %s" % str(gameState.getScore()))
            return gameState.getScore(), None

        valid_location = gameState.getLegalActions()

        # case Agent - the maximizing player
        if self.index:
            best_score = -math.inf
            best_col = random.choice(valid_location)
            for col in valid_location:
                # Create a copy of the game state
                self.depth -= 1
                gameState.switch_turn(gameState.get_piece_player())
                temp_state = gameState.generateSuccessor(gameState.get_piece_player(), col)
                score, move = self.getAction(temp_state)
                if type(score) is tuple:
                    score = score[0]
                if score > best_score:
                    best_score = score
                    best_col = col
            return best_score, best_col
        # case player
        else:
            best_score = math.inf
            best_col = random.choice(valid_location)
            for col in valid_location:
                # Create a copy of the game state
                self.depth -= 1
                gameState.switch_turn(gameState.get_piece_player())
                temp_state = gameState.generateSuccessor(gameState.get_piece_player(), col)
                score, move = self.getAction(temp_state)
                if type(score) is tuple:
                    score = score[0]
                if score < best_score:
                    best_score = score
                    best_col = col
            return best_score, best_col


class AlphaBetaAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        """
            Your minimax agent with alpha-beta pruning (question 2)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()
