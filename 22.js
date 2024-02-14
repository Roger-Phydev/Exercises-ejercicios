"use strict"
const IntersectionAndDifOf = (arrayOne,arrayTwo,bool=true)=>{
    let result=[];
    if(bool){
        arrayOne.forEach(item => {
            if(arrayTwo.includes(item)&&!(result.includes(item))){
                result.push(item)
            }
        });
        return result
    } else{
        arrayOne.forEach(element => {
            if(!(arrayTwo.includes(element)||result.includes(element))){
                result.push(element)
            }
        });
        arrayTwo.forEach(element => {
            if(!(arrayOne.includes(element)||result.includes(element))){
                result.push(element)
            }
        });
        return result;
    }
}