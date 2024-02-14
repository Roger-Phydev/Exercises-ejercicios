const isPrime = n=>{
    if (n<=1){
        return false;
    }
    let i=2;
    while(i<=parseInt(n/2)){
        if (n%i==0){
            break;
        }
        i++;
    }
    if (i==parseInt(n/2)+1){
        return true;
    }
    else{
        return false;
    }
}
for (let j = 1;j<=100;j++){
    if (isPrime(j)) console.log(j);
}