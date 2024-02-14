const decToBinary = number=>{
    try{
        number = parseInt(number);
    } catch{
        return "debes meter un número"
    }
    if (number==0) return 0
    else if (number>0){
        let bin = ""
        while (number>0){
            let r = number%(2);
            number = (number - r)/2;
            bin = r + bin;
        }
        return bin;
    } else{
        return "error, debe ser un número positivo";
    }
}