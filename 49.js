const HandlesIn = str=>{
    let find = [...str.matchAll(/\B[@]\w+/g)];
    let users=[],hashtags=[],webs=[];
    for(element of find){
        users.push(element[0]);
    }
    find  = [...str.matchAll(/\B[#]\w+/g)];
    for(element of find){
        hashtags.push(element[0]);
    }
    find  = [...str.matchAll(/(www\.|http:\/\/|https:\/\/)[^\s]+(.com)/g)];
    for(element of find){
        webs.push(element[0]);
    }
    return {
        "usuarios":users,
        "hashtags":hashtags,
        "páginas web":webs
    };
}