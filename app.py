import streamlit as st

# Set the title of the app
st.title("Science Support Platform (SSP) Submission Portal")

# Introduction
st.write("""
Welcome to the SSP Submission Portal. This application allows you to submit your research samples, schedule experiments, 
and select the appropriate analytical techniques. Please follow the guidelines provided in each section.
""")

# Sample Submission Section
st.header("Sample Submission")
st.write("""
Please fill out the following form to submit your samples for analysis.
""")

# Sample Information Form
with st.form(key='sample_submission_form'):
    sample_id = st.text_input("Sample ID", placeholder="Enter a unique sample ID")
    sample_type = st.selectbox("Type of Biological Material", ["Tissue", "Cell Culture", "Blood", "Other"])
    collection_date = st.date_input("Date of Collection")
    extraction_method = st.text_input("Extraction Method", placeholder="Describe the extraction method")
    additional_notes = st.text_area("Additional Notes", placeholder="Any specific requests or notes")
    
    # Submit button for sample submission
    submit_samples = st.form_submit_button("Submit Sample")
    
    if submit_samples:
        st.success(f"Sample {sample_id} submitted successfully!")
        # Here you can add code to save this data or send it to a backend

# Scheduling Section
st.header("Experiment Scheduling")
st.write("""
To schedule an experiment, please provide your contact details and preferred dates.
""")

# Scheduling Form
with st.form(key='scheduling_form'):
    contact_name = st.text_input("Your Name", placeholder="Enter your name")
    contact_email = st.text_input("Your Email", placeholder="Enter your email")
    preferred_date = st.date_input("Preferred Date for Experiment")
    
    # Submit button for scheduling
    submit_schedule = st.form_submit_button("Schedule Experiment")
    
    if submit_schedule:
        st.success(f"Experiment scheduled successfully for {contact_name} on {preferred_date}!")
        # Here you can add code to save this data or send it to a backend

# Analytical Techniques Section
st.header("Select Analytical Technique")
st.write("""
Choose the analytical technique you would like to use for your samples.
""")

technique = st.selectbox("Select Technique", ["GC-MS", "LC-MS", "Proteomics", "Bioinformatics"])

if technique == "GC-MS":
    st.write("""
    **Gas Chromatography-Mass Spectrometry (GC-MS)**: 
    Ensure proper sample preparation and follow GC-MS protocols. Calibration of instruments is essential before analysis.
    """)
elif technique == "LC-MS":
    st.write("""
    **Liquid Chromatography-Mass Spectrometry (LC-MS)**: 
    Follow established LC-MS protocols tailored for targeted or untargeted analyses. Discuss method development with SSP staff if analyzing novel compounds.
    """)
elif technique == "Proteomics":
    st.write("""
    **Proteomics**: 
    For proteomic analyses, ensure that protein extraction protocols are meticulously followed. Consult with bioinformaticians in SSP for data interpretation related to protein identification and quantification.
    """)
elif technique == "Bioinformatics":
    st.write("""
    **Bioinformatics**: 
    Engage with bioinformaticians early in your project to discuss data management strategies and analysis plans. Attend workshops offered by SSP on bioinformatics tools relevant to metabolomic and proteomic data analysis.
    """)

# Data Handling Guidelines Section
st.header("Data Handling and Documentation")
st.write("""
After analysis completion, you will receive a report detailing identified metabolites or proteins. Ensure that raw data files are securely stored and backed up regularly.
""")

# Footer Information
st.write("""
For further assistance, please contact Nicole van Dam at [vandam@igzev.de](mailto:vandam@igzev.de).
""")

# Run the app with: streamlit run app.py
