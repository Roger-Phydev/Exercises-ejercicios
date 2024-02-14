const MCD = (n,m)=>{
    let M=Math.max(n,m),N=Math.min(n,m);
    if(N==0){
        return M;
    } else{
        let d=M%N;
        return MCD(N,d);
    }
}
const mcm = (n,m)=>{
    return (n*m)/MCD(n,m);
}