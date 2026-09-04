import streamlit as st
import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("❌ Gemini API key not found. Please set GEMINI_API_KEY in environment variables or Streamlit secrets.")
else:
    genai.configure(api_key=API_KEY)

# Use supported Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

st.set_page_config(page_title="AI Content Assistant", page_icon="✨", layout="centered")
st.title("✨ AI Content Assistant")
st.write("Generate complete posts with captions and hashtags using Gemini AI.")

content_type = st.selectbox("Select Content Type", ["Post", "Article", "Tweet", "LinkedIn Update"])
platform = st.selectbox("Select Platform", ["Instagram", "Twitter", "LinkedIn", "Facebook"])
topic = st.text_input("Enter Topic", "AI in Education")
audience = st.text_input("Target Audience", "Students, Teachers, Tech Enthusiasts")
tone = st.selectbox("Select Tone", ["Professional", "Casual", "Inspirational", "Humorous"])

if st.button("Generate Content"):
    with st.spinner("Generating content..."):
        prompt = f"""
        You are an expert social media content creator.
        Create a {content_type} for {platform}.
        Topic: {topic}
        Target Audience: {audience}
        Tone: {tone}
        
        Provide:
        1. A complete post text
        2. A catchy caption
        3. 5-7 relevant hashtags
        """

        try:
            response = model.generate_content(prompt)
            output = response.text

            st.subheader("Generated Content")
            st.write(output)

            st.download_button(
                label="📥 Download Content",
                data=output,
                file_name="generated_content.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"❌ Error generating content: {str(e)}")
