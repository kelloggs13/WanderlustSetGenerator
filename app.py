import streamlit as st
import pandas as pd

images = [
  'Aktivitaeten.jpeg', 'Freundschaft.jpeg', 'Wassersport.jpeg', 'Outdoor.jpeg',
  'Handarbeit.jpeg', 'Gruppenspiele.jpeg', 'Kochen.jpeg'
]

df_decks = pd.DataFrame({'image': images})

decks_selected = df_decks.sample(3)

if st.button('Set erstellen'):
  c1, c2, c3 = st.columns([1, 1, 1])
  with c1:
    st.image(decks_selected.iloc[0]["image"], width=200)
  with c2:
    st.image(decks_selected.iloc[1]["image"], width=200)
  with c3:
    st.image(decks_selected.iloc[2]["image"], width=200)
