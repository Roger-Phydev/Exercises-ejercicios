const countSymbol = (array,symbol)=>{
    let n=0;
    array.forEach(item=>{
        if(item==symbol) n++; 
    })
    return n;
}
const whoWon = matrix=>{
    if(typeof(matrix)=="object"||matrix.length==3&&(typeof(matrix[0])=="object"||matrix[0].length==3)&&(typeof(matrix[1])=="object"||matrix[1].length==3)&&(typeof(matrix[2])=="object"||matrix[2].length==3)){
        let o = countSymbol(matrix[0],"O")+countSymbol(matrix[1],"O")+countSymbol(matrix[2],"O");
        let x = countSymbol(matrix[0],"X")+countSymbol(matrix[1],"X")+countSymbol(matrix[2],"X");
        let s = countSymbol(matrix[0]," ")+countSymbol(matrix[1]," ")+countSymbol(matrix[2]," ");
        if(o+x+s==9){
            if(Math.abs(o-x)<=1){//this is the case in which the game is consistent
                let wins=[];
                for(i in matrix){
                    if(countSymbol(matrix[i],"X")==3||countSymbol(matrix[i],"O")==3) {
                        wins.push(matrix[i][0]);
                        console.log(`row ${i}`);
                    }
                    else if(countSymbol([matrix[0][i],matrix[1][i],matrix[2][i]],"X")==3||countSymbol([matrix[0][i],matrix[1][i],matrix[2][i]],"O")==3) {
                        wins.push(matrix[0][i]);
                        console.log(`column ${i}`)
                    }         
                }
                if((matrix[0][0]==matrix[1][1]==matrix[2][2]||matrix[0][2]==matrix[1][1]==matrix[2][0])&&matrix[1][1]!=" ") {
                    wins.push(matrix[1][1]);
                    console.log("cross")
                }
                console.log(wins);
                if(countSymbol(wins,"X")==1&&countSymbol(wins,"O")==0) return "X wins";
                else if(countSymbol(wins,"O")==1&&countSymbol(wins,"X")==0) return "O wins";
                return "Tie";
            }
        }else{
            return "tu matriz solo debe contener symbolos de los siguientes: 'O','X' o ' '";
        }
    }else{
        return "asegurate de seguir el formato: matriz=[[a,b,c],[d,e,f],[g,h,i]]"
    }
}
let l =[["O"," ","X"],[" ","O","X"],[" ","X","O"]];
