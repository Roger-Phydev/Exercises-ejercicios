const effectivityMap={
    "agua":[0.5,2,0.5,1],
    "fuego":[0.5,0.5,2,1],
    "planta":[2,0.5,0.5,1],
    "eléctrico":[2,1,0.5,0.5]
};
const effectivity = (attackType,targetType,power,defense)=>{
    let types = ["agua","fuego","planta","eléctrico"];
    let table = effectivityMap[attackType];
    let i = types.indexOf(targetType);
    if(table!=undefined||i!=-1){
        if(Math.abs(parseFloat(power)-50)<=50&&Math.abs(parseFloat(defense)-50)<=50){
            return (power/defense)*50*table[i];
        }else{
            return "error, el ataque y defensa no deben pasar de 100 ni ser inferiores a cero";
        }
    } else{
        return "error,algún tipo es erroneo, posibilidades: agua, fuego, planta, eléctrico";
    }
}