# IMPORT LIBRARY
import pandas as pd
import numpy as np
import folium
from folium import FeatureGroup, LayerControl, Map, Marker
from  streamlit_folium import folium_static, st_folium
import streamlit as st
from folium.features import DivIcon

st.set_page_config(layout = 'wide')


# import dataset 
df = pd.read_csv('data/tppo_tenggelam.csv', sep = ';')




#create folium object

my_map = folium.Map(
    location=[3.1651958, 96.8204231],
    zoom_start=6,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 
    attr='Esri.WorldImagery', 
)


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

folium.map.Marker(
    [7.333068, 86.844171],
    icon=DivIcon(
        icon_size=(450,200),
        icon_anchor=(0,0),
        html='<h3 style="font-family:Georgia Pro Regular">Kematian Pekerja Migran Ilegal Indonesia di Selat Malaka : Segitiga Bermudanya PMI</h3>'
        )
    ).add_to(my_map)

folium.map.Marker(
    [7.433068, 105.844171],
    icon=DivIcon(
        icon_size=(380,200),
        icon_anchor=(0,0),
        html=
                '''<p style="font-family:Georgia Pro Regular;color:silver;font-size:9px;">
                Oleh : M Ibnu Sinaga
                </p><br>'''
        )
    ).add_to(my_map)
folium.map.Marker(
    [7.233068, 105.544171],
    icon=DivIcon(
        icon_size=(380,200),
        icon_anchor=(0,0),
        html=
                '''<p style="font-family:Georgia Pro Regular;color:silver;font-size:9px;">
                mibnusinaga@gmail.com
                </p><br>'''
        )
    ).add_to(my_map)
folium.map.Marker(
    [7.000008, 105.744171],
    icon=DivIcon(
        icon_size=(380,200),
        icon_anchor=(0,0),
        html=
                '''<p style="font-family:Georgia Pro Regular;color:silver;font-size:9px;">
                mibnusinaga (linkedin)
                </p><br>'''
        )
    ).add_to(my_map)



folium.map.Marker(
    [5.533068, 86.844171],
    icon=DivIcon(
        icon_size=(380,200),
        icon_anchor=(0,0),
        html=
                '''<p style="font-family:Georgia Pro Regular;font-size:10px;">
                Imigrasi Pekerja Migran Indonesia (PMI) yang ilegal ke wilayah negara Malaysia dan Singapura
                ataupun sebaliknya lewat jalur laut, kerap kali mengalami insiden tenggelamnya kapal akibat 
                ketidaklayakan kapal dan menempuh jalur perairan berbahaya demi menghindari petugas.
                </p><br>'''
        )
    ).add_to(my_map)


folium.map.Marker(
    [4.033068, 86.844171],
    icon=DivIcon(
        icon_size=(380,200),
        icon_anchor=(0,0),
        html=

                '''<p style="font-family:Georgia Pro Regular;font-size:10px;">Visualisasi ini menunjukkan semua insiden
                tenggelamnya kapal pengangkut pekerja migran Indonesia mulai dari Januari 2009 hingga Oktober 2022.
                Ukuran lingkaran berwarna merah menunjukkan seberapa besar jumlah korban meninggal akibat insiden tersebut.
                Arahkan kursor pada lingkaran dan klik untuk mengetahui informasi lengkap mengenai setiap insiden.
                Setiap insiden kapal tenggelam 
                didata lokasi rinci perairan dan ditentukan wilayah perairan besarnya.
                Berdasarkan pendataan terdapat dua wilayah perairan yang umumnya terjadi kecelakaan,  
                yaitu perairan Selat Malaka dan Laut Natuna yang telah diproyeksikan melalui pembatas segitiga bergaris putih.
                </p><br>'''
        )
    ).add_to(my_map)
folium.map.Marker(
    [0.373068, 86.844171],
    icon=DivIcon(
        icon_size=(300,200),
        icon_anchor=(0,0),
        html=

                '''<p style="font-family:Georgia Pro Regular;color:silver;font-size:7px;">
                Metodologi : <br>                                                                            
                Data dikumpulkan dari sampel berita publik yang berbasis di Indonesia (Januari 2009-Oktober 2022),
                melalui proses ekstraksi dengan teknik web scraping. Untuk menjaga akurasi, data 
                dicocokkan kembali pada laman berita secara manual.
                </p><br>'''
        )
    ).add_to(my_map)

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

# Adding line
folium.PolyLine(locations = [[5.546413, 96.075917],[5.635349, 100.049955]],
                             popup = 'rute sama',
                             color = 'White',
                             weight = 1,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[5.546413, 96.075917],[0.543961, 103.919291]],
                             popup = 'rute sama',
                             color = 'White',
                             weight = 1,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[5.635349, 100.049955],[0.543961, 103.919291]],
                             popup = 'rute sama',
                             color = 'White',
                             weight = 1,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[2.696597, 104.218442],[0.761225, 105.547874]],
                             popup = 'rute sama',
                             color = 'White',
                             weight = 1,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[2.696597, 104.218442],[0.543961, 103.919291]],
                             popup = 'rute sama',
                             color = 'White',
                             weight = 1,
                             opacity=1).add_to(my_map)
folium.PolyLine(locations = [[0.543961, 103.919291],[0.761225, 105.547874]],
                             popup = 'rute sama',
                             color = 'White',
                             weight = 1,
                             opacity=1).add_to(my_map)



# Adding Custom Markers dengan iterating city, lat,lng
for lat, lon, death, posisi, alive, sumber, cause, tgl in zip(df['lat'], df['lon'], 
                                                  df['jumlah_meninggal'], df['posisi_karam'],
                                                  df['jumlah_selamat'], df['sumber'],
                                                  df['penyebab'], df['tanggal']):
    folium.CircleMarker(location=[lat,lon],
                  weight=1,
                  radius=death*0.3,
                  popup=folium.Popup("<h5><b>Selat Malaka<br>"+
                                     posisi+"<br></b>"+
                                     tgl+"<br></b>"+
                                     "<br></b>"+
                                     "Sebanyak </b>"+"<b>"+str(death)+"</b>"+
                                     " orang meninggal dunia dan "+"<b>"+str(alive)+"</b>"+" orang selamat, "+
                                     "sementara penyebab kecelakaan "+str(cause)+".<br>"+
                                     "<br></b>"+
                                     "sumber :&nbsp"+sumber,
                                     max_width=len(f"name= {posisi}")*10),
                  color='crimson', 
                  fill=True).add_to(my_map)

    
st_folium(my_map, width=1000, height=400)
