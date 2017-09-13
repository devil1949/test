/*

//alert('测试');

//name = '123'

//var name = '456'

Foo('456','789');

function Foo(name){
    var para = arguments[1];
    console.log(name);
    console.log(para);
}

(function(name){
    Console.log(name);
})('123')

var arry1 = [1,2,3,4];
//var arry2 = Array(1,2,3,4,5)
arry1.push('qwe');
arry1.unshift('asd');
arry1.splice(1,0,'zxc');
console.log(arry1);

*/

var arry1 = [1,2,3,4];

for(var i in arry1){
    console.log(arry1[i]);
}
