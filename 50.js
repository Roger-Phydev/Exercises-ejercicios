const karakaCrypt = str =>{
    let code = str.split("");
    code.reverse();
    code = code.join("");
    let tail = "aca";
    let vowels = "aeiou".split("");
    if(code.startsWith(tail)&&code.length>3&&code.substring(3).match(/[^aeiou56789]+/)!=null){
        code = code.substring(3);
        for(i in vowels){
            code = code.replace(RegExp(i,"g"),vowels[i]);
        }
        return code;
    }else{
        for(i in vowels){
            if(code.includes(vowels[i])){
                code = code.replace(RegExp(vowels[i],"g"),i);
            }
        }
        code+=tail;
        return code;
    }
}