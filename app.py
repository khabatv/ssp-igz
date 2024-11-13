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
    
    # Metadata attributes
    species = st.text_input("Species", placeholder="Enter species (e.g., human, plant)")
    institute = st.text_input("Institute/Organization", placeholder="Enter your institute or organization")
    location = st.text_input("Location of Sample", placeholder="Enter location (e.g., city, country)")
    biosafety_level = st.selectbox("Biosafety Level", ["1", "2", "3", "4"])
    
    # Extraction Method Selection
    extraction_method = st.selectbox(
        "Extraction Method",
        [
            "None",
            "Liquid-Liquid Extraction",
            "Solid Phase Extraction (SPE)",
            "Solid Phase Micro Extraction (SPME)",
            "Stir Bar Sorptive Extraction (SBSE)",
            "Accelerated Solvent Extraction (ASE)"
        ]
    )
    
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
Choose the analytical technique you would like to use for your samples. Each technique has specific guidelines.
""")

technique = st.selectbox("Select Technique", ["GC-MS", "LC-MS", "Proteomics", "Bioinformatics"])

if technique == "GC-MS":
    st.subheader("Gas Chromatography-Mass Spectrometry (GC-MS)")
    st.write("""
    GC-MS is widely used in metabolomics for analyzing volatile and semi-volatile compounds.

    **Extraction Methods**:
    - **Liquid-Liquid Extraction**: Commonly used for extracting compounds from biological matrices.
    - **Solid Phase Extraction (SPE)**: Useful for isolating analytes from complex mixtures.
    - **Solid Phase Micro Extraction (SPME)**: A solvent-free method ideal for volatile compounds.
    
    **Sample Preparation**:
    - Derivatization is often required to make non-volatile compounds volatile enough for analysis.

    **Submission Protocol**:
    - Submit samples in appropriate vials with clear labeling.
    
    **Data Handling**:
    - Raw data will include mass spectra and chromatograms. Ensure proper storage and backup of raw data files.

    **Instruments Used**:
    - High-resolution mass spectrometers such as those from ThermoFisher are commonly used in GC-MS analysis.
    """)

elif technique == "LC-MS":
    st.subheader("Liquid Chromatography-Mass Spectrometry (LC-MS)")
    st.write("""
    LC-MS combines liquid chromatography with mass spectrometry, frequently used in metabolomics.

    **Extraction Methods**:
    - **Liquid-Liquid Extraction**: Effective for separating analytes based on solubility.
    - **Solid Phase Extraction (SPE)**: Useful for cleanup and concentration of samples prior to analysis.

    **Sample Preparation**:
    - Ensure proper extraction and cleanup protocols are followed.

    **Submission Protocol**:
    - Samples should be submitted in appropriate containers with detailed information on extraction methods.

    **Data Handling**:
    - Data reports will include identified metabolites with m/z values, retention times, and peak intensities.

    **Instruments Used**:
    - The Orbitrap Exploris 240 is an example of a high-resolution mass spectrometer used in LC-MS applications.
    """)

elif technique == "Proteomics":
    st.subheader("Proteomics")
    st.write("""
   Proteomics involves the large-scale study of proteins and is essential in understanding biological processes.

   **Extraction Methods**:
   - **Liquid-Liquid Extraction**: Commonly used for protein extraction from biological samples.
   - **Precipitation Methods**: Such as acetone or trichloroacetic acid precipitation to concentrate proteins.

   **Sample Preparation**:
   - Proper protein extraction protocols must be followed to maintain sample integrity.

   **Submission Protocol**:
   - Clearly label all protein samples and provide detailed information about the extraction methods used.

   **Data Handling**:
   - Data will include protein identification and quantification results, which should be securely stored.

   **Instruments Used**:
   - Mass spectrometers such as Q-TOF or Orbitrap systems are commonly utilized in proteomic studies.
   """)

elif technique == "Bioinformatics":
   st.subheader("Bioinformatics Support")
   st.write("""
   Bioinformatics is crucial for analyzing complex biological data generated from metabolomics and proteomics studies. 
   
   **Data Analysis**:
   - Engage with bioinformaticians early in your project to discuss data management strategies.

   **Tools Available**:
   - Various software tools are available for metabolomic and proteomic data analysis; workshops may be offered by SSP.

   **Data Management**:
   - Ensure proper documentation of all analyses performed and maintain backups of processed data.
   """)

# Data Handling Guidelines Section
st.header("Data Handling and Documentation")
st.write("""
After analysis completion, you will receive a report detailing identified metabolites or proteins. Ensure that raw 
data files are securely stored and backed up regularly.
""")

# Footer Information
st.write("""
For further assistance, please contact Nicole van Dam at [vandam@igzev.de](mailto:vandam@igzev.de).
""")

# Run the app with: streamlit run app.py
