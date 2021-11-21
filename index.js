let answers = [];

function questionOneSubmit(answer) {
	location.href = 'page2.html?answers=' + encodeURI(answer);
}

function questionTwoLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
//	console.log(answers);
}

function questionTwoSubmit(answer) {
	answers.push(answer);
	location.href = 'page3.html?answers=' +encodeURI(answers);
}

function questionThreeLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
//	console.log(answers);
}

function questionThreeSubmit(answer) {
	answers.push(answer);
	location.href = 'page4.html?answers=' +encodeURI(answers);
}

function questionFourLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
//	console.log(answers);
}

function questionFourSubmit(answer) {
	answers.push(answer);
	location.href = 'page5.html?answers=' +encodeURI(answers);
}

function questionFiveLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
}

function questionFiveSubmit(answer){
	answers.push(answer);
	location.href = 'page6.html?answers=' +encodeURI(answers);
}

function questionSixLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
}

function questionSixSubmit(answer){
	answers.push(answer);
	location.href = 'page7.html?answers=' +encodeURI(answers);
}

function questionSevenLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
}

function questionSevenSubmit(answer){
	answers.push(answer);
	location.href = 'page8.html?answers=' +encodeURI(answers);
}

function questionEightLoad(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = searchParams.get('answers').split(',');
}

function questionEightSubmit(answer){
	console.log('hiiiiiiiiiii')
	answers.push(answer);
	//location.href = 'results.html?answers=' +encodeURI(answers);
	
	var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};
url = "https://0785-169-234-59-114.ngrok.io/submit?answers=" +answers.join(',')
fetch(url, requestOptions)
  .then(response => response.json())
  .then(result => location.href="results.html?result=" + JSON.stringify(result))
  .catch(error => console.log('error', error));
}

function readResult(){
	let searchParams = new URLSearchParams(window.location.search);
	answers = JSON.parse(searchParams.get('result'));
	
	document.getElementById("gamename").innerHTML=answers["gamename"]
	document.getElementById("gamerating").innerHTML=answers["gamerating"]
	document.getElementById("gameplot").innerHTML=answers["gameplot"]
	document.getElementById("gamepicture").src=answers["gamepicture"]
}
