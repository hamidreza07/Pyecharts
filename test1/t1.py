from itertools import count
from flask import Flask,redirect,url_for,render_template,request,session
from datetime import timedelta
from pyecharts.charts import *
from pyecharts import options as opts
import datetime
from pyecharts.faker import Faker
app=Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(milliseconds=0)



@app.route("/",methods=["POST","GET"])
def start():
    if request.method=="POST":
       
        user=request.form["Charts"]
        session["user"]=user
        charts={" bar chart":"bar"," pie plot":"pie"," bar3d chart":"bar3d"," Box plot":"Boxplots"
                    ," Calendar":"Calendarplot"," EffectScatter":"EffectScatterplot"," Funnel":"Funnelplot"
                    ," Gauge":"Gaugeplot"," Graph":"Graphplot"," HeatMap":"HeatMapplot"," Kline":"Klineplot"," line":"lineplot"
                    ," line3d":"line3dplot"," Liquid":"Liquidplot"," Parallel":"Parallelchart"
                    ," PictorialBar":"PictorialBarchart"," Polar":"Polarchart"," Radar":"Radarchart"," Scatter":"Scatterplot"
                    ," Scatter3D":"Scatter3Dplot"," WordCloud":"WordCloudplot"
                    }

        for item in charts:
            if user==item:
                return redirect(url_for(charts[item]))

   
    else:
        if "user" in session:
            return redirect(url_for("chart"))
        return render_template("main.html")


@app.route("/barcharts",methods=["POST","GET"])
def bar():
    if request.method=="POST":
       
        user=request.form["nm"]
        user1=request.form["nm1"]
        user2=request.form["nm2"]
        user3=request.form["nm3"]
        user4=request.form["nm3"]
        session["user"]=user
        session["user1"]=user1
        session["user2"]=user2
        session["user3"]=user3
        session["user4"]=user4
        xaxis=eval(user)
        yaxis=eval(user2)
        (Bar()
        .add_xaxis(xaxis)
        .add_yaxis(user1, yaxis)
        .set_global_opts(title_opts=opts.TitleOpts(title=user3, subtitle=user4))
        .render(path="templates/result.html") # generate a local HTML file
        )
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("bar"))
        return render_template("barcharts.html")

@app.route("/bar3d",methods=["POST","GET"])
def bar3d():
    if request.method=="POST":
       
        user=request.form["nm"]
        user1=request.form["nm1"]
        user2=request.form["nm2"]
  
        session["user"]=user
        session["user1"]=user1
        session["user2"]=user2
  
        xaxis=eval(user)
        yaxis=eval(user1)
        zaxis=eval(user2)
        c =Bar3D()
        data=list()
        for count,item in enumerate(xaxis):
            data.append((item,yaxis[count],zaxis[count]))
        c.add(
        "",
        [[d[0], d[1], d[2]] for d in data],
        xaxis3d_opts=opts.Axis3DOpts(type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        c.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
        
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("bar3d"))
        return render_template("bar3d.html")


@app.route("/piechart",methods=["POST","GET"])
def pie():
    if request.method=="POST":
       
        user=request.form["nm"]
        user1=request.form["nm1"]

        session["user"]=user
        session["user1"]=user1
 
        columnname=eval(user)
        numbers=eval(user1)
        c = Pie()
        
        c.add("", [list(z) for z in zip(columnname, numbers)])
        c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("pie"))
        return render_template("piecharts.html")




@app.route("/Boxplot",methods=["POST","GET"])
def Boxplots():
    if request.method=="POST":
       
        user=request.form["nm"]
        user1=request.form["nm1"]

        session["user"]=user
        session["user1"]=user1
 
        x_axis=eval(user)
        v1=[eval(user1)]

        c = Boxplot()
        series_a = [opts.BoxplotItem(name=x_axis[0], value=d) for d in c.prepare_data(v1)]
        c.add_xaxis(xaxis_data=x_axis).add_yaxis("A", series_a)
        c.render(path="templates/result.html")
        return render_template("result.html")
        # f"<h1>{data}</h1>"
    else:
        if "user" in session:
            return redirect(url_for("Boxplots"))
        return render_template("boxplot.html")        


