var trace2 = {
    x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y: [4000, 1000, 500, 3500, 888, 2000, 999, 5000, 2000, 647, 674, 2750],
    type: 'bar',
    name: 'Primary Product',
    text:[4000, 1000, 500, 3500, 888, 2000, 999, 5000, 2000, 647, 674, 2750], // This array holds the values for text display
    textposition: 'auto',
    marker: {
      color: 'rgb(49,130,189)',
      opacity: 0.7,
    }
  };
  
  var data2 = [trace2];
  
  var layout = {
    title: { text:'Water Out (Lit)',font: { size: 18,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "black" } },
    xaxis: {
      tickangle: -45
    },
    barmode: 'group',
    height: 350
  };
  
  Plotly.newPlot('myDiv2', data2, layout);
  
  var trace1 = {
    x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y: [4, 10, 5, 6, 8, 2, 9, 5, 2, 6, 4, 7],
    type: 'bar',
    name: 'Primary Product',
    text: [4, 10, 5, 6, 8, 2, 9, 5, 2, 6, 4, 7], // This array holds the values for text display
    textposition: 'auto',
    marker: {
        color: [
            'rgb(44, 77, 143)',
            'rgb(38, 112, 133)',
            'rgb(30, 147, 122)',
            'rgb(51, 165, 89)',
            'rgb(114, 175, 55)',
            'rgb(174, 184, 32)',
            'rgb(222, 182, 29)',
            'rgb(235, 147, 26)',
            'rgb(226, 91, 34)',
            'rgb(205, 51, 45)',
            'rgb(169, 21, 72)',
            'rgb(128, 25, 88)'
          ],
      opacity: 0.7,
    }
  };
      
    var data = [trace1];
    
    var layout = {
      title: { text:'Working Hours (hr)',font: { size: 18,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "black" } },
      xaxis: {
        tickangle: -45
      },
      barmode: 'group',
      height: 350
      
    };
    
    Plotly.newPlot('myDiv1', data, layout);

    