# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from abc import ABC, abstractmethod

import util


class SearchProblem(ABC):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    @abstractmethod
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    @abstractmethod
    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    recorrido = []
    por_visitar = util.Stack()
    visitados = set()
    por_visitar.push((problem.getStartState(), recorrido))

    while not por_visitar.isEmpty():
        estado, recorrido = por_visitar.pop()

        if not problem.isGoalState(estado):
            visitados.add(estado)

            for e in problem.getSuccessors(estado):
                if e[0] not in visitados:
                    por_visitar.push((e[0], recorrido + [e[1]]))
        else:
            break
    return recorrido


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    recorrido = []
    por_visitar = util.Queue()
    visitados = set()
    por_visitar.push((problem.getStartState(), recorrido))

    while not por_visitar.isEmpty():
        estado, recorrido = por_visitar.pop()
        #print(f'NUEVO ESTADO: {estado}')
        if estado not in visitados:
            #print(f'RECORRIDO HASTA AQUI: {recorrido}')

            if not problem.isGoalState(estado):
                visitados.add(estado)
                #print(f'AÑADIDO A VISITADOS: {estado}')

                for e in problem.getSuccessors(estado):
                    #print(f'EL SUCESOR QUE AÑADO: {(e[0], recorrido+[e[1]])}')
                    por_visitar.push((e[0], recorrido+[e[1]]))
            else: break
    #print(f'MI RECORRIDO FINAL: {recorrido}')
    return recorrido


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    recorrido = []
    coste_acumulado=0
    coste_nuevo=0
    por_visitar = util.PriorityQueue()
    visitados = set()
    por_visitar.push((problem.getStartState(), recorrido, coste_acumulado), coste_acumulado)

    while not por_visitar.isEmpty():
        estado, recorrido, coste_acumulado = por_visitar.pop()

        if estado not in visitados:
            if not problem.isGoalState(estado):
                visitados.add(estado)

                for e in problem.getSuccessors(estado):
                    coste_nuevo=coste_acumulado+e[2]
                    por_visitar.push((e[0], recorrido+[e[1]], coste_nuevo), coste_nuevo)
            else: break
    return recorrido


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    recorrido = []
    coste_acumulado=0
    por_visitar = util.PriorityQueue()
    visitados = set()
    start=problem.getStartState()

    dist = heuristic(start, problem) + coste_acumulado
    por_visitar.push((start, recorrido, coste_acumulado+0), dist)

    while not por_visitar.isEmpty():
        estado, recorrido, coste_acumulado = por_visitar.pop()

        if estado not in visitados:
            if not problem.isGoalState(estado):
                visitados.add(estado)

                for e in problem.getSuccessors(estado):
                    dist = heuristic(e[0], problem) + coste_acumulado + e[2]
                    por_visitar.push((e[0], recorrido+[e[1]], coste_acumulado + e[2]), dist)
            else: break
    return recorrido


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
