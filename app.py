import streamlit as st

# Set the title of the app
st.title("Science Support Platform (SSP) Submission Portal")

# Enable test mode
test_mode = st.sidebar.checkbox("Enable Test Mode (For Testing Only)")

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

st.header("Approval Mechanisms")
approval_mechanism = st.radio(
    "Select the mechanism for approval by the responsible person:",
    ["Email Confirmation", "Approval Code", "Manual Confirmation"]
)

approval_granted = False  # Default state

# Mechanism 1: Email Confirmation
if approval_mechanism == "Email Confirmation":
    st.write("""
    An email will be sent to the responsible person for approval. The process will only proceed after confirmation.
    """)
    email = st.text_input("Responsible Person's Email", placeholder="Enter the email address")
    send_email = st.button("Send Approval Request")

    if send_email:
        # Simulated email sending process
        st.success(f"Approval request sent to {email}. Please wait for confirmation.")
    
    # Cheat Code for Testing
    if test_mode:
        approval_granted = st.checkbox("Simulate Approval (Cheat Code for Testing)")

# Mechanism 2: Approval Code
elif approval_mechanism == "Approval Code":
    st.write("""
    The responsible person will provide you with an approval code to proceed.
    """)
    approval_code_input = st.text_input("Enter Approval Code", type="password")
    valid_approval_code = "SSP2024"  # Example code; replace with a real system
    if approval_code_input == valid_approval_code:
        st.success("Approval granted!")
        approval_granted = True
    elif approval_code_input:
        st.error("Invalid approval code. Please try again.")

    # Cheat Code for Testing
    if test_mode:
        if st.button("Use Cheat Code for Approval"):
            st.success("Cheat Code Activated: Approval granted!")
            approval_granted = True

# Mechanism 3: Manual Confirmation
elif approval_mechanism == "Manual Confirmation":
    st.write("""
    The responsible person must log in and approve this request manually.
    """)
    responsible_login = st.text_input("Responsible Person's Username", placeholder="Enter username")
    responsible_password = st.text_input("Responsible Person's Password", type="password")
    valid_username = "responsible_user"  # Example credentials
    valid_password = "securepassword"
    if responsible_login == valid_username and responsible_password == valid_password:
        st.success("Approval granted!")
        approval_granted = True
    elif responsible_login or responsible_password:
        st.error("Invalid credentials. Please try again.")

    # Cheat Code for Testing
    if test_mode:
        if st.button("Activate Cheat Code for Manual Login"):
            st.success("Cheat Code Activated: Approval granted!")
            approval_granted = True

