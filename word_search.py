class Solution:
    done = False
    visited = []
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        
        def validate(board,word,r,c):
            temp = word[1:] 
            # print("in validate", r, c, temp)

            for t in range(len(temp)):
                if c+1<col:
                    if board[r][c+1] == temp[t] and (r,c+1) not in self.visited:
                        if len(temp) == 1:
                            self.visited.append((r,c+1))
                            self.done = True
                            print("c+1 good",temp[t])
                            print("word exist!")
                            return
                        self.visited.append((r,c+1))
                        print("c+1 good",temp[t])
                        validate(board,word[1:],r,c+1)
                if c-1>0:
                    if board[r][c-1] == temp[t] and (r,c-1) not in self.visited:
                        if len(temp) == 1:
                            self.visited.append((r,c-1))
                            self.done = True
                            print("c-1 good",temp[t])
                            print("word exist!")
                            return
                        self.visited.append((r,c-1))
                        print("c-1 good",temp[t])
                        validate(board,word[1:],r,c-1)
                if r+1<row:
                    if board[r+1][c] == temp[t] and (r+1,c) not in self.visited:
                        if len(temp) == 1:
                            self.visited.append((r+1,c))
                            self.done = True
                            print("r+1 good",temp[t])
                            print("word exist!")
                            temp = None
                            return
                        self.visited.append((r+1,c))    
                        print("r+1 good",temp[t])
                        validate(board,word[1:],r+1,c)
                if r-1>0:
                    if board[r-1][c] == temp[t] and (r-1,c) not in self.visited:
                        if len(temp) == 1:
                            self.visited.append((r-1,c))
                            self.done = True
                            print("r-1 good",temp[t])
                            print("word exist!")
                            return
                        self.visited.append((r-1,c))
                        print("r-1 good",temp[t])
                        validate(board,word[1:],r-1,c)
                
                if self.done != True:
                    print("return to main function")
                    return
                
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    print("start validate",word[0],r,c)
                    validate(board,word,r,c)
                    print("returned")
                    if self.done == True:
                        return self.done
                    
        return self.done
        