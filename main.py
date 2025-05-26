import os
import vertexai
import streamlit as st
from vertexai.preview.generative_models import GenerativeModel

from dotenv import load_dotenv
load_dotenv()

# Get environment variables
project_id = os.getenv("project_id")
project_region = os.getenv("region")

try:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=project_region)

    # Use the correct model name
    model = GenerativeModel("gemini-2.0-flash-001")

    def user_interfaces():
        # Set up Streamlit page
        st.set_page_config(page_title="Gemini")
        st.header("Gemini")

        # Get user input
        user_question = st.text_input("Ask me anything")

        if user_question:
            try:
                # Generate response using Gemini model
                response = model.generate_content(user_question, stream=True)

                # Display response
                for res in response:
                    st.write(res.text)
            except Exception as e:
                st.error(f"Error generating response: {e}")

    if __name__ == "__main__":
        user_interfaces()
except Exception as e:
    print(f"Error initializing Vertex AI: {e}")