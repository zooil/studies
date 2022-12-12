function square(x) { return x*x }
console.log(square(3));

function multi(a, b){
	b= b||1;
	return a*b;
}
console.log(multi(2));

function kk(){
	for( var i=0;i<arguments.length;i++)
	console.log(arguments[i]);
}
kk(1,2,3,4,1);

function addSen(){

	var res = "";
	for(var i=0;i<arguments.length;i++)
		res += arguments[i] + " ";
	return res;
}
console.log(addSen("rabbit", "apple", "orange"));

