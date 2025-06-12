import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="南宁美食数据",page_icon="🥘")
data={
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [15, 20, 25, 35, 50],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
}
restaurants = pd.DataFrame(data)
st.map(restaurants)
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5])
# 将新索引应用到数据框上
df.index = index
# 修改df，用列作为df的索引，替换原有的索引
df.set_index('餐厅', inplace=True)
st.subheader("餐厅评分")
st.bar_chart(df, y='评分')

jg = pd.DataFrame(data)
# 修改jg，用列作为jg的索引，替换原有的索引
jg.set_index('餐厅', inplace=True)
st.subheader("餐厅价格")
# 通过y参数筛选只显示1号门店的数据
st.line_chart(df, y=['人均消费(元)'])


data = {
    '月份':['01月', '02月', '03月','04月', '05月', '06月','07月', '08月', '09月','10月', '11月', '12月'],
    '星艺会尝不忘':[200, 150, 180,152,166,155,188,177,190,150,162,180],
    '高峰柠檬鸭':[120, 160, 123,200, 150, 180,152,166,155,188,177,190],
    '复记老友粉':[110, 100, 160,150,180,152,163,150,190,160,180,170],
    '好友缘':[120,110,120, 160, 123,200, 150, 180,152,166,155,220],
    '西冷牛排店':[110,130,150,180,190,220,260,230,280,155,160,144]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='序号')
# 将新索引应用到数据框上
df.index = index
st.header("⏱️用餐高峰时段")
st.area_chart(df, x='月份')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)


st.header('餐厅详情')
city = st.selectbox('选择餐厅查看详情：', ['星艺会尝不忘', '高峰柠檬鸭', '复记老友粉', '好友缘', '西冷牛排店'])
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if city == '星艺会尝不忘':
    st.write('评分:4.5/5')
elif city == '高峰柠檬鸭':
    st.write('评分4.7/5')
elif city == '复记老友粉':
    st.write('评分4.1/5')
elif city == '好友缘':
    st.write('评分4.7/5')
elif city == '西冷牛排店':
    st.write('评分4.7/5')



st.header("当前拥挤程度")
# 设置初始状态
my_bar = st.progress(0)
for percent in range(94):
    my_bar.progress(percent + 1, text=f'{percent}%拥挤:hourglass:')





st.image("https://ts1.tc.mm.bing.net/th/id/R-C.a02f614dae3dd46aea5e9d1e3da2f390?rik=fU0aiRnQrJ1BPQ&riu=http%3a%2f%2fs2.cdn.xiachufang.com%2f67e3bbd67dae11e58728b82a72e00100.jpg%3fimageView2%2f2%2fw%2f620%2finterlace%2f1%2fq%2f90%2fformat%2fjpg%2f.jpg&ehk=g5eVLWPccNf7NjjlDPZXI7x6WiizHTUOJMvL6WlmG0I%3d&risl=&pid=ImgRaw&r=0", caption='美味午餐等着你')