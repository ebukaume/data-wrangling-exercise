var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 1100 - margin.left - margin.right,
    height = 550 - margin.top - margin.bottom;


function plot({target, data}){
  var svg = d3.select(target)
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  d3.csv(data,
    function(d){
      return { date : d3.timeParse("%Y-%m-%d")(d.date), price : d.price }
    },
    function(data) {
      var x = d3.scaleTime()
        .domain(d3.extent(data, function(d) { return d.date; }))
        .range([ 0, width ]);
      svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      var y = d3.scaleLinear()
        .domain([0, d3.max(data, function(d) { return +d.price; })])
        .range([ height, 0 ]);
      svg.append("g")
        .call(d3.axisLeft(y));

      svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("d", d3.line()
          .x(function(d) { return x(d.date) })
          .y(function(d) { return y(d.price) })
          )
  })
}

plot({
  target: "#daily_chart",
  data: "output/henry_hub_gas_daily_prices.csv"
});

plot({
  target: "#monthly_chart",
  data: "output/henry_hub_gas_monthly_prices.csv"
});