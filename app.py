import base64
import os
import tempfile
from dotenv import load_dotenv
import streamlit as st
import requests
from io import BytesIO
from streamlit_pdf_viewer import pdf_viewer

# ----------------------------
# Configuration
# ----------------------------
load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

# ----------------------------
# Streamlit App
# ----------------------------
st.set_page_config(layout="wide")
st.title("Unstract AI-Powered Document Classification")
st.markdown("""
Upload multiple PDFs to classify them using **Unstract**.
The app will call the API and show documents organized by type. 
""")

# Add a file uploader
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# If files are uploaded, process them
if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully!")
    
    # Process button
    if st.button("🚀 Start Document Classification", type="primary", use_container_width=True):
        st.info("Processing documents... Please wait.")
        
        # Remove duplicate files based on name
        unique_files = {}
        for pdf_file in uploaded_files:
            if pdf_file.name not in unique_files:
                unique_files[pdf_file.name] = pdf_file
            else:
                st.warning(f"Skipping duplicate file: {pdf_file.name}")
        
        # Display the number of unique files
        if len(unique_files) != len(uploaded_files):
            st.info(f"Removed {len(uploaded_files) - len(unique_files)} duplicate files. Processing {len(unique_files)} unique files.")
        
        # If there are unique files, process them
        if unique_files:

            # Initialize the dictionary to store PDFs by type
            organized_docs = {}
            
            # Prepare the API call with all files at once
            headers = {
                'Authorization': f'Bearer {API_KEY}'
            }
            payload = {'timeout': 300, 'include_metadata': False}
            
            # Create file objects for all files in a single API call
            files = []
            for pdf_file in unique_files.values():
                file_bytes = pdf_file.read()
                files.append(('files', (pdf_file.name, BytesIO(file_bytes), 'application/octet-stream')))
            
            # Call the API with all files
            response = requests.request("POST", API_URL, headers=headers, data=payload, files=files)
            
            # Check if the API call was successful
            if response.status_code == 200:
                # Get the result from the API call
                result = response.json()
                
                # Check if the execution is completed
                if result.get("message", {}).get("execution_status") == "COMPLETED":
                    # Extract results from the new response structure
                    results_list = result.get("message", {}).get("result", [])
                    
                    # Check if there are any results
                    if results_list and len(results_list) > 0:
                        
                        # Process all results
                        for file_result in results_list:
                            file_name = file_result.get("file", "Unknown")
                            pdf_file = unique_files.get(file_name)
                            
                            # Check if the file was processed successfully
                            if pdf_file and file_result.get("status") == "Success":
                                
                                # Extract classification from the successful result
                                try:
                                    doc_type = file_result.get("result", {}).get("output", {}).get("document_classification", {}).get("classification", "Unknown")
                                except (KeyError, AttributeError):
                                    doc_type = "Unknown"
                                
                                # Add the file to the organized_docs dictionary
                                if doc_type not in organized_docs:
                                    organized_docs[doc_type] = []
                                organized_docs[doc_type].append(pdf_file)
                            elif pdf_file:
                                st.error(f"File processing failed for {file_name}: {file_result.get('error', 'Unknown error')}")
                    else:
                        # If no results are found, display an error message
                        st.error("No results found in the API response")
                else:
                    # If the execution is not completed, display an error message
                    st.error(f"Execution not completed. Status: {result.get('message', {}).get('execution_status', 'Unknown')}")
                    st.json(result)

                # Display the full API response for debugging
                st.divider()
                st.subheader("API Response")
                st.json(result, expanded=False)
            else:
                # If the API call fails, display an error message
                st.error(f"Failed to classify files: {response.text}")
            
            # Display organized PDFs
            if organized_docs:

                # Display success message and divider
                st.success(f"Successfully classified {len(organized_docs)} document types")
                st.divider()
                st.subheader("Classification Results")
                
                # Create columns for better layout
                cols = st.columns(len(organized_docs), border=True)
                
                # Display each document type in a column
                for idx, (doc_type, files) in enumerate(organized_docs.items()):
                    
                    # Display the document type in a column
                    with cols[idx]:
                        st.subheader(f"{doc_type} ({len(files)} files)")
                        st.divider()
                        
                        # Display each file in the column
                        for f in files:
                            # Display the file name
                            st.markdown(f"**{f.name}**")
                            
                            # Display PDF in a container for better organization
                            with st.container():
                                
                                # Save uploaded file to a temporary file
                                temp_file = tempfile.NamedTemporaryFile(delete=False)
                                temp_file.write(f.getvalue())
                                temp_file.close()
                                
                                # Display PDF using the temporary file
                                pdf_viewer(temp_file.name, width="90%", height=500, zoom_level="auto")
                                st.divider()     
            else:
                # If no documents were successfully classified, display a warning message
                st.warning("No documents were successfully classified.")
