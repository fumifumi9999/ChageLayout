import streamlit as st
from streamlit_sortables import sort_items

st.subheader('リストのソート')
original_items = list('ABCDEFG')
sorted_items  = sort_items(original_items)
 
st.write('---')
st.write(f'並び変え前: {original_items}')
st.write(f'並び変え後: {sorted_items}')
st.write('---')