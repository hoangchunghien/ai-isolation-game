
def minimax_decision(gameState, depth):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    best_score = float("-inf")
    best_move = None
    for m in gameState.get_legal_moves():
        
        # call has been updated with a depth limit
        v = min_value(gameState.forecast_move(m), depth - 1)
        if v > best_score:
            best_score = v
            best_move = m
    return best_move


def min_value(gameState, depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1  # by Assumption 2
    
    # New conditional depth limit cutoff
    if depth <= 0:  # "==" could be used, but "<=" is safer 
        return 0
    
    v = float("inf")
    for m in gameState.get_legal_moves():
        # the depth should be decremented by 1 on each call
        v = min(v, max_value(gameState.forecast_move(m), depth - 1))
    return v


def max_value(gameState, depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1  # by assumption 2
    
    # New conditional depth limit cutoff
    if depth <= 0:  # "==" could be used, but "<=" is safer 
        return 0
    
    v = float("-inf")
    for m in gameState.get_legal_moves():
        # the depth should be decremented by 1 on each call
        v = max(v, min_value(gameState.forecast_move(m), depth - 1))
    return v

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    moves_available = bool(gameState.get_legal_moves())  # by Assumption 1
    return not moves_available