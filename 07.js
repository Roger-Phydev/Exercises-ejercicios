let a = "jasiodas.,dhisuiufdsuif";
const wordCounter = str =>{
    str = str.toLowerCase();
    let symbols = [".",",",";",":"]
    for (symbol of symbols){
        str = str.replace(symbol,"");
    }
    str = str.split(/\s+/);
    let words = [];
    let repeats = [];
    for (word of str){
        if (words.indexOf(word)==-1){
            words.push(word);
            repeats.push(1);
        } else{
            let n = words.indexOf(word);
            repeats[n]+=1;
        }
    }
    let result = [];
    for (i in words){
        result.push(`${words[i]}: ${repeats[i]}`);
    }
    return result;
}
let s = [["asdasda",2],["ab",5],["cop",54]];
console.log(s.indexOf(["ab",5]));