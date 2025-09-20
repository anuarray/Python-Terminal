import streamlit as st
import os
from terminal_core import ai_interpreter, commands, system_monitor  # import your modules

st.title("PyTerminal Emulator")

# Input command
user_input = st.text_input("Enter a command:")

if user_input:
    # Example: run command using your existing interpreter
    try:
        output = ai_interpreter.execute(user_input)  # modify to match your function
    except Exception as e:
        output = str(e)
    
    st.text_area("Output", output, height=300)
