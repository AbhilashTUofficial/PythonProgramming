# Queen Backtraking Problem

def isValidState(state):
    # Check if it is a valid solution.
    return True;

def getCandidates(state):
    # Return all possible slots for the Queen.
    return [];

def search(state,solutions):
    if isValidState(state):
        solutions.append(state.copy());

    for candidate in getCandidates(state):
        state.add(candidate);
        search(state,solutions);
        state.remove(candidate);

def solve():
    solutions=[];
    state=set();
    search(state,solutions);
    return solutions;

