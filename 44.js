const boomerangsIn = integersArray =>{
    let boomerangs = [];
    integersArray.forEach(element => {
        if(typeof(element)!="number"||Math.floor(element)!=element){
            return "error, debe ser una lista de números enteros";
        }
    });
    for(let i=0;i<integersArray.length-2;i++){
        if(integersArray[i]==integersArray[i+2]&&integersArray[i+1]!=integersArray[i]){
            boomerangs.push([integersArray[i],integersArray[i+1],integersArray[i+2]]);
        }
    }
    return boomerangs;
}