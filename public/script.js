
function handleSubmit(e) {
	e.preventDefault();
	const ves = this.querySelector("textarea").value;
	const width = document.querySelector("div:nth-child(2)").clientWidth; 
	const formular = new URLSearchParams(); 
	formular.append('ves', ves);
	formular.append('width', width);

	const url = this.action; 
	const method = this.method; 
	fetch(url, {method: method, body: formular})
		.then((res) => res.blob())
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image);
		})
}
document.querySelector("form").addEventListener("submit", handleSubmit); 


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
