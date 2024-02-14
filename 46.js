const vecSum = (vec1,c1,vec2,c2)=>{
    let sum = [];
    for(let i in vec1){
        sum[i]=c1*vec1[i]+c2*vec2[i];
    }
    return sum;
}
const dotProduct = (vec1,vec2)=>{
    let pdt=0;
    for(let i in vec1){
        pdt+=vec1[i]*vec2[i];
    }
    return pdt;
}
const matrixApplication = (matrix,vec)=>{
    let ans=[];
    matrix.forEach(element => {
        ans.push(dotProduct(element,vec));
    });
    return ans;
}
const whereIsTheRobot = intergersArray =>{
    let position=[0,0];
    let direction = [0,1];
    let transf = [[0,-1],[1,0]];
    intergersArray.forEach(element=>{
        if(typeof(element)!="number"||element!=Math.floor(element)){
            return "error, solo debe contener enteros";
        } else{
            position = vecSum(position,1,direction,parseFloat(element));
            direction = matrixApplication(transf,direction);
        }
    })
    return position;
}