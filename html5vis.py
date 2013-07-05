#!/usr/bin/env python

# make a horizontal bar chart
template = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link href="" rel="shortcut icon">
<title></title>

<!-- embedded  scripts -->
<script src="http://cdnjs.cloudflare.com/ajax/libs/json2/20110223/json2.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/d3/2.8.1/d3.v2.min.js"></script>

<!-- data -->
<script id="data" type="text/plain">
%s
</script>

<!-- embedded styles -->
<style>
* { margin:0px; padding:0px; }

body {
    font-family: "Helvetica Neue", "Helvetica", Arial, san-serif;
    font-size: 14px;
    padding:0px;
}

h1,h2,h3,h4,h5,h6 {
    font-style:normal;
    font-weight:300;
}

.container {
    width: 410px;
    height: 600px;
    margin:100px auto;

}

</style>
</head>

<body>

<div class="container">
<h2>Some chart</h2>
</div>

<!-- visualization -->
<script type="text/javascript">

// data
var data = JSON.parse(document.getElementById("data").text);
var chart_width = 400;
var chart_height = 400;
var bar_width = 40; 

var xscale = d3.scale.ordinal()
                .domain(data.map(function(i){ return i.label;}))
                .rangeBands([0, chart_width], .2);

var yscale = d3.scale.linear()
                .domain([0, d3.max(data, function(i){ return i.value;})])
                .range([0, chart_height]);

chart = d3.select(".container")
          .append("svg")
          .attr("width", chart_width + 100)
          .attr("height", chart_height + 100);

bars = chart.selectAll('rect')
     .data(data)
   .enter()
     .append('rect')
     .attr("width", xscale.rangeBand())
     .attr("height", function(d){ return yscale(d.value); })
     .attr("fill", "orange")
     .attr("x", function(d){ return xscale(d.label) + 10; })
     .attr("y", function(d){ return chart_height - yscale(d.value) + 10;})
     .on("mouseover", function(){
        d3.select(this).attr("fill", "yellow");
     })
     .on("mouseout", function(){
        d3.select(this).attr("fill", "orange");
     });

labels = chart.selectAll('text')
              .data(data)
            .enter()
              .append('text')
              .attr("y", function(d) { return chart_height + 30 })
              .attr("x", function(d) { return xscale(d.label) + 10 ;})
              .text(function(d){ return d.label;})

xaxis = chart.append("line")
             .attr("x1", 10)
             .attr("x2", chart_width  + 10)
             .attr("y1", chart_height + 10)
             .attr("y2", chart_height + 10)
             .attr("class", "xaxis")
             .attr("stroke", "#aaa");

xticks = chart.selectAll("line.xticks")
             .data(data).enter()
             .append("line")
             .attr("x1", function(d){ return 10 + xscale(d.label) + xscale.rangeBand()/2;})
             .attr("x2", function(d){ return 10 + xscale(d.label) + xscale.rangeBand()/2;})
             .attr("y1", chart_height + 5)
             .attr("y2", chart_height + 15)
             .attr("class", "xticks")
             .attr("stroke", "#aaa");

yaxis = chart.append("line")
             .attr("x1", 10)
             .attr("x2", 10)
             .attr("y1", 10)
             .attr("y2", chart_height + 10)
             .attr("class", "yaxis")
             .attr("stroke-width",1)
             .attr("stroke", "#aaa");

</script>
</body>
</html>

"""



#
# visualize.py python script
#

import json

data = [
    {"label": "dogs", "value": 10},
    {"label": "foos", "value": 12},
    {"label": "bars", "value": 14},
    {"label": "bazs", "value": 13},
    {"label": "cols", "value": 14},
    {"label": "dars", "value": 13},
    {"label": "cats", "value": 19},
]

# write out html file
outfile = "visualize.html"
with open(outfile, "w") as fh:
    html = template % json.dumps(data)
    fh.write(html)

import subprocess as sp
sp.check_call(["open", outfile])
