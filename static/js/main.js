$(document).ready(function statecheck(myLayer) {
	var myLayer1 = document.getElementById(myLayer);
	var str1 = myLayer;
	var str2 = "{{ data[ques_number-1][5] }}";
	console.log(str1);
	console.log(str2);
	var myLayer2 = document.getElementById(str2);
	var n = str1.localeCompare(str2);
	console.log(n);
	if(n == 0)
	{
		myLayer1.style.backgroundColor = "#bff0a1";
		document.getElementById("yoda-example").checked = true;
		document.getElementById("a").disabled = true;
		document.getElementById("b").disabled = true;
		document.getElementById("c").disabled = true;
		document.getElementById("d").disabled = true;
		setTimeout(function Redirect() {
			window.location='/ques/'+ ({{ques_number}} + 1);
		},2500);
	}
	else
	{
		myLayer1.style.backgroundColor = "#b000a1";
		myLayer2.style.backgroundColor = "#bff0a1";
		document.getElementById("darth-vader-example").checked = true;			
		document.getElementById("a").disabled = true;
		document.getElementById("b").disabled = true;
		document.getElementById("c").disabled = true;
		document.getElementById("d").disabled = true;
		setTimeout(function Redirect1() {
			window.location='/ques/'+ ({{ques_number}} + 1);
		},2500);
	}
	window.history.forward();			
}


var count = 200;
var fxn = function() {
	count--;
	document.getElementById('time').innerHTML = count;
	if(count == 0){
		Redirect1();
	}
}
setInterval(fxn, 800000);

if({{ques_number}} < 6)
{
	function Redirect() {
		window.location='/ques/'+ ({{ques_number}} + 1);
	}
	function Redirect1() {
		window.location='/ques/'+ ({{ques_number}} + 1);
	}
}

if({{ques_number}} >= 6)
{
	Redirect2();
}

function Redirect2(){
	window.location = '/end';
});