from flask import Flask,render_template,request
import os
app=Flask(__name__)
picFolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolder
pic1=os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpeg')

@app.route('/')
def index():
    return render_template("index.html")
@app.route("/solve",methods=['GET', 'POST'])
def solve():
    grid = []

    for i in range(1, 10):
        row = []
        for j in range(1, 10):
            input = f"{i}{j}"
            cell= request.form.get(input, '')
            row.append(cell)
        grid.append(row)
    print("succeessfully stored")
    def isvalid(row,col,c,grid):
        for i in range(len(grid)):
            if grid[row][i]==c:
                return False
            if grid[i][col]==c:
                return False
            if grid[(3*(row//3)+i//3)][3*(col//3)+i%3]==c:
                return False
        return True
    def sudukoChecker(grid):
        import collections
        rows=collections.defaultdict(list)
        cols=collections.defaultdict(list)
        squares=collections.defaultdict(list)

        print(rows,cols,squares)
        for i in range(9):
            for j in range(9):
                
                
                if grid[i][j]!='' :
                    try:
                        if not 0<int(grid[i][j])<=9:
                            return 0
                    except Exception as e:
                        print(e)
                        return 0
                    if (grid[i][j] not in rows[i]) and (grid[i][j] not in cols[j]) and (grid[i][j] not in squares[(i//3,j//3)]):
                        print("entered",i,j)
                        rows[i].append(grid[i][j])
                        cols[j].append(grid[i][j])
                        squares[(i//3,j//3)].append(grid[i][j])
                    else:
                        print(rows[i],cols[j],squares[(i,j)])
                        return 0
        print("going to main function")
        return solveSuduko(grid)
        


    def solveSuduko(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j]=='':
                    for c in range(1,10):
                        c=str(c)
                        if isvalid(i,j,c,grid):
                            grid[i][j]=c
                            if solveSuduko(grid)==True:
                                 return True
                            else:
                                grid[i][j]=''

                    return False
        return True
   
    if sudukoChecker(grid):
        return render_template('result.html', sudoku_values=grid)
    else:
        return render_template('wronginput.html',pic1=pic1)
if __name__=='__main__':
    app.run(debug=True)