@app.route("/Calendarplot",methods=["POST","GET"])
def Calendarplot():
    if request.method=="POST":
       
        year1=int(request.form["startyear"])
        month1=int(request.form["startmonth"])
        day1=int(request.form["startday"])
        year2=int(request.form["endyear"])
        month2=int(request.form["endmonth"])
        day2=int(request.form["endday"])
        begin = datetime.date(year1, month1, day1)
        end = datetime.date(year2, month2, day2)
        numberlist=eval(request.form["listnumber"])
        data = [
            [str(begin + datetime.timedelta(days=i)) ]
            for i in  range((end - begin).days + 1 ) ]
        for count,item in enumerate(data):
            data[count].append(numberlist[count])
        c = (
            Calendar()
            .add("", data, calendar_opts=opts.CalendarOpts(range_=str(year2)))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                    max_=int(request.form["max"]),
                    min_=int(request.form["min"]),
                    orient="horizontal",
                    is_piecewise=True,
                    pos_top="230px",
                    pos_left="100px",
                    )
                 )
            )
        c.render(path="templates/result.html")
        return render_template("result.html")


    else:
        if "user" in session:
            return redirect(url_for("Calendarplot"))
        return render_template("calender.html")



@app.route("/EffectScatterplot",methods=["POST","GET"])
def EffectScatterplot():
    if request.method=="POST":
        
        user=eval(request.form["nm"])
        user1=eval(request.form["nm1"])

        session["user"]=user
        session["user1"]=user1
 
        c = EffectScatter().add_xaxis(user).add_yaxis("", user1)
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("EffectScatterplot"))
        return render_template("EffectScatter.html")



@app.route("/Funnelplot",methods=["POST","GET"])
def Funnelplot():
    if request.method=="POST":
        
        user=eval(request.form["nm"])
        user1=eval(request.form["nm1"])

        session["user"]=user
        session["user1"]=user1
 
        c = Funnel().add(request.form["nm2"], [list(z) for z in zip(user, user1)])
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Funnelplot"))
        return render_template("Funnel.html")


@app.route("/Gaugeplot",methods=["POST","GET"])
def Gaugeplot():
    if request.method=="POST":
        
        user=(request.form["nm"])
        user1=eval(request.form["nm1"])

        session["user"]=user
        session["user1"]=user1
 
        c = Gauge().add(
        "",
        [(request.form["nm"], request.form["nm1"])],
        detail_label_opts=opts.GaugeDetailOpts(formatter="{value}"),
        title_label_opts=opts.GaugeTitleOpts(
            font_size=40, color="blue", font_family="Microsoft YaHei"
        ),
        )
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Gaugeplot"))
        return render_template("Gauge.html")

@app.route("/Graphplot",methods=["POST","GET"])
def Graphplot():
    if request.method=="POST":
        
        user=eval(request.form["nm"])
        user1=eval(request.form["nm1"])

        session["user"]=user
        session["user1"]=user1
        nodes=[]
        l={}
        for count,item in enumerate(user):
            
            l["name"]=item
            l["symbolSize"]=user1[count]
            l_copy=l.copy()
            nodes.append(l_copy)

        links = []
        for i in nodes:
            for j in nodes:
                links.append({"source": i.get("name"), "target": j.get("name")})
        c = Graph().add("", nodes, links, repulsion=8000)
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Graphplot"))
        return render_template("Graph.html")



@app.route("/HeatMapplot",methods=["POST","GET"])
def HeatMapplot():
    if request.method=="POST":
        
        columns=eval(request.form["nm"])
        rows=eval(request.form["nm1"])
        xnum=eval(request.form["nm2"])
        ynum=eval(request.form["nm3"])
        mainnum=eval(request.form["nm4"])


        value = []
        for count,item in enumerate(xnum):
            l=[]
            l.append(item)
            l.append(ynum[count])
            l.append(mainnum[count])
            value.append(l)
        c = (
            HeatMap()
            .add_xaxis(columns)
            .add_yaxis("",rows, value)
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )


        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("HeatMapplot"))
        return render_template("HeatMap.html")






