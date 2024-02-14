const whoWonRPS = playsArray =>{
    if(Array.isArray(playsArray)&&playsArray.length>0){
        let result=0;
        let posibilities = [["R","P","S"],["S","R","P"]];
        for (play of playsArray){
            if(!Array.isArray(play)||play.length!=2){
                return "formato equivocado, debe ser array con arrays de dos elementos";
            }else if(!["S","R","P"].includes(play[0])||!["S","R","P"].includes(play[1])){
                return "error, cada array solo debe tener 'R','S' o 'P'";
            } else{
                for(let j=0;j<6;j++){
                    if(j<3){
                        if(play[0]==posibilities[0][j]&&play[1]==posibilities[1][j]){
                            result++;
                        }
                    }else{
                        if(play[0]==posibilities[1][j-3]&&play[1]==posibilities[0][j-3]){
                            result--;
                        }
                    }
                }
            }
        }
        if(result>0) {return "Player 1 wins";}
        else if(result<0) {return "Player 2 wins";}
        else {return "Tie";}
    }else return "debes introducir un array";
}
let a =[[1,2],[4,2]];
console.log(a.indexOf([1,2]));