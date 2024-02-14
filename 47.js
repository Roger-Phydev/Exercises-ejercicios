const mostCommonVowel = str=>{
    let mostCommon = [];
    let a = ["a",str.split("").filter(l=>{
        if(l=="a"){ return true; }
        else {return false; }
    }).length];
    let e = ["e",str.split("").filter(l=>{
        if(l=="e"){ return true; }
        else {return false; }
    }).length];
    let i = ["i",str.split("").filter(l=>{
        if(l=="i"){ return true; }
        else {return false; }
    }).length];
    let o = ["o",str.split("").filter(l=>{
        if(l=="o"){ return true; }
        else {return false; }
    }).length];
    let u = ["u",str.split("").filter(l=>{
        if(l=="u"){ return true; }
        else {return false; }
    }).length];
    let m = Math.max(a[1],e[1],i[1],o[1],u[1]);
    [a,e,i,o,u].forEach(list=>{
        if(list[1]==m){
            mostCommon.push(list[0]);
        }
    })
    return mostCommon.join(" ");
}