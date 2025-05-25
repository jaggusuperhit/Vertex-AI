import vertexai
import streamlit as st
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig
import google.auth

# Initialize Vertex AI
try:
    credentials, project = google.auth.default()
    vertexai.init(
        project=project or "vertex-ai-459208",
        location="us-central1",
        credentials=credentials
    )
except Exception as e:
    st.error(f"Authentication failed: {str(e)}")
    st.error("Please ensure you've run:")
    st.code("gcloud auth application-default login")
    st.stop()

# Use the correct model name
MODEL_NAME = "gemini-1.0-pro"  # Updated to use the correct available model

def main():
    st.set_page_config(page_title="Gemini Chat")
    st.title(f"Gemini Chat ({MODEL_NAME})")
    
    if prompt := st.chat_input("Ask me anything"):
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            try:
                model = GenerativeModel(MODEL_NAME)
                response = model.generate_content(
                    prompt,
                    generation_config=GenerationConfig(
                        temperature=0.7,
                        max_output_tokens=2048,
                        top_p=0.8,
                        top_k=40
                    ),
                    stream=True
                )
                
                response_text = st.empty()
                full_response = ""
                for chunk in response:
                    full_response += chunk.text
                    response_text.markdown(full_response + "▌")
                
                response_text.markdown(full_response)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()