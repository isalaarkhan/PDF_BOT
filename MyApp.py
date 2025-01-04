# importing necessary libraries
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
import fitz  # PyMuPDF

import time
import tempfile


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

#----
# Get API key from environment variable for security reasons
api_key = os.getenv("GEMINI_API_KEY")
#GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', GEMINI_API_KEY)
#print(f"The API key is: {api_key}")

# Configure the Generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
# Retrieve the Gemini API key from environment variables


# Set page configuration
st.set_page_config(page_title=" PDF Genie✨ ", page_icon="books")

# App title and description
st.title(" PDF Genie✨")

# Displaying an image from a folder
img=Image.open('pdfimage.png')
st.image(img,  use_column_width=True)


 # Sidebar PDF Actions selection
st.sidebar.header("Welcome!")
#st.sidebar.subheader("Please select an option from the dropdown below:")

# Add a dropdown menu
pdfAction_options = ["📄 PDF SUMMARY", "📝 SUMMARIZE in BULLETS", "🔊 PDF AUDIO", "📝 Title and Heading Generation"]
selected_option = st.sidebar.selectbox("Please select an option from the dropdown below:",pdfAction_options)

#model configuration
#model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#generation_config = GenerationConfig(temperature=0.1, max_output_tokens=256)
##______________________________________________
 # Session state for storing responses
if 'response_text' not in st.session_state:
     st.session_state['response_text'] = ""
uploaded_file = st.file_uploader("📂 Upload your document", type=["pdf"])
 
# PDF SUMMARY
if selected_option == "📄 PDF SUMMARY":
  st.write("### 📄 PDF SUMMARY")
    # reading document
 # upload document
  #uploaded_file = st.file_uploader("📂 Upload your document", type=["pdf"])

  if uploaded_file is not None:
      doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # extracting text from document
      text_content = "".join([page.get_text() for page in doc])
        # enter prompt
      prompt = f""" Provide a very short summary, no more than three to six sentences for {text_content}
        Summary:
        """
        # model loading and generating 
      response = model.generate_content([text_content, prompt])
      st.session_state['response_text'] = response.text

  st.write(st.session_state['response_text'])
##Bullet Sumarization  
elif selected_option == "📝 SUMMARIZE in BULLETS":
    st.write("### 📝 SUMMARIZE in BULLETS")
    # reading document
 # upload document
    #uploaded_file = st.file_uploader("📂 Upload your document", type=["pdf"])

    if uploaded_file is not None:
       doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # extracting text from document
       text_content = "".join([page.get_text() for page in doc])
        # enter prompt
       prompt = f""" Provide a very short summary in four bullet points for {text_content}
        
        """
        # model loading and generating 
       response = model.generate_content([text_content, prompt])
       st.session_state['response_text'] = response.text

    st.write(st.session_state['response_text'])

##Title and Heading
elif selected_option == "📝 Title and Heading Generation":
    st.write("### 📝 Title and Heading Generation")
    # reading document
 # upload document
    #uploaded_file = st.file_uploader("📂 Upload your document", type=["pdf"])

    if uploaded_file is not None:
       doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # extracting text from document
       text_content = "".join([page.get_text() for page in doc])
        # enter prompt
       prompt = f""" Write a title for this text, give me five options: for {text_content}
        
        """
        # model loading and generating 
       response = model.generate_content([text_content, prompt])
       st.session_state['response_text'] = response.text

    st.write(st.session_state['response_text'])

      # Create a download button
st.download_button(
label="Download Text",
data=st.session_state['response_text'],
file_name="generated_text.txt",
mime="text/plain"
) 
   
st.sidebar.subheader('Created by Dr. Saima Hassan')

# Adding links to social accounts
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/drsaima-hassan)")
st.sidebar.markdown("[Reseachgate](https://www.researchgate.net/profile/Saima_Hassan)")


#             prompt,
#             generation_config=genai.types.GenerationConfig(
#                 candidate_count=1,
#                 stop_sequences=["x"],
#                 max_output_tokens=max_output_tokens,
#                 temperature=tempt,
#             ),
#         )
#         st.session_state['response_text'] = response.text

