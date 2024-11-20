import streamlit as st

# Set the title of the app
st.title("Science Support Platform (SSP) Submission Portal")

# Introduction
st.write("""
Welcome to the SSP Submission Portal. This application allows you to submit your research samples, schedule experiments, 
and select the appropriate analytical techniques. Please follow the guidelines provided in each section.
""")

# Agreement Section
st.header("Guidelines Agreement")
agreed_guidelines = st.checkbox(
    "I have read and agree to the SSP guidelines, including data handling, authorship, and project responsibilities."
)
if not agreed_guidelines:
    st.warning("You must agree to the guidelines before submitting samples or scheduling experiments.")

# Responsible Person Confirmation
responsible_person = st.text_input(
    "Responsible Person for Analysis and Scheduling (Full Name)",
    placeholder="Enter the name of the SSP staff responsible for your project"
)
agreement_confirmation = st.checkbox(
    "I confirm that the responsible person has agreed to oversee this project."
)
if not agreement_confirmation:
    st.warning("You must confirm the agreement of the responsible person before proceeding.")

# Proceed Only if Agreements Are Confirmed
if agreed_guidelines and agreement_confirmation:
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
        Follow the SSP guidelines for GC-MS, including proper extraction methods and submission protocols.
        """)
    elif technique == "LC-MS":
        st.subheader("Liquid Chromatography-Mass Spectrometry (LC-MS)")
        st.write("""
        Follow the SSP guidelines for LC-MS, ensuring proper sample preparation and labeling.
        """)
    elif technique == "Proteomics":
        st.subheader("Proteomics")
        st.write("""
        Ensure proper extraction and documentation as per SSP's guidelines for proteomic studies.
        """)
    elif technique == "Bioinformatics":
        st.subheader("Bioinformatics Support")
        st.write("""
        Engage early with SSP bioinformaticians and follow data management best practices.
        """)

# Footer Information
st.write("""
For further assistance, please contact Nicole van Dam at [vandam@igzev.de](mailto:vandam@igzev.de).
""")

# Run the app with: streamlit run app.py
