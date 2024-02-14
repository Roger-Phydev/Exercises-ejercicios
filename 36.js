let gooddies = {
    "pelosos":1,
    "sureños buenos":2,
    "enanos":3,
    "numenoreanos":4,
    "elfos":5
}
let baddies = {
    "sureños malos":2,
    "orcos":2,
    "duendes":2,
    "huargos":3,
    "trolls":5
};
const battleBetween = (goodArmy,evilArmy)=>{
    let status = 0;
    try{
        goodArmy=goodArmy.toLowerCase();
        evilArmy=evilArmy.toLowerCase();
    } catch{
        return "error, debes meter una lista con el ejercito";
    }
    let listOfGoods = goodArmy.matchAll(/[0-9]+\s(pelosos|sureños buenos|enanos|numeroreanos|elfos)/g);
    let listOfEvil = evilArmy.matchAll(/[0-9]+\s(sureños malos|orcos|duendes|huargos|trolls)/g);
    for(l of listOfGoods){
        let iteration = l[0].split(" ");
        status+=parseFloat(gooddies[iteration[1]])*iteration[0];
    };
    for(l of listOfEvil){
        let iteration = l[0].split(" ");
        status-=parseFloat(baddies[iteration[1]])*iteration[0];
    };
    if(status>0){
        return "Good wins";
    } else if(status==0){
        return "Tie";
    } else{
        return "Evil wins"
    }
}
let a = "23 pelosos";
let b = "4 orcos";