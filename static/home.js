


window.addEventListener("load", () => {

  })
  var data = [
    {
        domain: { x: [0, 1], y: [0, 1.5] },
        value: 4000,
        title: { text: "Number of Solar Pumps",font: { size: 18,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
        gauge: {
          axis: { range: [0, 5000] }
      }
    },
    {
        domain: { x: [0.12, 0.88], y: [0.04, 0.80] },
        value: 1500,
        //title: { text: "Degree" },
        type: "indicator",
        mode: "gauge+title",
        gauge: {
          axis: { range: [0, 5000], tickvals: [] },//bgcolor: "lightgray",  // Set the background color of the gauge
        bar: { color: "blue" } // Set the color of the gauge bar
      }
    },
    {
        domain: { x: [0.21, 0.8], y: [0.1, 0.62] },
        value: 2500,
        //title: { text: "km/h" },
        type: "indicator",
        mode: "gauge+title",
        gauge: {
          axis: { range: [0, 5000], tickvals: [] },
           bar: { color: "black" }
      }
    }
  ];
  var layout = {
    width: 500,
    height: 250,
    margin: { t: 0, b: 0 },
    grid: { rows: 1, columns: 1, pattern: 'independent' },
   annotations: [
      {
        x: -0.05, // Adjust x position to move the data horizontally
        y: 0, // Adjust y position to move the data vertically
        text: "Total",
        showarrow: false,
        font: { size: 14, color: "green", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true }
      },
      {
        x: 0.08, // Adjust x position to move the data horizontally
        y: 0, // Adjust y position to move the data vertically
        text: "Runing",
        showarrow: false,
        font: { size: 14, color: "blue", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true  }
      },
     {
        x: 0.25, // Adjust x position to move the data horizontally
        y: 0, // Adjust y position to move the data vertically
        text: "Not Runing",
        showarrow: false,
        font: { size: 14, color: "black", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true  }
      },
     {
        x: 0.5, // Adjust x position to move the data horizontally
        y: 0.25, // Adjust y position to move the data vertically
        text: "",
        showarrow: false,
        font: { size: 18, color: "black", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true }
      }
    ]
  };
  Plotly.newPlot('myDiv', data, layout);
   
  var button = document.getElementById('myButton');
  document.getElementById('counter1').textContent = 4000;
  document.getElementById('counter2').textContent = 1500;
  document.getElementById('counter3').textContent = 2500;