
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import requests

movie_dict = pickle.load(open(r'C:\Users\deeks\source\repos\PythonApplication1\PythonApplication1\movies_dict.pkl','rb'))
similarity = pickle.load(open(r'C:\Users\deeks\source\repos\PythonApplication1\PythonApplication1\similarity.pkl','rb'))

movies = pd.DataFrame(movie_dict)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f9f811e1333ef2592605bf661d6aa038&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies = []
    recommend_movies_poster = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster


st.title("Movie Recommendation System") 

selected_movie_name =st.selectbox(
    'How would you like to be connected ?',
    movies['title'].values)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])