#     st.write(st.session_state['response_text'])
#     # Create a download button
#     st.download_button(
#         label="Download Text",
#         data=st.session_state['response_text'] ,
#         file_name="generated_text.txt",
#         mime="text/plain"
#     )
     
 


    # st.write("### ✏️ Text to Text")
    # # configurations
    # tempt = st.sidebar.slider("🔥 Temperature:", min_value=0.0, max_value=1.0, value=0.5)
    # max_output_tokens = st.sidebar.slider("📏 Max Output Tokens:", min_value=50, max_value=1000, value=100)
    # prompt = st.text_input("🗣️ Enter your prompt:")
    #  # generating text
    # if prompt:
    #     model = genai.GenerativeModel("gemini-1.5-flash")
    #     response = model.generate_content(
    #         prompt,
    #         generation_config=genai.types.GenerationConfig(
    #             candidate_count=1,
    #             stop_sequences=["x"],
    #             max_output_tokens=max_output_tokens,
    #             temperature=tempt,
    #         ),
    #     )
    #     st.session_state['response_text'] = response.text

    # st.write(st.session_state['response_text'])
    # # Create a download button
    # st.download_button(
    #     label="Download Text",
    #     data=st.session_state['response_text'] ,
    #     file_name="generated_text.txt",
    #     mime="text/plain"
    # )

# # Document Processing
# elif selected_option == "📄 Document Processing":
#     st.write("### 📚 Document Processing")
#     # upload document
#     uploaded_file = st.file_uploader("📂 Upload your document", type=["pdf"])

#     if uploaded_file is not None:
#         # reading document
#         doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#         # extracting text from document
#         text_content = "".join([page.get_text() for page in doc])
#         # enter prompt
#         prompt = st.text_input("🗣️ Enter your prompt:")
#         # model loading and generating 
#         model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#         response = model.generate_content([text_content, prompt])
#         st.session_state['response_text'] = response.text

#     st.write(st.session_state['response_text'])
#       # Create a download button
#     st.download_button(
#     label="Download Text",
#     data=st.session_state['response_text'],
#     file_name="generated_text.txt",
#     mime="text/plain"
# )
# # Image to Text
# elif selected_option == "🖼️ Image to Text":
#     st.write("### 🖼️ Image to Text")
#     # uploading file
#     uploaded_image = st.file_uploader("📷 Upload your image", type=["png", "jpeg", "webp", "heic", "heif"])

#     if uploaded_image is not None:
#         # opening image
#         image = Image.open(uploaded_image)
#         prompt = st.text_input("🗣️ Enter your prompt:")
#         # using model 
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content([prompt, image])
#         st.session_state['response_text'] = response.text

#     st.write(st.session_state['response_text'])
#       # Create a download button
#     st.download_button(
#     label="Download Text",
#     data=st.session_state['response_text'],
#     file_name="generated_text.txt",
#     mime="text/plain"
# )
# # Audio to Text
# elif selected_option == "🔊 Audio to Text":
#     st.write("### 🎧 Audio to Text")
#     uploaded_audio = st.file_uploader("🎵 Upload your audio", type=["mp3", "wav", "aac", "aiff", "x-flv", "ogg", "flac"])

#     if uploaded_audio is not None:
#         # Get the file extension from the uploaded audio file
#         file_extension = os.path.splitext(uploaded_audio.name)[1]
        
#         # making temporary file to store audio
#         with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_audio_file:
#             # reading file
#             temp_audio_file.write(uploaded_audio.read())
#             temp_audio_path = temp_audio_file.name
        
#         # passing file path to genai library
#         audio_file = genai.upload_file(path=temp_audio_path)
#         model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#         prompt = st.text_input("🗣️ Enter your prompt:")
#         response = model.generate_content([prompt, audio_file])
#         st.session_state['response_text'] = response.text
        
#         # removing temporary file after processing
#         os.remove(temp_audio_path)

#     st.write(st.session_state.get('response_text', ''))
#       # Create a download button
#     st.download_button(
#     label="Download Text",
#     data=st.session_state['response_text'],
#     file_name="generated_text.txt",
#     mime="text/plain"
# )

# # Code Generation
# elif selected_option == "💻 Code Generation":
#     st.write("### 💻 Code Generation")
#     prompt = st.text_input("📝 Enter your code generation prompt:")

#     if prompt:
#         # generating by loading model
#         model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools="code_execution")
#         response = model.generate_content(prompt)
#         st.session_state['response_text'] = response.text

#     st.write(st.session_state['response_text'])
#       # Create a download button
#     st.download_button(
#     label="Download Text",
#     data=st.session_state['response_text'],
#     file_name="generated_text.txt",
#     mime="text/plain"
# )
# # Footer with name
# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown("### Created by **Najma Razzaq** 💻")
