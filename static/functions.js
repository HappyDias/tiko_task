function draw_chart(arg){
	var node = document.getElementById(arg);
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

function update_chart(chart, data){
	chart.data.datasets[0].data.push(data)
	chart.update();
}

function request_data(chart){
	var req = fetch('http://api.icndb.com/jokes/random')
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

