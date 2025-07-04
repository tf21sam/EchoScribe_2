import streamlit as st
import requests

st.set_page_config(page_title="EchoScribe", layout="centered")
st.title("🎙️ EchoScribe — Talk with YouTube/Audio")

# YouTube URL submission
with st.form("youtube_form"):
    youtube_url = st.text_input("Enter YouTube URL:")
    submitted = st.form_submit_button("Process")

if submitted and youtube_url:
    with st.spinner("Processing audio and generating transcript..."):
        response = requests.post("http://localhost:8000/process/", data={"youtube_url": youtube_url})
        if response.status_code == 200:
            st.success("Done! You can now ask questions below.")
        else:
            st.error("Failed to process the video.")

# QA section
st.markdown("---")
st.subheader("Ask a question about the video")

question = st.text_input("Your question")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            query_response = requests.post("http://localhost:8000/query/", json={"question": question})
            if query_response.status_code == 200:
                answer = query_response.json().get("answer", "")
                if answer:
                    st.success("Answer:")
                    st.write(answer)
                else:
                    st.warning("No answer returned from backend.")
            else:
                st.error("Failed to get answer.")