# Proceed Only if Approval is Granted
if approval_granted:
    st.success("Approval confirmed! You may now proceed.")

    # Category Selection
    st.header("Select Analysis Category")
    category = st.selectbox("Choose a category", ["LC-MS", "GC-MS", "Proteomics", "Bioinformatics", "Data Management"])

    # Guidelines and Forms Section
    st.header("Guidelines and Forms")
    st.write("Please review the guidelines and forms for your selected category before proceeding.")

    if category == "LC-MS":
        with st.expander("LC-MS Guidelines and Forms"):
            st.write("""
            **Guidelines:**
            - [LC-MS General Guidelines](/path/to/lcms_guidelines.pdf)
            - [Sample Preparation for LC-MS](/path/to/lcms_sample_prep.pdf)
            - [Data Submission Guidelines](/path/to/lcms_data_submission.pdf)

            **Forms:**
            - [LC-MS Sample Submission Form](/path/to/lcms_sample_form.pdf)
            - [LC-MS Experiment Request Form](/path/to/lcms_experiment_form.pdf)
            """)
    elif category == "GC-MS":
        with st.expander("GC-MS Guidelines and Forms"):
            st.write("""
            **Guidelines:**
            - [GC-MS General Guidelines](/path/to/gcms_guidelines.pdf)
            - [Sample Preparation for GC-MS](/path/to/gcms_sample_prep.pdf)
            - [Data Submission Guidelines](/path/to/gcms_data_submission.pdf)

            **Forms:**
            - [GC-MS Sample Submission Form](/path/to/gcms_sample_form.pdf)
            - [GC-MS Experiment Request Form](/path/to/gcms_experiment_form.pdf)
            """)
    elif category == "Proteomics":
        with st.expander("Proteomics Guidelines and Forms"):
            st.write("""
            **Guidelines:**
            - [Proteomics General Guidelines](/path/to/proteomics_guidelines.pdf)
            - [Sample Preparation for Proteomics](/path/to/proteomics_sample_prep.pdf)
            - [Data Submission Guidelines](/path/to/proteomics_data_submission.pdf)

            **Forms:**
            - [Proteomics Sample Submission Form](/path/to/proteomics_sample_form.pdf)
            - [Proteomics Experiment Request Form](/path/to/proteomics_experiment_form.pdf)
            """)
    elif category == "Bioinformatics":
        with st.expander("Bioinformatics Guidelines and Forms"):
            st.write("""
            **Guidelines:**
            - [Bioinformatics General Guidelines](/path/to/bioinformatics_guidelines.pdf)
            - [Data Submission Guidelines](/path/to/bioinformatics_data_submission.pdf)

            **Forms:**
            - [Bioinformatics Analysis Request Form](/path/to/bioinformatics_request_form.pdf)
            """)
    elif category == "Data Management":
        with st.expander("Data Management Guidelines and Forms"):
            st.write("""
            **Guidelines:**
            - [Data Management General Guidelines](/path/to/data_management_guidelines.pdf)
            - [Data Storage and Sharing Guidelines](/path/to/data_storage_guidelines.pdf)

            **Forms:**
            - [Data Management Plan Template](/path/to/data_management_plan_template.docx)
            - [Data Sharing Agreement Form](/path/to/data_sharing_agreement.pdf)
            """)

    # Common Fields for All Categories
    st.header("General Information")
    with st.form(key='general_info_form'):
        collaborator_name = st.text_input("Collaborator Name", placeholder="Enter your name")
        affiliation = st.text_input("Affiliation", placeholder="Enter your affiliation")
        email_address = st.text_input("Email Address", placeholder="Enter your email address")
        project_name = st.text_input("Project Name", placeholder="Enter the project name")
        project_abstract = st.text_area("Project Abstract", placeholder="Provide a brief abstract of the project")
        hypothesis = st.text_area("Hypothesis", placeholder="State your hypothesis")
        funded_project = st.radio("Is this part of a funded project?", ["Yes", "No"])
        if funded_project == "Yes":
            funded_project_name = st.text_input("Name of Funded Project", placeholder="Enter the name of the funded project")
            responsible_person_project = st.text_input("Responsible Person for Project", placeholder="Enter the name of the responsible person")
            responsible_institute_project = st.text_input("Institute for Project", placeholder="Enter the name of the institute")
        type_of_collaboration = st.multiselect("Type of Collaboration", ["Consultant", "Experiment Design", "Analysis"])
        if "Analysis" in type_of_collaboration:
            analysis_type = st.text_input("Type of Analysis", placeholder="Enter the type of analysis")
            scientific_name_organism = st.text_input("Scientific Name of Organism", placeholder="Enter the scientific name of the organism")
            tissue = st.text_input("Tissue", placeholder="Enter the tissue type")
            number_of_samples = st.number_input("Number of Samples", min_value=1)
            biosafety_level = st.selectbox("Biosafety Level", ["S1", "S2", "S3"])
            state_of_sample = st.selectbox("State of Sample", ["Fresh", "Dried", "Freeze-dried", "Extract"])
            additional_details = st.text_area("Additional Details", placeholder="Provide any additional details")
            number_of_treatments = st.number_input("Number of Treatments", min_value=1)
            number_of_biological_replicates = st.number_input("Number of Biological Replicates", min_value=1)
        trial_test = st.radio("Do you need a trial test on a few samples?", ["Yes", "No"])
        if trial_test == "Yes":
            optimized_protocols = st.radio("Are there optimized protocols for the analysis?", ["Yes", "No"])
            if optimized_protocols == "Yes":
                protocol_details = st.text_area("Details about the optimized protocol", placeholder="Provide details about the optimized protocol")
            else:
                protocol_setup = st.radio("Does it need a new protocol setup or is there a standard protocol?", ["New Protocol Setup", "Standard Protocol"])
        training_needed = st.radio("Do you need training?", ["Yes", "No"])
        if training_needed == "Yes":
            training_level = st.selectbox("Training Level", ["Basic", "Intermediate", "Professional", "Hands-on"])
        submit_general_info = st.form_submit_button("Submit General Information")

    # Calendar for Booking Consultation
    st.header("Book Consultation")
    st.write("Please select a date and time for your consultation with the respective specialist.")
    consultation_date = st.date_input("Consultation Date")
    consultation_time = st.time_input("Consultation Time")
    book_consultation = st.button("Book Consultation")
    if book_consultation:
        st.success(f"Consultation booked successfully for {consultation_date} at {consultation_time}!")

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

else:
    st.warning("Approval is required to proceed with submission and scheduling.")
