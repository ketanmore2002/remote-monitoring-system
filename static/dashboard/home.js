window.addEventListener("load", () => {

  })
  var data = [
    {
        domain: { x: [0, 1], y: [0, 1] },
        value: 100,
        title: { text: "",font: { size: 14,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
        gauge: {
          axis: {
              range: [0, 120],
              tickvals: [0, 20, 40, 60, 80, 100, 120],
              tickfont: {  // Adding font settings for the tick labels
                  size: 10,  // Specify the desired font size for the tick labels
                  family: "Arial, sans-serif",  // Specify the font family for the tick labels
                  color: "black"  // Specify the font color for the tick labels
              }
          }
      }
  }
  ];
  var layout = {
    width: 350,
    height: 120,
    margin: { t: 0, b: 0 },
    grid: { rows: 1, columns: 1, pattern: 'independent' },
   annotations: [
      {
        x: 0.5, // Adjust x position to move the data horizontally
        y: 0.3, // Adjust y position to move the data vertically
        text: "Voltage (V)",
        showarrow: false,
        font: { size: 14, color: "green", family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true }
      }
    ]
  };
  Plotly.newPlot('myDiv1', data, layout);
  var data = [
    {
        domain: { x: [0, 1], y: [0, 1.5] },
        value: 10,
        title: { text: "",font: { size: 14,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
        gauge: {
          axis: {
              range: [0, 15],
              tickvals: [0, 5, 10, 15],
              tickfont: {  // Adding font settings for the tick labels
                  size: 10,  // Specify the desired font size for the tick labels
                  family: "Arial, sans-serif",  // Specify the font family for the tick labels
                  color: "black"  // Specify the font color for the tick labels
              }
          }
      }
  }
  ];
  var layout = {
    width: 350,
    height: 120,
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
        value: 450,
        title: { text: "",font: { size: 14,  family: "Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", bold: true, color: "green" } },
        type: "indicator",
        mode: "gauge",
        gauge: {
          axis: {
              range: [0, 1000],
              tickvals: [0, 200, 400, 600, 800, 1000],
              tickfont: {  // Adding font settings for the tick labels
                  size: 10,  // Specify the desired font size for the tick labels
                  family: "Arial, sans-serif",  // Specify the font family for the tick labels
                  color: "black"  // Specify the font color for the tick labels
              }
          }
      }
  }
  ];
  var layout = {
    width: 350,
    height: 120,
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