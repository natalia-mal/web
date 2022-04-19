function handleSubmit(e) {
	e.preventDefault();
	const form = document.getElementById("form")
	const ves = form.querySelector("textarea").value;
	const width = document.querySelector("div:nth-child(2)").clientWidth; 
	const formular = new URLSearchParams(); 
	formular.append('ves', ves);
	formular.append('width', width);

	const url = form.action; 
	const method = form.method; 
	fetch(url, {method: method, body: formular})
		.then((res) => res.blob())
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image);
			document.getElementById("output").style.visibility = "visible";
		})
}

function clear(e) {
    e.preventDefault();
    document.querySelector("textarea").value = "VES v1.6 600 400";
    document.getElementById("output").style.visibility = "hidden"; 
}

function obr1(e) {
    e.preventDefault();
    document.querySelector("textarea").value = "VES v1.0 600 400 \nCLEAR #FF0000 \nFILL_TRIANGLE 200 100 400 300 300 300 #0000FF\nFILL_CIRCLE 200 100 50 #00FF00\nFILL_RECT 400 100 150 200 #00FF00\nCIRCLE 300 200 100 1 #FFFFFF\nTRIANGLE 50 100 200 300 150 200 1 #00FF00\nRECT 200 100 300 100 1 #000000\nLINE 0 0 599 499 1 #000000"; 
	handleSubmit(e)
}
function obr2(e) {
    e.preventDefault();
    document.querySelector("textarea").value = "VES v1.0 600 400\nCLEAR #FFFFFF\nFILL_CIRCLE 240 170 140 #0CC142\nFILL_CIRCLE 240 265 25 #000000\nFILL_TRIANGLE 140 100 160 160 220 120 #8C3908\nFILL_TRIANGLE 220 120 240 200 260 120 #8C3908\nFILL_TRIANGLE 260 120 310 160 340 100 #8C3908\nFILL_TRIANGLE 220 120 160 160 240 200 #AB4D15\nFILL_TRIANGLE 260 120 240 200 310 160 #AB4D15\nFILL_TRIANGLE 160 160 150 200 240 200 #C14E0C\nFILL_TRIANGLE 310 160 240 200 320 200 #C14E0C\nFILL_TRIANGLE 160 160 150 200 240 200 #C14E0C\nFILL_TRIANGLE 150 200 220 280 220 200 #CB5F20\nFILL_TRIANGLE 260 200 260 280 320 200 #CB5F20\nFILL_TRIANGLE 140 100 160 165 170 150 #F5A0A0\nFILL_TRIANGLE 300 150 310 160 340 100 #F5A0A0\nFILL_TRIANGLE 220 200 220 280 260 200 #AB4D15\nFILL_TRIANGLE 260 200 220 280 260 280 #AB4D15\nFILL_TRIANGLE 190 200 220 210 220 200 #000000\nFILL_TRIANGLE 260 200 260 210 290 200 #000000\nLINE 120 210 216 225 1 #000000\nLINE 130 240 205 230 1 #000000\nLINE 120 270 220 240 1 #000000\nLINE 267 230 370 210 1 #000000\nLINE 275 233 350 245 1 #000000\nLINE 265 240 376 270 1 #000000"; 
	handleSubmit(e)
}

var r = document.querySelector(':root');
function changeThemeDark() {
	r.style.setProperty('--color-green', '#44A644');
	r.style.setProperty('--color-dark', 'black');
	r.style.setProperty('--color-secondary', '#022601');
	r.style.setProperty('--color-box-shadow', '#042B02');
}

function changeThemeLight() {
	r.style.setProperty('--color-green', '#9FCF9F');
	r.style.setProperty('--color-dark', '#191F29');
	r.style.setProperty('--color-secondary', '#334F45');
	r.style.setProperty('--color-box-shadow', '#2B402F');
}
document.querySelector("form").addEventListener("submit", handleSubmit);
document.querySelector("#clear").addEventListener("click", clear)
document.querySelector("#example1").addEventListener("click", obr1)
document.querySelector("#example2").addEventListener("click", obr2)