const chineseZodiacalInfo = year=>{
    const elements = ["madera/wood","fuego/fire","tierra/ground","metal","agua/water"];
    const animals = ["rata/rat","buey/ox","tigre/tiger","conejo/rabbit","dragón/dragon",
"serpiente/snake","caballo/horse","oveja/sheep","mono/monkey","gallo/rooster","perro/dog",
"cerdo/pig"];
    let diff = year-1984;
    let animalIndex = diff%16;
    let elementSymbol = (Math.floor(diff/2))%5;
    return animals[animalIndex]+" | "+elements[elementSymbol];
};