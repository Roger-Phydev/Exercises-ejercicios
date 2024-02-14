const reverseString = str=>{
    if (typeof(str)=="string"){
        let letters = str.split("");
        let inverted = "";
        for (letter of letters){
            inverted=letter.concat(inverted);
        }
        return inverted;
    } else{
        console.log("Error, debes introducir un string");
    }
}