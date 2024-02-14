const trickOrTreat = (trick,...peopleData)=>{
    if(trick==true){
        let options = ["🎃","👻","💀","🕷","🕸","🦇"];
        let scares = 0;
        let totalHeight = 0;
        peopleData.forEach(element => {
            if(element.length==3&&typeof(element[0])=="string"&&typeof(element[1])=="number"
            &&Math.floor(element[1])==element[1]&&element[1]>0&&typeof(element[2])=="number"
            &&element[2]>0){
                scares+=Math.floor(element[0].length/2);
                if(element[1]%2==0){
                    scares+=2;
                }
                totalHeight+=element[2];
            }else{
                return "error de formato, debes meter personas con el siguiente formato [nombre,edad,altura(cm)]";
            }
        });
        scares+=3*Math.floor(totalHeight/100);
        let trick = [];
        for(let j=1;j<=scares;j++){
            let i = Math.round(6*Math.random()-0.5);
            trick.push(options[i]);
        }
        return trick.join(" ");
    } else if(trick==false){
        let options = ["🍰","🍬","🍡","🍭","🍪","🍫","🧁","🍩"];
        let candies = 0;
        let treat = [];
        peopleData.forEach(element => { 
            if(element.length==3&&typeof(element[0])=="string"&&typeof(element[1])=="number"
            &&Math.floor(element[1])==element[1]&&element[1]>0&&typeof(element[2])=="number"
            &&element[2]>0){
                candies+=element[0].length;
                if(element[1]>10){
                    candies+=3;
                }else{
                    candies+=Math.floor(element[1]/3);
                }
                if(element[2]>=150){
                    candies+=6
                } else{
                    candies+=2*Math.floor(element[2]/50);
                }
            }else{
                return "error de formato, debes meter personas con el siguiente formato [nombre,edad,altura(cm)]";
            }
        });
    for(let j=1;j<=candies;j++){
        let i = Math.round(8*Math.random()-0.5);
        treat.push(options[i]);
    }
    return treat.join(" ");
    } else{
        return "error,trick solo puede ser verdadero o falso (equivalente a treat)"
    }
}