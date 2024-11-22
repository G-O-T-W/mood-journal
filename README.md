# Mood Journal App

The **Mood Journal App** is a Streamlit-based application that allows users to track their mood by analyzing the sentiment of their daily journal entries. This app provides visual insights into the positivity and negativity of your entries, helping you monitor and reflect on your emotional well-being over time.

## Features

- **Sentiment Analysis**: Uses Natural Language Processing (NLP) to calculate positivity and negativity scores for daily journal entries.
- **Interactive Visualizations**: Displays sentiment trends using Plotly line charts.
- **Data Processing**: Reads text files as journal entries and processes them into a structured data format.
- **User-Friendly Interface**: Built using Streamlit for a clean, interactive, and responsive user experience.

## How It Works

1. **Add Your Journal Entries**: 
   - Write your daily thoughts and save them as `.txt` files in the `entries/` folder.
   - Ensure each file is named in the format `YYYY-MM-DD.txt` (e.g., `2024-10-27.txt`).

2. **Sentiment Analysis**:
   - The app uses the **VADER Sentiment Analyzer** from the `nltk` library to calculate positivity and negativity scores for each entry.

3. **Visualize Your Mood**:
   - The app processes all available journal entries and displays sentiment trends over time using interactive Plotly charts.

## Project Structure

- **main.py**: The primary script for the Streamlit app interface and visualization.
- **functions.py**: Handles data extraction, sentiment analysis, and processing of journal entries.
- **entries/**: A directory where all journal `.txt` files are stored. Each file represents a daily entry.

## Technologies Used

- **Streamlit**: For building the web-based user interface.
- **Pandas**: For data manipulation and processing.
- **NLTK (VADER Sentiment Analyzer)**: For sentiment analysis of journal entries.
- **Plotly**: For creating interactive and visually appealing charts.
- **Python**: The core programming language used to develop the app.

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/mood-journal-app.git
   cd mood-journal-app
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
3. Add your journal entries to the entries/ folder following the naming convention YYYY-MM-DD.txt.

4. Run the app:
    ```bash
    streamlit run main.py
    ```
   
5. Open the app in your browser (usually at http://localhost:8501) and start exploring your mood trends.


