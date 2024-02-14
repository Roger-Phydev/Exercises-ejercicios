const theSecondMost = numbArray =>{
    if (numbArray.length==1){
        return numbArray[0];
    }
    let m=parseFloat(numbArray[0]);
    numbArray.forEach(element => {
        element=parseFloat(element);
        m=Math.max(m,element);
    });
    const patron = new RegExp(m+" ","g");
    let newArr = numbArray.join(" ").replace(RegExp(m,"g"),"").replace(/\s+/g," ").trim().split(" ");
    m=parseFloat(newArr[0]);
    newArr.forEach(element=>{
        m=Math.max(parseFloat(element),m);
    })
    return m;
}