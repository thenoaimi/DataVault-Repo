from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import pandas as pd
import plotly.graph_objs as go
import plotly as plotly1
from .models import Image
from .models import ProbedataSatellite,FnirsDeoxySatellite,FnirsOxySatellite
# Create your views here.
def dataprocess(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    if request.method == "POST":
        experiment_id=  request.POST.get('Experimentid')
        if experiment_id=='1':
            return redirect('/TEST/experiment1/')
        else:
            return redirect('/TEST/experiment2/')
    return render(request, 'TEST/dataprocessing.html')

def experiment2(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    if request.method == "POST":
        j=[]
        for i in range(11,54):
            j.append(str(i))
        patient_id=  request.POST.get('patient_id')
        session_id=int(request.POST.get('sessionid'))
        if(patient_id not in j):
            return HttpResponse("This patient ID does not exist in Experiment 2")
        querySet=Image.objects.filter(patientid=patient_id,sessionid=session_id).values()
        df = pd.DataFrame(querySet)
        columns=df['datatype']
        return render(request, 'TEST/fNIRsdatatype.html',  {'columns': columns,'patient_id':patient_id,'sessionid':session_id})
    return render(request,'TEST/experiment2.html')

def experiment1(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    if request.method == "POST":
        j=[]
        for i in range(1,11):
            j.append(str(i))
        patient_id= request.POST.get('patient_id')
        datatype=request.POST.get('datatype')
        probetype=request.POST.get('probetype')
        if(patient_id not in j):
            return HttpResponse("This patient ID does not exist in Experiment 1 ")
        else:
            if(probetype=='MES'):
                querySet = ProbedataSatellite.objects.filter(patient_id=patient_id,stimuli_type=datatype).values()
            else:
                if(probetype=='oxy'):
                    querySet = FnirsOxySatellite.objects.filter(patient_id=patient_id, fnirs_type=datatype).values()
                else:
                    querySet = FnirsDeoxySatellite.objects.filter(patient_id=patient_id, fnirs_type=datatype).values()
            df = pd.DataFrame(list(querySet))
            length=df.shape[0]
            columns=df.columns.tolist ()
            column123=[]
            for i in columns:
                if 'ch' in i:
                    column123.append(i)
            columns=column123
            return render(request, 'TEST/probedataex.html',  {'columns': columns,'patient_id':patient_id,'datatype':datatype,'probetype':probetype,'length':length})
    return render(request,'TEST/experiment1.html')

def probedata(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    return render(request, 'TEST/experiment2.html')

def fNIRs(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    if request.method == "POST":
        patient_id = request.POST.get('patient_id')
        datatype = request.POST.get('datatype')
        session_id = request.POST.get('session_id')
        querySet = Image.objects.filter(patientid=patient_id, sessionid=session_id,datatype=datatype).values()
        df = pd.DataFrame(list(querySet))
        image_data=df['data']
        return HttpResponse(image_data, content_type="image/png")
    return redirect("/index/")

def plot(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    if request.method == "POST":
        patient_id= request.POST.get('patient_id')
        datatype=request.POST.get('datatype')
        quantity1=int(request.POST.get('quantity1'))
        quantity2=int(request.POST.get('quantity2'))
        probetype=request.POST.get('probetype')
        if (probetype == 'MES'):
            querySet = ProbedataSatellite.objects.filter(patient_id=patient_id, stimuli_type=datatype).values()
        else:
            if (probetype == 'oxy'):
                querySet = FnirsOxySatellite.objects.filter(patient_id=patient_id, fnirs_type=datatype).values()
            else:
                querySet = FnirsDeoxySatellite.objects.filter(patient_id=patient_id, fnirs_type=datatype).values()
        df = pd.DataFrame(list(querySet))
        columns = df.columns.tolist()
        columnlist=[]
        for i in columns:
            c=request.POST.get(i)
            if(c=='1.1'):
                columnlist.append(i)
        listfin=[]
        listout=[]
        df=df.loc[quantity1:quantity2,columnlist]
        out=quantity2+1-quantity1
        for i in range(quantity1,quantity2+1):
            listfin.append(i)
        for j in range(out):
            listout.append(j)
        text = []
        for column in columnlist:
            x1=listfin
            y1=[k for k in df[column]]
            trace = go.Scatter(
                x=x1,
                y=y1,
                textposition='top center',
                mode='markers+text+lines',
                name=column,  # Style name/legend entry with html tags
                connectgaps=True  # 是否连接缺失值
            )
            text.append(trace)
        layout = go.Layout(
            autosize=False,
            width=3000,
            height=2000,
            xaxis=go.layout.XAxis(linecolor='black',
                                  linewidth=1,
                                  mirror=True),

            yaxis=go.layout.YAxis(linecolor='black',
                                  linewidth=1,
                                  mirror=True),

            margin=go.layout.Margin(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=4
            )
        )
        fig = go.Figure(data=text, layout=layout)
        graph_div = plotly1.offline.plot(fig, auto_open = True, output_type="div")
        return render(request, 'TEST/probedataplot.html',{'graph_div':graph_div,'patient_id':patient_id,'datatype':datatype,'probetype':probetype})
    return render(request,'TEST/probedataplot.html')