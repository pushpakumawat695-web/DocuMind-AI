
from google import genai
import streamlit as st
import os
import io
from dotenv import load_dotenv
from pypdf import PdfReader

# ==============================
# CONFIGURATION
# ==============================

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🧠",
    layout="wide"
)

# ==============================
# CUSTOM UI
# ==============================

st.markdown("""
<style>
 /* ===== DOCUMIND AI - UI THEME ===== */
 .stApp {
     background: #101827;
     color: #E5E7EB;
 }
 /* Main content */
 [data-testid="stMain"] {
     background: #101827;
 }
 [data-testid="stMainBlockContainer"] {
     max-width: 1100px;
     padding-top: 2.5rem;
     padding-bottom: 3rem;
     background: #101827;
 }
 /* Sidebar */
 [data-testid="stSidebar"] {
     background: #172235;
     border-right: 1px solid #27364D;
 }
 [data-testid="stSidebar"] > div {
     background: #172235;
 }
 [data-testid="stSidebar"] p,
 [data-testid="stSidebar"] label,
 [data-testid="stSidebar"] span {
     color: #DCE5F3;
 }
 /* Headings */
 h1, h2, h3 {
     color: #F1F5F9 !important;
 }
 /* Paragraphs */
 p, li {
     color: #CBD5E1;
 }
 /* Divider */
 hr {
     border-color: #29374C !important;
 }
 /* Buttons */
 .stButton > button {
     background: #8B7CF6;
     color: #FFFFFF;
     border: 1px solid #8B7CF6;
     border-radius: 10px;
     padding: 0.55rem 1rem;
     font-weight: 600;
     transition: all 0.2s ease;
 }
 .stButton > button:hover {
     background: #7565E8;
     border-color: #7565E8;
     color: #FFFFFF;
     transform: translateY(-1px);
 }
 /* File uploader */
 [data-testid="stFileUploader"] {
     background: #1B2638;
     border: 1px solid #334155;
     border-radius: 16px;
     padding: 12px;
 }
 [data-testid="stFileUploader"] section {
     background: #1B2638;
     border: 1px dashed #64748B;
     border-radius: 12px;
 }
 /* Chat input */
 [data-testid="stChatInput"] {
     background: #1B2638;
     border: 1px solid #334155;
     border-radius: 16px;
 }
 [data-testid="stChatInput"] textarea {
     color: #F1F5F9;
 }
 [data-testid="stChatInput"] textarea::placeholder {
     color: #94A3B8;
 }
 [data-testid="stChatInput"] > div {
     background: #1B2638;
     border-radius: 16px;
 }
 /* Chat messages */
 [data-testid="stChatMessage"] {
     background: #1B2638;
     border: 1px solid #29374C;
     border-radius: 14px;
     padding: 12px;
     margin-bottom: 12px;
 }
 /* Expanders */
 [data-testid="stExpander"] {
     background: #1B2638;
     border: 1px solid #334155;
     border-radius: 12px;
 }
 /* Alerts */
 [data-testid="stAlert"] {
     border-radius: 12px;
 }
 /* Text inputs */
 .stTextInput input,
 .stTextArea textarea {
     background: #1B2638;
     color: #F1F5F9;
     border: 1px solid #334155;
     border-radius: 10px;
 }
 /* Select boxes */
 .stSelectbox > div > div {
     background: #1B2638;
     border-radius: 10px;
 }
 /* Smooth page appearance */
 .block-container {
     transition: all 0.2s ease;
 }
 /* ===== FIX STREAMLIT EXTRA BACKGROUND AREAS ===== */
 /* Top header */
 [data-testid="stHeader"] {
     background: #101827 !important;
 }
 /* Top toolbar */
 [data-testid="stToolbar"] {
     background: #101827 !important;
 }
 /* App view container */
 [data-testid="stAppViewContainer"] {
     background: #101827 !important;
 }
 /* Bottom chat area */
 [data-testid="stBottom"] {
     background: #101827 !important;
 }
 /* Bottom chat container */
 [data-testid="stBottomBlockContainer"] {
     background: #101827 !important;
 }
 /* Chat input wrapper */
 [data-testid="stChatInputContainer"] {
     background: #101827 !important;
 }

 [data-testid="stLayoutWrapper"] summary {
    background: #263449 !important;
 }
 /* File uploader button */
 [data-testid="stFileUploader"] button {
     background: #263449 !important;
     color: #E5E7EB !important;
     border: 1px solid #475569 !important;
     border-radius: 8px !important;
 }
 /* File uploader button hover */
 [data-testid="stFileUploader"] button:hover {
     background: #334155 !important;
     border-color: #8B7CF6 !important;
 }
 /* Uploaded PDF file chip */
 [data-testid="stFileUploaderFile"] {
     background: #263449 !important;
     border: 1px solid #475569 !important;
     border-radius: 10px !important;
     color: #E5E7EB !important;
 }
 /* File name text */
 [data-testid="stFileUploaderFile"] span {
     color: #E5E7EB !important;
 }
 /* File uploader file container */
 [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"],[data-testid="stFileChip"] {
     background-color: #263449 !important;
 }
 /* ===== HOME FEATURE CARDS ===== */
 .feature-box {
     background: #1B2638;
     border: 1px solid #334155;
     border-radius: 16px;
     padding: 22px 20px;
     min-height: 150px;
     margin-bottom: 16px;
     transition: all 0.2s ease;
 }
 .feature-box:hover {
     border-color: #8B7CF6;
     background: #202D42;
 }
 .feature-box h3 {
     color: #E2E8F0 !important;
     font-size: 19px;
     margin-bottom: 10px;
 }
 .feature-box p {
     color: #94A3B8 !important;
     font-size: 14px;
     margin-bottom: 0;
 }
</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.markdown("## 🧠 DocuMind AI")

    st.caption("Your intelligent document assistant")

    st.divider()

    st.markdown("### 📚 Workspace")

    st.markdown("📄 PDF Document Assistant")
    st.markdown("💬 Document Q&A")
    st.markdown("📝 Smart Summaries")

    st.divider()

    st.caption("Powered by Gemini AI")

# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="main-title">🧠 DocuMind AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Documents. Your Answers. Your Insights.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# ==============================
# UPLOAD SECTION
# ==============================

st.markdown("## 📄 Upload Your Document")

st.markdown(
    "Upload a PDF to unlock intelligent document analysis."
)

uploaded_file = st.file_uploader(
    "Choose your PDF file",
    type=["pdf"],
    help="Upload a PDF document to get started."
)

# ==============================
# PDF PROCESSING
# ==============================

if uploaded_file:

    try:

        pdf_reader = PdfReader(
            io.BytesIO(uploaded_file.getvalue())
        )

        pdf_text = ""

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                pdf_text += page_text + "\n"

        if not pdf_text.strip():

            st.warning(
                "No readable text was found in this PDF. "
                "It may be a scanned document."
            )

        else:

            # ==============================
            # DOCUMENT INFORMATION
            # ==============================

            st.markdown("### 📄 Document Information")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("**📁 File Name**")

                st.caption(uploaded_file.name)

            with col2:

                st.markdown("**📃 Total Pages**")

                st.markdown(
                    f"### {len(pdf_reader.pages)}"
                )

            with col3:

                st.markdown("**📝 Extracted Characters**")

                st.markdown(
                    f"### {len(pdf_text):,}"
                )

            st.success("Text extracted successfully!")

            # ==============================
            # TEXT PREVIEW
            # ==============================

            with st.expander("🔍 Preview Extracted Text"):

                st.text(pdf_text[:3000])

                if len(pdf_text) > 3000:

                    st.caption(
                        "Preview limited to first 3,000 characters."
                    )

            st.divider()

            # ==============================
            # DOCUMENT SUMMARY
            # ==============================

            st.markdown("## 📝 Smart Summary")

            if st.button(
                "✨ Generate Summary",
                key="summary_button"
            ):

                with st.spinner(
                    "Generating your document summary..."
                ):

                    summary_prompt = f"""
Analyze the following document and create a structured summary.

Format your response using these sections:

## 📌 Overview
Write a short paragraph explaining what the document is about.

## 🔑 Key Points
List the most important information in clear bullet points.

## 📚 Important Details
Explain important facts, concepts, terms or details from the document.

## 🎯 Conclusion
Provide a short final takeaway from the document.

Keep the language simple, clear and easy to understand.
Use ONLY the information provided in the document.
Do not invent or assume any facts.

DOCUMENT:
{pdf_text}
"""

                    try:

                        response = client.models.generate_content(
                            model="gemini-3.5-flash",
                            contents=summary_prompt
                        )

                        st.session_state.summary = response.text

                    except Exception:

                        st.error(
                            "Unable to generate summary. "
                            "Please try again."
                        )

            if "summary" in st.session_state:

                st.markdown(
                    st.session_state.summary
                )

            st.divider()

            # ==============================
            # DOCUMENT CHAT
            # ==============================

            st.markdown("## 💬 Chat with Your Document")

            doc_id = (
                f"{uploaded_file.name}_{uploaded_file.size}"
            )

            if (
                "doc_id" not in st.session_state
                or st.session_state.doc_id != doc_id
            ):

                st.session_state.doc_id = doc_id
                st.session_state.chat_history = []

                if "summary" in st.session_state:
                    del st.session_state.summary

            # Display previous messages

            for message in st.session_state.chat_history:

                with st.chat_message(message["role"]):

                    st.markdown(message["content"])

            # User input

            user_question = st.chat_input(
                "Ask anything about your PDF..."
            )

            if user_question:

                st.session_state.chat_history.append(
                    {
                        "role": "user",
                        "content": user_question
                    }
                )

                with st.chat_message("user"):

                    st.markdown(user_question)

                conversation_context = ""

                for message in st.session_state.chat_history:

                    conversation_context += (
                        f'{message["role"]}: '
                        f'{message["content"]}\n'
                    )

                prompt = f"""
You are DocuMind AI, an intelligent document assistant.

Answer questions using ONLY the information in the document.

If the answer is not available in the document,
clearly say that the information is not found.

DOCUMENT:
{pdf_text}

CONVERSATION:
{conversation_context}

Answer the latest user question clearly.
"""

                with st.chat_message("assistant"):

                    with st.spinner(
                        "Analyzing your document..."
                    ):

                        try:

                            response = client.models.generate_content(
                                model="gemini-3.5-flash",
                                contents=prompt
                            )

                            answer = response.text

                            st.markdown(answer)

                            st.session_state.chat_history.append(
                                {
                                    "role": "assistant",
                                    "content": answer
                                }
                            )

                        except Exception:

                            st.error(
                                "Gemini is temporarily busy. "
                                "Please try again."
                            )

    except Exception:

        st.error(
            "Unable to read this PDF. "
            "Please upload a valid PDF document."
        )

# ==============================
# HOME SCREEN
# ==============================

else:

    st.markdown("## ✨ Your Document Workspace")

    st.markdown(
        "Upload a PDF to summarize, explore and ask questions."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-box">
            <h3>📑 Smart Summary</h3>
            <p>
            Generate structured summaries with key points
            and important details.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-box">
            <h3>🔍 Text Preview</h3>
            <p>
            Preview extracted text from your uploaded PDF.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="feature-box">
            <h3>💬 Document Q&A</h3>
            <p>
            Ask questions and get contextual answers
            from your document.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-box">
            <h3>📄 PDF Extraction</h3>
            <p>
            Extract readable content and document
            information from PDFs.
            </p>
        </div>
        """, unsafe_allow_html=True)
