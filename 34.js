const lostNumbers = numbArray =>{
    let lost = [];
    let n=1;
    let status="";
    numbArray.forEach(element => {
        try{
            element=parseFloat(element);
        } catch{
            return "error de formato, debe se un array de números";
        }
    });
    for(let i=1;i<numbArray.length;i++){
        if(numbArray[i-1]>=numbArray[i]){
            n++;
        } else{
            break;
        }
    }
    if(n==numbArray.length){
        status="desc";
    }
    n=1;
    for(let i=1;i<numbArray.length;i++){
        if(numbArray[i-1]<=numbArray[i]){
            n++;
        } else{
            break;
        }
    }
    if(n==numbArray.length){
        status="asc";
    }
    console.log(status);
    if(status=="asc"||status=="desc"){
        let initial = Math.min(numbArray[0],numbArray.at(-1));
        let final = Math.max(numbArray[0],numbArray.at(-1));
        console.log(initial,final);
        for(let j=initial;j<=final;j++){
            if(!numbArray.includes(j)){
                lost.push(j);
            }
        } if(status=="desc"){
            lost.reverse()
        }
        return lost;
    } else{
        return "error, tu array debe estar ordenado ascendente o descendente";
    }
}