@app.route("/Klineplot",methods=["POST","GET"])
def Klineplot():
    if request.method=="POST":
       
        year=(request.form["startyear"])
        month=(request.form["startmonth"])
        day=int(request.form["day"])
    

        open=eval(request.form["nm1"])
        close=eval(request.form["nm2"])
        low=eval(request.form["nm3"])
        high=eval(request.form["nm4"])


        data = []
        for count,item in enumerate(open):
            l=[]
            l.append(item)
            l.append(close[count])
            l.append(low[count])
            l.append(high[count])
            data.append(l)


       
        c=str(year)+"/"+str(month)+"/"+"{}"

        c = (
        Kline()
        .add_xaxis([c.format(i + 1) for i in range(day)])
        .add_yaxis("kline", data)
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(is_scale=True),
            xaxis_opts=opts.AxisOpts(is_scale=True),
        )
         )

        c.render(path="templates/result.html")
        return render_template("result.html")

    else:
        if "user" in session:
            return redirect(url_for("Klineplot"))
        return render_template("Kline.html")


@app.route("/lineplot",methods=["POST","GET"])
def lineplot():
    if request.method=="POST":
       
        user=eval(request.form["nm"])
        user1=eval(request.form["nm1"])

        c = Line()
        c.add_xaxis(user)
        for count,item in enumerate(user1):
            c.add_yaxis("series"+str(count), item)


        
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("lineplot"))
        return render_template("line.html")


@app.route("/line3dplot",methods=["POST","GET"])
def line3dplot():
    if request.method=="POST":
       
        xaxis=eval(request.form["x"])
        yaxis=eval(request.form["y"])
        zaxis=eval(request.form["z"])


        data = []
        for count,item in enumerate(xaxis):
   
            data.append([item, yaxis[count], zaxis[count]])
        c = (
            Line3D()
            .add(
                "",
                data,
                xaxis3d_opts=opts.Axis3DOpts(type_="value"),
                yaxis3d_opts=opts.Axis3DOpts(type_="value"),
                grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
            )
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                    max_=30, min_=0
                )
            )
        )

        
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("line3dplot"))
        return render_template("line3d.html")


@app.route("/Liquidplot",methods=["POST","GET"])
def Liquidplot():
    if request.method=="POST":
        
        user=(request.form["tag"])
        anim=(request.form["animation"])
        number1=int(request.form["show"])
        number2=int(request.form["liquid"])
        session["tag"]=user
        session["animation"]=anim
        session["show"]=number1
        session["liquid"]=number2

        if anim=="OK":
            c = Liquid().add(user, [number1/100, number2/100], is_animation=True)
        else:
            c = Liquid().add(user, [number1/100, number2/100], is_animation=False)
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Liquidplot"))
        return render_template("Liquid.html")



def Graphplot():
    if request.method=="POST":
        
        user=eval(request.form["nm"])
        user1=eval(request.form["nm1"])

        session["user"]=user
        session["user1"]=user1
        nodes=[]
        l={}
        for count,item in enumerate(user):
            
            l["name"]=item
            l["symbolSize"]=user1[count]
            l_copy=l.copy()
            nodes.append(l_copy)

        links = []
        for i in nodes:
            for j in nodes:
                links.append({"source": i.get("name"), "target": j.get("name")})
        c = Graph().add("", nodes, links, repulsion=8000)
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Graphplot"))
        return render_template("Graph.html")



@app.route("/Parallelchart",methods=["POST","GET"])
def Parallelchart():
    if request.method=="POST":
        
        data=eval(request.form["data"])
        name=eval(request.form["name"])
        nameseries=request.form["series"]


        value = []
        for count,item in enumerate(name):
            di={}
            di["dim"]=count
            di["name"]=item
            value.append(di)
            
        c = (
             Parallel()
            .add_schema(value)

        )
        c.add(nameseries, data)
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Parallelchart"))
        return render_template("Parallelchart.html")





