def solution(board, h, w):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cur = board[h][w]
    answer = 0
    length = len(board)
    
    for i in range(4):
        cx, cy = h+dx[i], w+dy[i]
        if cx>=0 and cx<length and cy >=0 and cy<length:
            if cur == board[cx][cy]:
                answer+=1
        
    return answer