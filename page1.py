import streamlit as st
import pandas as pd

st.title('我的个人网站 💡')
st.write('### 早上好！')

a = 234*9
a

[11, 22, 33]

{'tag1': '1', 'tag2': '2', 'tag3': 3}

df = pd.DataFrame({'姓名':['张三','李四','王五','贾六','赵七'],
                   '学号': ['01', '02', '03','04','05'],
              '班级':['二班','一班','二班','三班','一班'],
              '成绩':[92,67,70,88,76]})
st.dataframe(df)
st.divider()
st.table(df)