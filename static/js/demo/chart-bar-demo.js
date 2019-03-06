// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["20 Dec", "21 Dec", "22 Dec", "23 Dec", "24 Dec", "25 Dec"],
    datasets: [{
      label: "PM2.5",
      backgroundColor: "rgba(153, 102, 255, 0.2)",
      borderColor: "rgba(153, 102, 255, 0.2)",
      data: [53, 68, 33, 13, 51, 27,9],
    },
    {
      label: "PM10",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [93,118, 81, 53, 91, 65, 26],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'day'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 4
        }
      }],
      yAxes: [{
        unit: 'μg/m3',
        ticks: {
          min: 0,
          max: 120,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: true,
      text: String,
    }
  }
});
