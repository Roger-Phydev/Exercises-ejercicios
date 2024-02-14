const waterDepot = blocksArray=>{
    if(!Array.isArray(blocksArray)){
        return "error, debes introducir un array";
    }
    blocksArray.forEach(element => {
        if(typeof(element)!="number"||element!=Math.floor(element)||element<0){
            return "error de formato, tu array debe tener solo números naturales";
        }
    });
    let init = 0;//this will simbolize where each sub-water-depot intializes
    let end = 1; //this will represent when it will end
    let water = 0; //represents the quantity of water that we want to calculate
    while(init<blocksArray.length-1){//with init between the right values
        while(blocksArray[init]<=blocksArray[init+1]&&init<blocksArray.length-1){
            init++;//while the numbers go up, we move init and end by one unit
            end++;
        }
        while(blocksArray[end]>blocksArray[end+1]&&end<blocksArray.length-1){
            end++;//while now numbers go down, we move just end by one unit
        }
        while(blocksArray[end]<=blocksArray[end+1]&&end<blocksArray.length-1){
            end++;//while now numbers go up again, we move just end by one unit
        }//when ends everycycle, we've got a subdepot
        let subDepot = blocksArray.slice(init,end+1);//this subdepot is given by this
        let waterLevel = Math.min(blocksArray[init],blocksArray[end]);//calculates where the water ends
        subDepot.forEach(n=>{
            water+= Math.max(0,waterLevel-n); //for every element, we add to water this.
            //it just count when the number is less than the waterLevel. Otherwise, we add the diference
        })
        init = end;//we set the init here for the next iteration
        end++; //finally we increase the end by one for the next iteration.
    }
}