@app.route("/PictorialBar",methods=["POST","GET"])
def PictorialBarchart():
    if request.method=="POST":
       
        user=eval(request.form["nm"])
        user1=request.form["nm1"]

        session["user"]=user
        session["user1"]=user1
 
        columnname=list(user)
        numbers=eval(user1)
        c = (
            PictorialBar()
            .add_xaxis(columnname)
            .add_yaxis(
                "",
                numbers,
                symbol_size=18,
                symbol_repeat="fixed",
                symbol_offset=[0, 0],
                is_symbol_clip=True,
            )
            .reversal_axis()
        )
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("PictorialBarchart"))
        return render_template("PictorialBar.html")



@app.route("/polar",methods=["POST","GET"])
def Polarchart():
    if request.method=="POST":
       
        user=request.form["nm"]
        user1=request.form["nm1"]
        
  
        session["user"]=user
        session["user1"]=user1
      
  
        xaxis=eval(user)
        yaxis=eval(user1)
        
        show=request.form["show"]

        data = []
        for count,item in enumerate(xaxis):
            t=(item,yaxis[count])
            data.append(t)

        if show=="OK":    
            c = Polar().add("", data, type_="line", label_opts=opts.LabelOpts(is_show=True))
        else:
            c = Polar().add("", data, type_="line", label_opts=opts.LabelOpts(is_show=False))
        
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Polarchart"))
        return render_template("Polar.html")

@app.route("/Radar",methods=["POST","GET"])
def Radarchart():
    if request.method=="POST":
        
        name=eval(request.form["series"])
        numbers=eval(request.form["numbers"])
        cnames = {
            1:            'green',
            2:         'red',
            3:                 'black',
            4:           'blue',
            5:                'cyan',
            6:                'magenta',
            7:               'yellow',
            8:                'black',
     
                    }
        c = Radar()
        for count,n in enumerate( numbers):
            globals()['name_%s' % (count+1)] = [(tuple(n))]
            c.add(name[count], [(tuple(n))],color=cnames[count+1])


        c.add_schema(
            schema=[
                opts.RadarIndicatorItem(name="point "+str(i), max_=len(name_1[0])*5) for i in range( len(name_1[0]))
        
            ]
        )
        
  
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
      

        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Radarchart"))
        return render_template("Radar.html")


@app.route("/Scatter",methods=["POST","GET"])
def Scatterplot():
    if request.method=="POST":
       
        xaxis=eval(request.form["xaxis"])
        yaxis=eval(request.form["yaxis"])
        nameseries=eval(request.form["series"])

        session["xaxis"]=xaxis
        session["yaxis"]=yaxis
        session["series"]=nameseries



        c = Scatter()
                
        c.add_xaxis(xaxis) 

        for count , item in enumerate( yaxis):
             c.add_yaxis(nameseries[count], item)
      
        
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Scatterplot"))
        return render_template("Scatter.html")






@app.route("/Scatter3D",methods=["POST","GET"])
def Scatter3Dplot():
    if request.method=="POST":
       
        xaxis=eval(request.form["xaxis"])
        yaxis=eval(request.form["yaxis"])
        zaxis=eval(request.form["zaxis"])


        nameseries=(request.form["series"])


        session["xaxis"]=xaxis
        session["xaxis"]=yaxis
        session["xaxis"]=zaxis

        session["series"]=nameseries
        data=[]
        c =Scatter3D()


        data=list()
        for count,item in enumerate(xaxis):
            data.append((item,yaxis[count],zaxis[count]))
        c.add(
        nameseries,
        [[d[0], d[1], d[2]] for d in data],
        xaxis3d_opts=opts.Axis3DOpts(type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        c.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
            
           
        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("Scatter3Dplot"))
        return render_template("Scatter3D.html")





@app.route("/WordCloud",methods=["POST","GET"])
def WordCloudplot():
    if request.method=="POST":
       
        columnname=eval(request.form["series"])
        numbers=eval(request.form["numbers"])

        session["user"]=columnname
        session["user1"]=numbers
 
        words=[]
        for count,name in enumerate (columnname):
            a=(name,numbers[count])
            words.append(a)

       
        c = WordCloud().add("cloud", words)

        c.render(path="templates/result.html")
        return render_template("result.html")
    else:
        if "user" in session:
            return redirect(url_for("WordCloudplot"))
        return render_template("WordCloud.html")


@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("start"))


if __name__=="__main__":
    app.run(debug=True)