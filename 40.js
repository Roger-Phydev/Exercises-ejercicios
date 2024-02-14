const drawPascalTriangle = side=>{
    try{
        side=parseFloat(side);
    } catch{
        return "debes meter un número"
    }
    if(side==Math.floor(side)&&side>=0){
        let pascal
        if(side==0){
            pascal = [[1]];
        }else if(side==1){
            pascal = [[1],[1,1]]
        } else{
            pascal = [[1],[1,1]];
            for(let i=2;i<=side;i++){
                let row = [1];
                for(let j=0;j<pascal[i-1].length-1;j++){
                    row.push(pascal[i-1][j]+pascal[i-1][j+1]);
                }
                row.push(1);
                pascal.push(row);
            }
        }
        let m=0;
        pascal.at(-1).forEach(element => {
            m=Math.max(m,element.toString().length);
        });
        for(let index in pascal){
            let space = m*(side-index);
            let line = "".padStart(space," ");
            pascal[index].forEach(element => {
                line+=element.toString().padStart(m," ");
                line+="".padEnd(m," ");
            });
            console.log(line);
        }
        return pascal;
    } else{
        return "el lado debe ser mayor a cero y entero";
    }
}
