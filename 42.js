const temperatureConversor = tempStr =>{
    if(tempStr == tempStr.match(/[0-9]+\s°[F|C]/)){
        let tail = tempStr.split(" ")[1].replace("°","");
        let value = parseFloat(tempStr.split(" ")[0]);
        if(tail=="F"){
            let temp = (value-32)*5/9;
            return temp+" °C";
        } else{
            let temp = (9/5)*value+32;
            return temp+" °F";
        }
    } else{
        return false;
    }
}