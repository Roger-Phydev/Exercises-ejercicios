const sum = (a,b)=>{
    alert(a+b);
}
const delayedSum = (a,b,seconds)=>{
    let time = seconds*1000;
    return setTimeout(()=>{sum(a,b)},time);
}
//setTimeout(()=>{sum(3,4)},3000);