import streamlit as st
import pandas as pd
import pickle
import requests
import time

API_KEY = '8c90279b967022da556bc289a782b7b7'

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/' + str(movie_id) + f"?api_key={API_KEY}&language=en-US")
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']


def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]

    dist = similarity[idx]

    movies_list = sorted(list(enumerate(dist)),
                         reverse=True, key=lambda x: x[1])[0:6]
    mov, cast, dir, gen, idx = [], [], [], [], []
    for i in movies_list:
        mov.append(movies.iloc[i[0]].title)
        cast.append(movies.iloc[i[0]].cast)
        dir.append(movies.iloc[i[0]].director)
        gen.append(movies.iloc[i[0]].genres)
        idx.append(movies.iloc[i[0]].id)
    return mov, cast, dir, gen, idx


st.title('Movie Recommender')

selected_movie_name = st.selectbox('Which movie?', movies['title'].values)
if st.button('Recommend'):
    mov, cast, dir, gen, idx = recommend(selected_movie_name)

    c1, c2, c3 = st.columns([4, 7, 2])
    with c1:
        st.write("")
    with c2:
        st.header(selected_movie_name)
        st.image(fetch_poster(int(idx[0])), width=150)
        st.write("Cast: " + ", ".join(cast[0]))
        st.write("Director: " + ", ".join(dir[0]))
        st.write("Genres: " + ", ".join(gen[0]))
    with c3:
        st.write("")
    
    st.write("\n"*5)
    st.header("You might also like...")
    st.write("\n"*2)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(mov[1])
        st.image(fetch_poster(int(idx[1])))
        st.write("Cast: " + ", ".join(cast[0]))
        st.write("Director: " + ", ".join(dir[0]))
        st.write("Genres: " + ", ".join(gen[0]))
    with col2:
        st.write(mov[2])
        st.image(fetch_poster(int(idx[2])))
        st.write("Cast: " + ", ".join(cast[1]))
        st.write("Director: " + ", ".join(dir[1]))
        st.write("Genres: " + ", ".join(gen[1]))
    with col3:
        st.write(mov[3])
        st.image(fetch_poster(int(idx[3])))
        st.write("Cast: " + ", ".join(cast[2]))
        st.write("Director: " + ", ".join(dir[2]))
        st.write("Genres: " + ", ".join(gen[2]))
    with col4:
        st.write(mov[4])
        st.image(fetch_poster(int(idx[4])))
        st.write("Cast: " + ", ".join(cast[3]))
        st.write("Director: " + ", ".join(dir[3]))
        st.write("Genres: " + ", ".join(gen[3]))
    with col5:
        st.write(mov[5])
        st.image(fetch_poster(int(idx[5])))
        st.write("Cast: " + ", ".join(cast[4]))
        st.write("Director: " + ", ".join(dir[4]))
        st.write("Genres: " + ", ".join(gen[4]))
