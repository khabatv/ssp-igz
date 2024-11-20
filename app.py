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
        # Here, integrate an email-sending function (e.g., using smtplib or an API)
        st.success(f"Approval request sent to {email}. Please wait for confirmation.")
        # Simulating approval for demonstration
        approval_granted = st.checkbox("Simulate Approval (for testing only)")

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

# Proceed Only if Approval is Granted
if approval_granted:
    st.success("Approval confirmed! You may now proceed.")

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
