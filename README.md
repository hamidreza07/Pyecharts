# Zhaav-Echarts

Repository for Echarts integration with Zhaav Ecosystem.






## 📣 Introduction to pyecharts
[Apache ECharts](https://github.com/apache/echarts) is easy-to-use, highly interactive and highly performant javascript visualization library under Apache license. Since its first public release in 2013, it now dominates over 74% of Chinese web front-end market. Yet Python is an expressive language and is loved by data science community. Combining the strength of both technologies, [pyecharts](https://github.com/pyecharts/pyecharts) is born.

## ✨ Feature highlights

* Simple API, Sleek and method chaining
* Support 30 + popular charts
* Suppot data science tools: Jupyter Notebook, JupyterLab, nteract
* Integrate with Flask，Django at ease
* Easy to use and highly configurable
* Detailed documentation and examples.
* More than 400+ geomaps assets for geograpic information processing

## 🔰 Installation

**pip install**
```shell
$ pip install pyecharts
```

**Install from source**
```shell
$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```
## Startup
1. build docker image:
 ```shell 
 Docker build -t pyecharts .
 ```
2. run docker:
 ```shell 
 Docker run -p 8080:8080 -td pyecharts
 ```

Navigate to **http://localhost:8080**


## Objectives
1. create an API endpoint for each of the charts. this endpoint should listen for User's `HTTP POST` method and  render the chart. endpoint  implemented via Flask  and the endpoint should be able to handle multiple requests at the same time via RESTful API manner.
2. create a web page for each of the charts. this page should contain the chart and the API endpoint.


### How to do it?
1. Start page: Using `HTTP POST` and `HTTP GET` Flask method we can easily create first page.in this method we create function include chart names and by `HTTP POST` method we are abled to redirect to the each chart pages.
2. Charts page : For each chart we create a function and by `HTTP POST` we gather information from each web page.after that by using pyecharts we create a charts page.

## Charts Description:

This tables presents the description of charts on this project And what chart will it support according to   [Apache ECharts](https://echarts.apache.org/examples/en/index.html) site.


ID|Charts|tset file|details|support
--|---|---|---|---
1|Bar3D<br>|[Bar3d Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_bar3d.py)<br>| A bar 3D chart represents quantitative information. This chart consists 3 dimention (x,y,z)  | Bar3D
2|Bar <br>|[Bar Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_bar.py)<br> |Bar charts show the frequency counts of values for the different levels of a categorical or nominal variable. This chart consists 2 dimention (x,y),title,subtitle and tag bar  | Basic Bar
3|Boxplot<br>|[Boxplot Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_boxplot.py)<br>| In descriptive statistics, a box plot or boxplot (also known as box and whisker plot) is a type of chart often used in explanatory data analysis. This plot consists rows name and numbers  | Boxplot Light Velocity
4|Calendar <br>|[calender Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_calendar.py)<br> |Calendar heat charts visualize patterns in temporal data by aggregating incidents into a calendar grid. . This chart consists list of number,maximum and minimum of showing range and start and end  date include Year,Month,Day |Calendar Heatmap
5|EffectScatter <br>|[Effect Scatter Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_effectscatter.py)<br> |The scatter plot uncovers relationships in data. "Relationships" means that there is some pattern between X and Y. This chart consists rows name and numbers |Effect Scatter Chart
6|Funnel <br>|[Funnel Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_funnel.py)<br> |A funnel chart is a specialized chart type that demonstrates the flow of users through a business or sales process.  This chart consists rows name,numbers and tag |Funnel Chart
7|Gauge <br>|[Gauge Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_gauge.py)<br> |Gauge charts, also known as dial charts or speedometer charts, use needles to show information as a reading on a dial.  This chart consists names,number of the Guage |Simple Gauge
8|HeatMap <br>|[HeatMap Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_heatmap.py)<br> |Heat Map Chart, or Heatmap is a two-dimensional visual representation of data, where values are encoded in colors, delivering a convenient, insightful view of information. This chart consists x axis number,yaxis number, main number,columns and rows name of the Guage |Heatmap on Cartesian
9|Candlestick <br>|[Kline Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_kline.py)<br> |Heat Map Chart, or Heatmap is a two-dimensional visual representation of data, where values are encoded in colors, delivering a convenient, insightful view of information. This chart consists x axis number,yaxis number, main number,columns and rows name of the Guage |Heatmap on Cartesian
10|line <br>|[line Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_line.py)<br> |A line chart is a graphical representation of an asset's historical price action that connects a series of data points with a continuous line. This chart consists  x axis name and numbers  | Basic Line Chart
11|line 3D <br>|[line 3d Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_line.py)<br> |A line chart is a graphical three dimention representation of an asset's historical price action that connects a series of data points with a continuous line. This chart consists  x axis,y axis,z axis numbers | 3D Line
12|Liquid <br>|[Liquid Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_liquid.py)<br> | This chart consists  show and liquid numbers,alonge with tag name and activation of animation  |-
13|Parallel  <br>|[Parallel chart Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_parallel.py)<br> |Parallel coordinates is a visualization technique used to plot individual data elements across many performance measures. This chart consists  data,name of dimention and name of series  | Basic Parallel
14|Pictorial Bar <br>|[Pictorial Bar Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_pictorialbar.py)<br> |A pictorial Bar is are pictorial representations of the numerical data.  This chart consists rows name,numbers  |PictorialBar 
15|pie chart <br>|[pie chart Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_pie.py)<br> |a circular chart cut by radii into segments illustrating relative magnitudes or frequencies. This chart consists rows name,numbers  |PictorialBar
16|Polar <br>|[Polar Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_polar.py)<br> | This chart consists  show and polar numbers,alonge with series of numbers and activation of showing numbers  |- 
17|Radar <br>|[Radar Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_radar.py)<br> |Radar Charts are used to compare two or more items or groups on various features or characteristics. This chart consists series name and numbers  |Basic Radar Chart
18|Scatter <br>|[Scatter Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_scatter.py)<br> |A scatter chart, also called a scatter plot, is a chart that shows the relationship between two variables.  This chart consists 2 dimention (x,y),name series  | Basic Scatter Chart
19|Scatter 3d <br>|[Scatter 3d  Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_scatter.py)<br> |3D scatter plots are used to plot data points on three axes in the attempt to show the relationship between three variables.  This chart consists 3 dimention (x,y,z),name series  | Scatter3D
20|Word Cloud <br>|[Word Cloud  Test](https://github.com/pyecharts/pyecharts/blob/dev/test/test_wordcloud.py)<br> |A Word Cloud chart is a visual representation of text data in which the importance or frequency of individual words is represented using font size and color. This chart consists names and the size of text  | Scatter3D