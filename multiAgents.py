import random, util, math
from connect4 import Agent, GameState

def scoreEvaluationFunction(currentGameState):
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn = 'scoreEvaluationFunction', depth='2'):
        self.index = 1 # agent is always index 1
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
class BestRandom(MultiAgentSearchAgent):

    def getAction(self, gameState):

        return gameState.pick_best_move()


class MinimaxAgent(MultiAgentSearchAgent):
    def min_max_decision(self, gameState, current_depth):
        # switch turn.
        gameState.switch_turn(current_depth)
        if gameState.is_terminal() or self.depth == current_depth:
            return self.evaluationFunction(gameState), None

        valid_location = gameState.getLegalActions()
        best_col = random.choice(valid_location)
        if gameState.turn == self.index:
            best_score = -math.inf
            for col in valid_location:
                temp_state = gameState.generateSuccessor(gameState.turn, col)
                score = self.min_max_decision(temp_state, current_depth + 1)[0]
                if score > best_score:
                    best_score = score
                    best_col = col
            return best_score, best_col
        else:
            best_score = math.inf
            for col in valid_location:
                temp_state = gameState.generateSuccessor(gameState.turn, col)
                score = self.min_max_decision(temp_state, current_depth + 1)[0]
                if score < best_score:
                    best_score = score
                    best_col = col
            return best_score, best_col

    def getAction(self, gameState):
        best_score, best_col = self.min_max_decision(gameState, 0)
        return best_col


class AlphaBetaAgent(MultiAgentSearchAgent):

    def min_max_decision_ab(self, gameState, current_depth, alpha, beta):
        # switch turn.
        gameState.switch_turn(current_depth)
        if gameState.is_terminal() or self.depth == current_depth:
            return self.evaluationFunction(gameState), None

        valid_location = gameState.getLegalActions()
        best_col = random.choice(valid_location)
        if gameState.turn == self.index:
            best_score = -math.inf
            for col in valid_location:
                temp_state = gameState.generateSuccessor(gameState.turn, col)
                score = self.min_max_decision_ab(temp_state, current_depth + 1, alpha, beta)[0]
                if score > best_score:
                    best_score = score
                    best_col = col
                if alpha > score:
                    alpha = score
                if beta < alpha:
                    break
            return best_score, best_col
        else:
            best_score = math.inf
            for col in valid_location:
                temp_state = gameState.generateSuccessor(gameState.turn, col)
                score = self.min_max_decision_ab(temp_state, current_depth + 1, alpha, beta)[0]
                if score < best_score:
                    best_score = score
                    best_col = col
                if beta < score:
                    beta = score
                if beta < alpha:
                    break
            return best_score, best_col

    def getAction(self, gameState):
        alpha = -math.inf
        beta = math.inf
        best_score, best_col = self.min_max_decision_ab(gameState, 0, alpha, beta)
        return best_col

class ExpectimaxAgent(MultiAgentSearchAgent):
    def expectiminimax(self, gameState, current_depth):
        # switch turn.
        gameState.switch_turn(current_depth)
        if gameState.is_terminal() or self.depth == current_depth:
            return self.evaluationFunction(gameState), None

        valid_location = gameState.getLegalActions()
        best_col = random.choice(valid_location)
        if gameState.turn == self.index:
            best_score = -math.inf
            for col in valid_location:
                temp_state = gameState.generateSuccessor(gameState.turn, col)
                score = self.expectiminimax(temp_state, current_depth + 1)[0]
                if score > best_score:
                    best_score = score
                    best_col = col
            return best_score, best_col
        else:
            best_score = 0
            for col in valid_location:
                p = 1 / len(valid_location)
                temp_state = gameState.generateSuccessor(gameState.turn, col)
                best_score += p * self.expectiminimax(temp_state, current_depth + 1)[0]
            return best_score, best_col

    def getAction(self, gameState):
        best_score, best_col = self.expectiminimax(gameState, 0)
        return best_col