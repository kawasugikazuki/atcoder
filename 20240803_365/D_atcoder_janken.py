# 貪欲法 今の最適解を探す方法 この問題では正しくない
N = int(input())
s = input()

# 前の手を初期化
previous_move = None

# 勝ち数をカウントする変数
win_count = 0

for move in s:
    if move == 'R':
        # 相手がグーなら、パーかグーを出す
        if previous_move != 'P':
            my_move = 'P'
        else:
            my_move = 'R'
    elif move == 'S':
        # 相手がチョキなら、グーかチョキを出す
        if previous_move != 'R':
            my_move = 'R'
        else:
            my_move = 'S'
    elif move == 'P':
        # 相手がパーなら、チョキかパーを出す
        if previous_move != 'S':
            my_move = 'S'
        else:
            my_move = 'P'
    
    # 勝てるか引き分けになるかを判定
    if (move == 'R' and my_move == 'P') or (move == 'S' and my_move == 'R') or (move == 'P' and my_move == 'S'):
        win_count += 1
    
    # 前の手を更新
    previous_move = my_move

print(win_count)
