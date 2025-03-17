import streamlit as st
from openai import OpenAI
f = open("D:\Learnbay\Gen AI\Prompt Engineering\Keys\OpenAI_API _Key_Proj_1.txt")
key =f.read()
model = OpenAI(api_key = key)
st.title("---:)Achyuth AI Chatbot")
st.chat_message("Assistant").write("Hi, How may I help you?")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.chat_message(msg['role']).write(msg['content'])    

user_input = st.chat_input()
if user_input:
    st.chat_message("user").write(user_input)
    response = model.chat.completions.create(model = "gpt-3.5-turbo",
                                            messages = [{"role":"system",
                                                         "content":"""you are known to be polite and 
                                                         helpful AI Bot. Act as helping guide for general knowledge
                                                         questions. Your job is to help those who ask you general question or 
                                                         current affairs. If the doubt is not relavant to general knowledge,
                                                         you can politely ask for another question."""}] + st.session_state["messages"]+[{"role":"user",
                                                                                                                                          "content":user_input}])
    st.chat_message("assistant").write(response.choices[0].message.content) 
    st.session_state["messages"].append({"role":"user","content":user_input})
    st.session_state["messages"].append({"role":"assistant","content":response.choices[0].message.content})  