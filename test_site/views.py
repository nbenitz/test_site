from django.conf import settings
from django.core.mail import send_mail 

from .forms import ContactForm
from django.shortcuts import render
from django.core import management
from django.core.management.commands import loaddata
from django.http.response import HttpResponse

from django.views.generic import TemplateView

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
from test_site.covid19_data_clean import clean_data




# Create your views here.
    
def plott(request):
    
    clean_data()
    
    # read_csv
    confirmed_df = pd.read_csv('datasets/covid19/time_series_covid19_confirmed_global.csv')
    actives_df = pd.read_csv('datasets/covid19/time_series_covid19_actives_global.csv')
    recovered_df = pd.read_csv('datasets/covid19/time_series_covid19_recovered_global.csv')
    death_df = pd.read_csv('datasets/covid19/time_series_covid19_deaths_global.csv')
    country_df = pd.read_csv('datasets/covid19/cases_country.csv')

    # total number of confirmed, death and recovered cases
    confirmed_total = int(country_df['confirmed'].sum())
    deaths_total = int(country_df['deaths'].sum())
    recovered_total = int(country_df['recovered'].sum())
    active_total = int(country_df['active'].sum())
    
    # displaying the total stats

    total_stats = "<div style = 'background-color: #504e4e; padding: 30px '>" + \
    "<span style='color: #fff; font-size:30px;'> Confirmed: "  + str(confirmed_total) +"</span>" + \
    "<span style='color: red; font-size:30px;margin-left:20px;'> Deaths: " + str(deaths_total) + "</span>"+ \
    "<span style='color: lightgreen; font-size:30px; margin-left:20px;'> Recovered: " + str(recovered_total) + "</span>"+ \
    "</div>"
    
    sorted_country_df = country_df.sort_values('confirmed', ascending= False)
    
    context = {#"total_stats": total_stats,
               #"plot_worst_hit_countries":plot_worst_hit_countries(sorted_country_df, 10),
               "plot_cases_of_a_country":plot_cases_of_a_country('Paraguay', confirmed_df, actives_df, recovered_df, death_df),
               #"worst_hit_countries_Confirmed":worst_hit_countries_Confirmed(sorted_country_df)
               }
    return render(request, "plots/index.html", context)

def plot_worst_hit_countries(sorted_country_df, n):
    fig = px.scatter(sorted_country_df.head(n), 
                     x="country", y="confirmed", 
                     size="confirmed", color="country",
                     hover_name="country", size_max=60)
    fig.update_layout(
        title=str(n) +" Worst hit countries",
        xaxis_title="Countries",
        yaxis_title="Confirmed Cases",
        width = 800
    )    
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')
    return plot_div

def plot_cases_of_a_country(country, confirmed_df, active_df, recovered_df, death_df):
    """
    active_df = confirmed_df.loc[confirmed_df['country'] == 'Paraguay']
    recovered_list = recovered_df.loc[recovered_df['country'] == 'Paraguay'].iloc[:,4:].values.tolist()[0]
    deaths_list = death_df.loc[death_df['country'] == 'Paraguay'].iloc[:,4:].values.tolist()[0]
    active_df.iloc[:,4:] = active_df.iloc[:,4:].sub(recovered_list, axis='columns')
    active_df.iloc[:,4:] = active_df.iloc[:,4:].sub(deaths_list, axis='columns')
    print(active_df) """
    
    labels = ['deaths', 'recovered', 'actives', 'confirmed']
    colors = ['red', 'green', 'orange', 'blue']
    #mode_size = [6, 8]
    line_size = [1, 1, 1, 1]
    
    df_list = [death_df, recovered_df, active_df, confirmed_df]
    
    fig = go.Figure()
    
    for i, df in enumerate(df_list):
        if country == 'World' or country == 'world':
            x_data = np.array(list(df.iloc[:, 4:].columns))
            y_data = np.sum(np.asarray(df.iloc[:,4:]),axis = 0)
            
        else:    
            x_data = np.array(list(df.iloc[:, 49:].columns))
            y_data = np.sum(np.asarray(df[df['country'] == country].iloc[:,49:]),axis = 0)
            
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers',
                                 name=labels[i],
                                 line=dict(color=colors[i], width=line_size[i]),
                                 connectgaps=True,
                                 text = "Total " + str(labels[i]) +": "+ str(y_data[-1])
                                 ))
    
    fig.update_layout(
        title="COVID 19 cases of " + country,
        xaxis_title='Date',
        yaxis_title='No. of Confirmed Cases',
        margin=dict(l=20, r=20, t=40, b=20),
        #width = 800,
        #paper_bgcolor="lightgrey",
        
    )
    
    fig.update_yaxes(type="linear")
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div

def worst_hit_countries_Confirmed(sorted_country_df):
    fig = px.bar(
        sorted_country_df.head(10),
        x = "country",
        y = "confirmed",
        title= "Top 10 worst affected countries", # the axis names
        color_discrete_sequence=["pink"], 
        height=500,
        width=800
    )
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')
    return plot_div

def examplePlot():
    # Makes a simple plotly plot, and returns html to be included in template.
    x = np.linspace(0, 12.56, 41)
    y = np.sin(x)
    y2 = np.sin(1.2*x)

    data = [
        go.Scatter(
            name = 'Sin(x)',
            x=x,
            y=y,
        ),

        go.Scatter(
            name = 'Sin(1.2x)',
            x=x,
            y=y2,
        ),
    ]

    layout = go.Layout(
        xaxis=dict(
            title='x'
        ),

        yaxis=dict(
            title='Value',
            hoverformat = '.2f'
        ),
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = py.plot(fig, include_plotlyjs=False, output_type='div')

    return plot_div

def inicio(request):
    return render(request, "inicio.html", {})

def atributos_meta(request):
    valor = request.META.items()
    #valor.sort()
    html = []
    for k, v in valor:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def about(request):
    #management.call_command('dumpdata', 'estructura', output='estructura/fixtures/db.json', format='json')
    management.call_command('loaddata', 'db.json', format='json', app_label='estructura')
    return render(request, "about.html")
    loaddata

def contact(request):
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #    print(key, value)
        # for key in form.cleaned_data:
        #    print(key)
        #    print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "n.benitez.a@hotmail.com"]
        email_mensaje = "%s: %s enviado por %s" % (form_nombre, form_mensaje, form_email)
        send_mail(
            asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )
        print(form_email, email_mensaje, form_nombre)
        
    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, "contact.html", context)
    
    

