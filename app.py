import streamlit as st
import random
st.title("Welcome To My World!😎")

if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.won = False
st.write("Please guess a number between 1 and 100")
guess = st.number_input("Please enter a number: ",
                        min_value=1, max_value=100, step=1)
if st.button("🎶Submit Your Answer🎶", disabled=st.session_state.won):
    if guess > st.session_state.target:
        st.warning("Overestimated it! stupid,🤣")
    elif guess < st.session_state.target:
        st.warning("Underestimated it! pity,😿")
    else:
        st.success("Wow! It's right! You're the smartest person in the world!")
        st.session_state.won = True
        st.balloons()
if st.button("🐾Restart🐾"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.won = False
    st.rerun()
