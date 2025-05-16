import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64

st.title("📊 Student Marks Analyzer")

# Input Student Name
name = st.text_input("Enter Student Name:")

# Input Subject Marks
st.subheader("Enter Subject Marks (out of 100)")
math = st.number_input("Math", min_value=0, max_value=100, step=1)
science = st.number_input("Science", min_value=0, max_value=100, step=1)
english = st.number_input("English", min_value=0, max_value=100, step=1)
hindi = st.number_input("Hindi", min_value=0, max_value=100, step=1)
sst = st.number_input("Social Science", min_value=0, max_value=100, step=1)

def create_pdf(name, marks_dict, total, average, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Student Marks Report", ln=1, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=1)
    pdf.ln(5)

    for subject, mark in marks_dict.items():
        pdf.cell(200, 10, txt=f"{subject}: {mark}", ln=1)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Total: {total} / 500", ln=1)
    pdf.cell(200, 10, txt=f"Average: {average:.2f}", ln=1)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=1)

    return pdf.output(dest='S').encode('latin1')  # Return as byte string

if st.button("Analyze"):
    # Store in dict and DataFrame
    marks = {
        "Math": math,
        "Science": science,
        "English": english,
        "Hindi": hindi,
        "Social Science": sst
    }
    df = pd.DataFrame(marks.items(), columns=["Subject", "Marks"])

    # Calculations
    total = sum(marks.values())
    average = total / 5
    result = "Pass" if all(mark >= 33 for mark in marks.values()) else "Fail"

    st.success(f"Student Name: {name}")
    st.write(f"**Total Marks:** {total} / 500")
    st.write(f"**Average Marks:** {average:.2f}")
    st.write(f"**Result:** {'✅ ' + result if result == 'Pass' else '❌ ' + result}")

    # Bar chart
    st.subheader("📈 Marks Visualization")
    fig, ax = plt.subplots()
    ax.bar(df["Subject"], df["Marks"], color='skyblue')
    ax.axhline(33, color='red', linestyle='--', label='Passing Marks')
    ax.set_ylabel("Marks")
    ax.set_title("Subject-wise Marks")
    ax.legend()
    st.pyplot(fig)

    # PDF generation
    st.subheader("📄 Download Report as PDF")
    pdf_bytes = create_pdf(name, marks, total, average, result)
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{name}_report.pdf">📥 Click here to Download PDF</a>'
    st.markdown(href, unsafe_allow_html=True)
