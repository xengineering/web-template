
function example_post() {
	
	var data = {
		"key":"value",
	}
	var json = JSON.stringify(data);
	
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "api", true);
	xhr.send(json);

}

