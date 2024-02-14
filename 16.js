const capitalConverter = str =>{
    if(typeof(str)=="string"){
        let words = str.replace(/\./g,"");
        words = words.replace(/\,/g,"").replace(/\;/g,"").replace(/\:/g,"");
        words = words.split(" ").filter(item=>{
            if(item=="") return false;
            return true;
        });
        for (word of words){
            let ref = word.toString();
            if(word.length>1){
                str = str.replace(word,ref.substring(0,1).toUpperCase()+ref.substring(1))
            } else{
                str = str.replace(word,ref.toUpperCase());
            }
        }
        return str;
    }else{
        return "error de formato"
    }
}