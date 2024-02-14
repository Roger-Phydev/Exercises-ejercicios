const solveOhmLaw = (v=undefined,r=undefined,i=undefined)=>{
    if(typeof(v)=="number"&&typeof(r)=="number"&&i==undefined){
        return v/r;
    } else if(typeof(v)=="number"&&typeof(i)=="number"&&r==undefined){
        return v/i;
    } else if(typeof(i)=="number"&&typeof(r)=="number"&&v==undefined){
        return r*i;
    } else{
        return "error, solo debes meter dos argumentos que conozcas y deben ser números, el tercer argumento desconocido debes colocar un 'undefined'";
    }
}