# Student Marks Analyzer

A Streamlit app that allows users to input a student's marks, visualize them with a bar chart, and download a PDF report of the results.

## Features
- Input a student's name and marks for five subjects (Math, Science, English, Hindi, Social Science).
- Calculate total marks, average, and pass/fail status (pass if all subjects >= 33).
- Visualize marks with a bar chart, including a passing marks threshold.
- Download a PDF report summarizing the student’s performance.

## Installation
1. Ensure you have Python 3.7+ installed on your system.
2. Clone this repository or download the project files:
   ```
   git clone <repository-url>
   ```
3. Navigate to the project directory:
   ```
   cd path dir
   ```
4. (Optional) Create a virtual environment:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   # OR
   source .venv/bin/activate  # On macOS/Linux
   ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you’re in the project directory and the virtual environment is activated (if used).
2. Run the Streamlit app:
   ```
   streamlit run main.py
   ```
3. Open the provided URL (e.g., `http://localhost:8501`) in your browser.
4. Enter the student’s name and marks for each subject.
5. Click "Analyze" to see the results, view the bar chart, and download the PDF report.

## Dependencies
The app requires the following Python libraries, listed in `requirements.txt`:
- `streamlit`
- `pandas`
- `matplotlib`
- `fpdf`

## Deployment on Streamlit Cloud
1. Push your project to a GitHub repository.
2. Ensure `requirements.txt` is in the repository root alongside `main.py`.
3. Sign in to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
4. Connect your GitHub repository and select the branch.
5. Set the app’s entry point to `main.py`.
6. Deploy the app and visit the provided URL (e.g., `marks-analyser.streamlit.app`).
