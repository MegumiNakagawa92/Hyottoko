import streamlit as st
import numpy as np
import time

st.title("ひょっとこクイズ")

if st.button("今日のひょっとこはどっち向き？"):
  
  options = ["左","右"]
  luck = np.random.choice(options, 1, p=[0.99,0.01])[0]

  if luck=="左":
    image = "left.png"
  elif luck=="右":
    image = "right.png"
  
  st.image("front.png", caption=f"　↓↓↓今日のひょっとこは・・・？　右かなー？　左かなーー？？↓↓↓", use_column_width=True)
  time.sleep(3)

  st.write(luck)
  st.image(image, use_column_width=True)

  if st.button("リセット"):
    placeholder = st.empty()
    placeholder.empty()