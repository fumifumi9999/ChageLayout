import streamlit as st
from streamlit_sortables import sort_items

st.subheader('メンバー表作成')
original_items = [
    {'header': '選抜メンバー1：', 'items' : ['森田']},
    {'header': '選抜メンバー2：', 'items' : ['花田']},
    {'header': '選抜メンバー3：', 'items' : ['稲田']},
    {'header': '候補メンバー：',
        'items': ['田原', '鈴木', '田中', '森', '林', '伊藤', '阿部', '田口', '木村']}
]
sorted_items = sort_items(original_items, multi_containers=True, direction='vertical')
st.write('---')
for container in sorted_items:
    st.write(container["header"])
    for member in container["items"]:
       st.write(member)