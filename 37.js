zeldaDates={
    "Tloz":new Date(1986,1,21),
    "Zelda ii":new Date(1987,0,14),
    "A link to the past":new Date(1991,10,21),
    "Ocarina of time":new Date(1998,10,21),
    "Majora's mask":new Date(2000,3,27),
    "The wind waker":new Date(2002,11,13),
    "Four swords adventures":new Date(2004,2,18),
    "Twilight princess":new Date(2006,10,19),
    "Skyward sword":new Date(2011,10,18),
    "Breath of the wild":new Date(2017,2,3),
    "Tears of the kingdom":new Date(2023,4,12),
    "Link's awakening":new Date(1993,5,6),
    "Oracle of seasons":new Date(2001,1,27),
    "Oracle of ages":new Date(2001,1,27),
    "The minish cap":new Date(2004,10,4),
    "Phantom hourglass":new Date(2007,5,23),
    "Spirit tracks":new Date(2007,11,7),
    "A link between worlds":new Date(2013,10,22),
    "Triforce heroes":new Date(2015,9,22),
    "Four swords":new Date(2001,10,20)};
const timeBetweenZeldaTitles = (titleOne,titleTwo)=>{
    const zeldaDates={
        "Tloz":new Date(1986,1,21),
        "Zelda ii":new Date(1987,0,14),
        "A link to the past":new Date(1991,10,21),
        "Ocarina of time":new Date(1998,10,21),
        "Majora's mask":new Date(2000,3,27),
        "The wind waker":new Date(2002,11,13),
        "Four swords adventures":new Date(2004,2,18),
        "Twilight princess":new Date(2006,10,19),
        "Skyward sword":new Date(2011,10,18),
        "Breath of the wild":new Date(2017,2,3),
        "Tears of the kingdom":new Date(2023,4,12),
        "Link's awakening":new Date(1993,5,6),
        "Oracle of seasons":new Date(2001,1,27),
        "Oracle of ages":new Date(2001,1,27),
        "The minish cap":new Date(2004,10,4),
        "Phantom hourglass":new Date(2007,5,23),
        "Spirit tracks":new Date(2007,11,7),
        "A link between worlds":new Date(2013,10,22),
        "Triforce heroes":new Date(2015,9,22),
        "Four swords":new Date(2001,10,20)
    };
    if(zeldaDates[titleOne]!=undefined&&zeldaDates[titleTwo]!=undefined){
        let first = zeldaDates[titleOne];
        let second = zeldaDates[titleTwo];
        let years = 0;
        let days = 0;
        if(second-first>=0){
            let reference = new Date(second.getFullYear(),first.getMonth(),first.getDate());
            if(second-reference>=0){
                console.log("mayor");
                years = reference.getFullYear()-first.getFullYear();
                days = (second-reference)/(1000*60*60*24);
            } else{
                console.log("menor");
                reference = new Date(second.getFullYear()-1,first.getMonth(),first.getDate());
                years = reference.getFullYear()-first.getFullYear();
                days = (second-reference)/(1000*60*60*24);
            }
            console.log(reference,second,first);
            return `Hay ${years} años y ${days} días de diferencia entre los títulos`;
        }else{
            let reference = new Date(first.getFullYear,second.getMonth(),second.getDate());
            if(first-reference>=0){
                years = reference.getFullYear()-second.getFullYear();
                days = (first-reference)/(1000*60*60*24);
            } else{
                reference = new Date(first.getFullYear()-1,second.getMonth(),second.getDate());
                years = reference.getFullYear()-second.getFullYear();
                days = (first-reference)/(1000*60*60*24);
            }
            return `Hay ${years} años y ${days} días de diferencia entre los títulos`;
        }
    }else{
        return "alguno de los titulos que elegiste no es válido"
    }
}
zeldaDates["A link between worlds"]