var array = [1,5,1,6,4,5,2,5,4,3,1,2,6,6,3,3,2,4];


// var unique = array.filter(function(item, index){
//     //return true일때 item을 리턴
//     // 0 == 0 true
//     // 1 == 1 true
//     // 2 == 0 false
//     // 3 == 3 true
//     // return index == array.indexOf(item);
//     return true
// });

const unique = array.filter( (value,index) => {
    return index == array.indexOf(value)
});


console.log(unique);