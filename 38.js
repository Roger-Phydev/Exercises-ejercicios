"use strict"
const binaryToDec = binNumber =>{
    let n=0;
    try{
        binNumber = binNumber.toString();
    }catch{
        return "formato inapropiado";
    }
    for(let k of binNumber){
        if(k==0||k==1){
            n++;
        }
    }
    let l = binNumber.length;
    if(n==l){
        let digits = binNumber.split("");
        let dec = 0;
        for(let i in digits){
            dec+=parseFloat(digits[i])*(2**(l-i-1));
        }
        return dec;
    }else{
        return "error, tu expresión no corresponde a un número binario"
    }
}