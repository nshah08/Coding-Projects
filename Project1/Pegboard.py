import Board

def main():
    size=int(input("Input Size for the Board from 4-10 "))
    b = Board.board(size)
    b.create()
    print("1. Breadth First Search")
    print("2. Depth First Search")
    search=int(input("Put the number of the search you want to do! "))
    if search ==1:
        b.bfs()
    elif search ==2:
        b.dfs()




main()

