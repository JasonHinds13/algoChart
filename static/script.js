var results;
var colors = ['#ff0000','#800080','#ff6347','#ffff00','#00ff00','#0000ff'];

$(document).ready(function(){
	$.get( "/api/algoData", function(data) {
		results = data;
		$(".loader").remove();

		var chartIndex = 0;

		for(k in results){
			var labs = [];
			var vals = [];

			for(var i=0; i < results[k].length; i++){
				labs.push(results[k][i][0]);
				vals.push(results[k][i][1]);
			}

			$(".wrapper").append('<canvas id="myChart'+ chartIndex +'" height="300px" width="300px"></canvas>');
			$(".compare").append('<input type="checkbox" class="select" value="'+ k +'"/><p class="selectText">'+k+'</p>');
			var ctx = document.getElementById('myChart'+chartIndex);
			var myLineChart = new Chart(ctx, {
			    type: 'line',
			    data: {
			    	labels: labs,
			    	datasets: [{
			    		label: k,
			    		backgroundColor: colors[chartIndex % colors.length],
			    		borderColor: colors[chartIndex % colors.length],
			    		data: vals,
			    		fill: false,
						borderWidth: 1
			    	}]
			    },
			    options: {
				    responsive: false,
				    maintainAspectRatio: false,
				    title: {
						display: true,
						text: 'Performace of ' + k
					},
				    scales: {
				    	xAxes: [{
							display: true,
							scaleLabel: {
								display: true,
								labelString: '# of elements (n)'
							}
						}],
				        yAxes: [{
				        	scaleLabel:{
				        		display: true,
				        		labelString: 'Time'
				        	},
				            ticks: {
				                beginAtZero:false
				            }
				        }]
				    },
						color: [
					    'red',
					    'blue',
					    'green',
						'yellow',
					    'black',
					]
				}
			});
			chartIndex = chartIndex + 1;
		}
	});

	$("#compButton").click(function(){
		var selected = [];
		var newlabel = [];

		$(".select:checked").each(function(ind, val){
			var vals = [];
			var labs = [];

			for(var i=0; i < results[val.value].length; i++){
				labs.push(results[val.value][i][0]);
				vals.push(results[val.value][i][1]);
			}

			newlabel = labs;

			obj = {
				label: val.value,
		    	backgroundColor: colors[ind % colors.length],
		    	borderColor: colors[ind % colors.length],
		    	data: vals,
		    	fill: false,
				borderWidth: 1
		    }

		    selected.push(obj);
		});

		var ctx = document.getElementById('compChart');
		var myLineChart = new Chart(ctx, {
		    type: 'line',
		    data: {
		    	labels: newlabel,
		    	datasets: selected
		    },
		    options: {
			    responsive: false,
			    maintainAspectRatio: false,
			    title: {
					display: true,
					text: 'Comparison of Performace'
				},
			    scales: {
			    	xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: '# of elements (n)'
						}
					}],
			        yAxes: [{
			        	scaleLabel:{
			        		display: true,
			        		labelString: 'Time'
			        	},
			            ticks: {
			                beginAtZero:false
			            }
			        }]
			    }
			}
		});
	});
});