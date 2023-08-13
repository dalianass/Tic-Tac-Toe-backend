
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'


def minimax(board, depth, isMaximizingPlayer, alpha, beta):
    if proveriPobedu(board):
        return evaluate(board, depth)

    if isMaximizingPlayer:
        maxEval = float('-inf')
        bestMove = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = AI_PLAYER
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ''
                    if eval > maxEval:
                        maxEval = eval
                        bestMove = (i, j)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        if depth == 0:
            return bestMove
        return maxEval
    else:
        minEval = float('inf')
        bestMove = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = HUMAN_PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ''
                    if eval < minEval:
                        minEval = eval
                        bestMove = (i, j)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        if depth == 0:
            return bestMove
        return minEval


def proveriPobedu(board):
    # provera redova
    for i in range(3):
        if board[i][0] != '' and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return True

    # provera kolona
    for i in range(3):
        if board[0][i] != '' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True

    # provera dijagonala
    if board[0][0] != '' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True

    if board[0][2] != '' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True

    # provera za slucaj 'nereseno'
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False  # tabla jos nije popunjena
    return True  # Nereseno je

def evaluate(board, depth):
    # redovi
    for i in range(3):
        if board[i][0] != '' and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return 10 - depth if board[i][0] == AI_PLAYER else depth - 10

    # kolone
    for i in range(3):
        if board[0][i] != '' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return 10 - depth if board[0][i] == AI_PLAYER else depth - 10

    # dijagonale
    if board[0][0] != '' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return 10 - depth if board[0][0] == AI_PLAYER else depth - 10

    if board[0][2] != '' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return 10 - depth if board[0][2] == AI_PLAYER else depth - 10

    return 0  # nereseno je