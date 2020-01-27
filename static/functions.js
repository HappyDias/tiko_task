var Chart = window.Chart

function draw_chart(arg){
	var node = document.getElementById(arg);
	if(!(Chart === undefined)){

		var chart = new Chart(node, {
			type: 'line',
			data: {
				datasets: [{
					label: 'Length of joke',
					data: []
				}]
			},
			options: {
				scales: {
					xAxes: [{
						type: 'time',
						time: {
							unit: 'second'
						}
					}]
				}
			}
		});
		return chart
	}
	throw {message: "Chart library does not exist"}
}

function update_chart(chart, data){
	chart.data.datasets[0].data.push(data)
	chart.update();
}

function request_data(chart){
	fetch('http://api.icndb.com/jokes/random')
		.then( response => {
			if(!response.ok){ throw response }
			return response.json()
		})
		.then( json => {
			const joke_length = json.value.joke.length
			const nowDate = new Date()
			update_chart(chart, {x:nowDate, y: joke_length})
		})
}

export default {draw_chart, request_data}