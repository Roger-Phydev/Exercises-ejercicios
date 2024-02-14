const closed = (a,b)=>{
    if((a=="{"&&b=="}")||(a=="("&&b==")")||(a=="["&&b=="]")){
        return true;
    }
    return false;
} // a function that determines if two chars match or not
const isEquilibrated = expression =>{
    let symbols = [" "]; // this will contain all {} () and [], it includes " " in order to solve the case that the first symbol is ],}or) and if the last is (.[ or{
    let op = ["(","[","{"];
    let cls = [")","]","}"];
    for(l of expression){
        if(op.includes(l)) symbols.push(l);
        else if (cls.includes(l)&&!(closed(symbols.pop(),l))) return false
    }
    console.log(symbols);
    if(symbols.length==1) return true;
    return false;
}