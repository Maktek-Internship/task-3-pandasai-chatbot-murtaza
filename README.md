# Prompt-Driven Data Analysis Application
## Overview
This Streamlit application allows users to perform data analysis on CSV files using natural language prompts. By leveraging PandasAI and Google Gemini, the app provides an intuitive interface for exploring datasets without needing to write complex queries.

## Features
- **CSV File Upload:** Upload any CSV file for analysis.
- **Smart Dataframe:** Automatically convert your data into a SmartDataframe for intelligent querying.
- **Natural Language Prompts:** Input natural language prompts to generate insights and analyses from your data.
- **Google Gemini Integration:** Utilizes Google Gemini for natural language processing, enhancing the app's ability to understand and respond to queries.
## Installation
### Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```
### Install the required packages:

```bash
pip install -r requirements.txt
```
### Set up your environment:

- Create a .env file in the root directory.
- Add your Google API key:
```plaintext
GOOGLE_API_KEY=your_api_key_here
```
### Usage
- Run the Streamlit app:

``` bash
streamlit run app.py
```
### Upload a CSV file:

### Use the file uploader in the app interface to upload your CSV file.
- Enter a prompt:


## Requirements
```
Python 3.x
Streamlit
Pandas
PandasAI
dotenv
Google Gemini API Key
```

## License
This project is licensed under the MIT License.
