const isPalindrom = phrase =>{
    phrase = phrase.replace(/\s/g,"");
    phrase = phrase.replace(/\./g,"");
    phrase = phrase.replace(/\,/g,"");
    phrase = phrase.replace(/\;/g,"");
    phrase = phrase.replace(/\:/g,"");
    reversedPhrase = phrase.split("").reverse().join("");
    if (phrase==reversedPhrase) return true;
    return false;
}