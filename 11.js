const charDiffIn = (str1,str2)=>{
    let l1=str1.split(""),l2=str2.split("");
    let dif1="",dif2="";
    for(a of l1){
        if (!str2.includes(a)) dif1+=a;
    }
    for(b of l2){
        if (!str1.includes(b)) dif2+=b;
    }
    return [dif1,dif2];
}
let chjas = "ashijudhiuas";