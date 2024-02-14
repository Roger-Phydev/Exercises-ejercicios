const isArmstrong = n=>{
   if(typeof(n)=="number"&&n>=0&&n==Math.floor(n)){
        let list=n.toString().split("");
        let s=0,l=list.length;
        console.log(list,s,l);
        for(i of list){
            s+=Math.pow(parseInt(i),l);
        }
        if(s==n) return true;
        return false;
   } 
}