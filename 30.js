const asteriscFrame = str=>{
    let arr = str.split(" ");
    let l=0;
    arr.forEach(element => {
        l=Math.max(l,element.length)
    });
    console.log("".padEnd(l+2,"*"));
    arr.forEach(element=>{
        console.log("*"+element.padEnd(l," ")+"*");
    });
    console.log("".padEnd(l+2,"*"));
}