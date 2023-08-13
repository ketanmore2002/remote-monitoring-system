window.addEventListener("load", () => {

  })
  var data = [
    {
        domain: { x: [0, 1], y: [0, 1] },
        value: 12,
        title: { text: "",font: { size: 14,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
       // gauge: {
        //  axis: { range: [0, 25]  }
      //}
    }
    ];
  var layout = {
    width: 350,
    height: 150,
    margin: { t: 0, b: 0 },
    grid: { rows: 1, columns: 1, pattern: 'independent' },
   annotations: [
      {
        x: 0.5, // Adjust x position to move the data horizontally
        y: 0.3, // Adjust y position to move the data vertically
        text: "Voltage (V)",
        showarrow: false,
        font: { size: 22, color: "green", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true }
      }
    ]
  };
  Plotly.newPlot('myDiv1', data, layout);
  var data = [
    {
        domain: { x: [0, 1], y: [0, 1.5] },
        value: 12,
        title: { text: "",font: { size: 14,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
       // gauge: {
         // axis: { range: [0, 25]  }
      //}
    }
    ];
  var layout = {
    width: 350,
    height: 150,
    margin: { t: 0, b: 0 },
    grid: { rows: 1, columns: 1, pattern: 'independent' },
   annotations: [
      {
        x: 0.5, // Adjust x position to move the data horizontally
        y: 0.3, // Adjust y position to move the data vertically
        text: "Current (A)",
        showarrow: false,
        font: { size: 14, color: "green", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true }
      }
    ]
  };
  Plotly.newPlot('myDiv2', data, layout);
  var data = [
    {
        domain: { x: [0, 1], y: [0, 1.5] },
        value: 12,
        title: { text: "",font: { size: 14,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
      //  gauge: {
       //   axis: { range: [0, 25]  }
      //}
    }
    ];
  var layout = {
    width: 350,
    height: 150,
    margin: { t: 0, b: 0 },
    grid: { rows: 1, columns: 1, pattern: 'independent' },
   annotations: [
      {
        x: 0.5, // Adjust x position to move the data horizontally
        y: 0.3, // Adjust y position to move the data vertically
        text: "Power (W)",
        showarrow: false,
        font: { size: 14, color: "green", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true }
      }
    ]
  };
  Plotly.newPlot('myDiv3', data, layout);