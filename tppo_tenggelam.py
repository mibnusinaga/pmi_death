# IMPORT LIBRARY
import pandas as pd
import numpy as np
import folium
from folium import FeatureGroup, LayerControl, Map, Marker
from  streamlit_folium import folium_static, st_folium
import streamlit as st
from folium.features import DivIcon
from folium.plugins import FloatImage


st.set_page_config(layout = 'wide')

# import dataset 
df = pd.read_csv('data/tppo_tenggelam.csv', sep = ';')

#create folium object

my_map = folium.Map(location=[3.1651958, 96.4204231],
                    zoom_start=6,  zoom_control=False)

folium.TileLayer(
        tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains='abcd'
    ).add_to(my_map)



# grafik
folium.map.Marker(
    [2.200068, 86.244171],
    icon=DivIcon(
        icon_size=(100,200),
        icon_anchor=(0,0),
        html=
                '''<p style="font-family:Georgia Pro Regular;font-size:10px;color:white;">
                Grafik jumlah PMI meninggal per tahun (2008-2022).
                </p><br>'''
        )
    ).add_to(my_map)
folium.map.Marker(
    [3.233068, 86.344171],
    icon=DivIcon(
        icon_size=(650,200),
        icon_anchor=(0,0),
        html='''<img src="https://github.com/mibnusinaga/pmi_death/blob/main/data/pmi_tenggelam.png?raw=true"style="width:560px;height:200px;"><br>'''
        )
    ).add_to(my_map)



# text jumlah korban meninggal
folium.map.Marker(
    [5.533068, 103.644171],
    icon=DivIcon(
        icon_size=(650,200),
        icon_anchor=(0,0),
        html='<h5 style="font-family:Georgia Pro Regular;color:silver;">Tercatat</h5><br>'
        )
    ).add_to(my_map)
folium.map.Marker(
    [5.523068, 103.644171],
    icon=DivIcon(
        icon_size=(650,200),
        icon_anchor=(0,0),
        html=
            '''<p style="color:crimson;font-size:70px;font-family:Georgia Pro Regular;">566</p>'''
        )
    ).add_to(my_map)
folium.map.Marker(
    [3.933068, 103.644171],
    icon=DivIcon(
        icon_size=(650,200),
        icon_anchor=(0,0),
        html=
            '<h5 style="font-family:Georgia Pro Regular;color:silver;">PMI meninggal</h5>'
        )
    ).add_to(my_map)


# text judul paragraf dan paragraf
folium.map.Marker(
    [7.333068, 86.244171],
    icon=DivIcon(
        icon_size=(450,200),
        icon_anchor=(0,0),
        html='<h3 style="font-family:Georgia Pro Regular;color:white;">Kematian Pekerja Migran Ilegal Indonesia di Selat Malaka : Segitiga Bermudanya PMI</h3>'
        )
    ).add_to(my_map)
folium.map.Marker(
    [5.533068, 86.244171],
    icon=DivIcon(
        icon_size=(650,200),
        icon_anchor=(0,0),
        html='<p style="font-family:Georgia Pro Regular;color:white;font-size:10px;">Oleh : </hp>'+"<a href=https://www.linkedin.com/in/mibnusinaga/ target=_blank>M Ibnu Sinaga</a>"
        )
    ).add_to(my_map)
folium.map.Marker(
    [5.200068, 86.244171],
    icon=DivIcon(
        icon_size=(400,200),
        icon_anchor=(0,0),
        html=
                '''<p style="font-family:Georgia Pro Regular;font-size:10px;color:white;">
                Imigrasi Pekerja Migran Indonesia (PMI) yang ilegal ke wilayah negara Malaysia dan Singapura
                ataupun sebaliknya lewat jalur laut, kerap kali mengalami insiden tenggelamnya kapal akibat 
                ketidaklayakan kapal dan menempuh jalur perairan berbahaya demi menghindari petugas.
                Visualisasi ini menunjukkan semua insiden yang mengakibatkan PMI 
                meninggal, dengan data yang dikumpulkan berasal dari sampel berita publik Indonesia (Januari 2008-Oktober 2022).
                </p><br>'''
        )
    ).add_to(my_map)

# text metodologi


# text perairan
folium.map.Marker(
    [5.950124, 98.223917],
    icon=DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<h7 style="font-family:Georgia Pro Regular;color:silver;">Selat Malaka</h7>',

        )
    ).add_to(my_map)
folium.map.Marker(
    [0.694966, 104.988742],
    icon=DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<h7 style="font-family:Georgia Pro Regular;color:silver;">Laut Natuna</h7>',

        )
    ).add_to(my_map)


# membuat garis perairan
folium.PolyLine(locations = [[5.546413, 96.075917],[5.635349, 100.049955]],
                             color = 'White',
                             weight = 0.5,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[5.546413, 96.075917],[0.543961, 103.919291]],
                             color = 'White',
                             weight = 0.5,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[5.635349, 100.049955],[0.543961, 103.919291]],
                             color = 'White',
                             weight = 0.5,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[2.696597, 104.218442],[0.761225, 105.547874]],
                             color = 'White',
                             weight = 0.5,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[2.696597, 104.218442],[0.543961, 103.919291]],
                             color = 'White',
                             weight = 0.5,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[0.543961, 103.919291],[0.761225, 105.547874]],
                             color = 'White',
                             weight = 0.5,
                             opacity=1).add_to(my_map)



# Adding Custom Markers 
for lat, lon, death, posisi, alive, sumber, cause, tgl, laut, link in zip(df['lat'], df['lon'], 
                                                  df['jumlah_meninggal'], df['posisi_karam'],
                                                  df['jumlah_selamat'], df['sumber'],
                                                  df['penyebab'], df['tanggal'], df['perairan_besar'],
                                                  df['link']):
    folium.CircleMarker(location=[lat,lon],
                  weight=1,
                  radius=death*0.3,
                  popup=folium.Popup("<h5><b>"+laut+"<br>"+
                                     posisi+"<br></b>"+
                                     tgl+"<br></b>"+
                                     "<br></b>"+
                                     "Sebanyak </b>"+"<b>"+str(death)+"</b>"+
                                     " orang meninggal dunia dan "+"<b>"+str(alive)+"</b>"+" orang selamat, "+
                                     "sementara penyebab kecelakaan "+str(cause)+".<br>"+
                                     "<br></b>"+
                                     "sumber :&nbsp"+
                                     "<a href="+link+" target=_blank>"+sumber+"</a>",
                                     max_width=len(f"name= {posisi}")*10),
                  color='crimson', 
                  fill=True).add_to(my_map)

    
st_folium(my_map, width=1000, height=400)
