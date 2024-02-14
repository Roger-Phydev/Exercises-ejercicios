const recursivefact = n=>{
    if(typeof(n)=="number"&&n>=0&&Math.floor(n)==n){
        if(n==1||n==0) return 1;
        return n*recursivefact(n-1);
    }
}