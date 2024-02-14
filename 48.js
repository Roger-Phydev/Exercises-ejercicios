const adevCalendar = dateTypeObject =>{
    const begin = new Date(2022,11,1,0,0,0);
    const end = new Date(2022,11,23,23,59,59);
    const calendar = [
        "Iphone",
        "PC",
        "Adobe",
        "dragones",
        "juego de mesa",
        "codigo windows",
        "Iphone",
        "PC",
        "Adobe",
        "dragones",
        "juego de mesa",
        "codigo windows",
        "Iphone",
        "PC",
        "Adobe",
        "dragones",
        "juego de mesa",
        "codigo windows",
        "Iphone",
        "PC",
        "Adobe",
        "dragones",
        "juego de mesa",
        "Teclado"
    ];
    try{
        dateTypeObject.getDate();
    }catch{
        return "error, tu dato debe ser una fecha de tipo Date";
    }
    let left = begin-dateTypeObject;
    let right = dateTypeObject-end;
    if(left>0){
        let days = Math.floor(left/(24*60*60*1000));
        let hours = 23-dateTypeObject.getHours();
        let minutes = 59-dateTypeObject.getMinutes();
        let seconds = 59-dateTypeObject.getSeconds();
        return "restan: "+days+" días "+hours+" horas "+minutes+" minutos y "+seconds+" segundos";
    } else if(right>0){
        let days = Math.floor(right/(24*60*60*1000));
        let hours = dateTypeObject.getHours();
        let minutes = dateTypeObject.getMinutes();
        let seconds = 1+dateTypeObject.getSeconds();
        return "acabó hace: "+days+" días "+hours+" horas "+minutes+" minutos y "+seconds+" segundos";
    } else{
        let i=0;r=0;
        if(dateTypeObject.getHours()<23||dateTypeObject.getMinutes()<59||dateTypeObject.getSeconds()<=59){
            i = dateTypeObject.getDate()-1;
        }else{
            i = dateTypeObject.getDate();
        }
        let hours = 23-dateTypeObject.getHours();
        let minutes = 59-dateTypeObject.getMinutes();
        let seconds = 60-dateTypeObject.getSeconds();
        return `el premio del día es ${calendar[i]}, y restan ${hours} horas, ${minutes} minutos y ${seconds} segundos para reclamarlo`;
    }
}