# Twist Scraper

## Overview
Twist Scraper is a **web scraping and AI-powered query engine** that allows users to extract structured data from web pages and query it using an AI model. Built with **Selenium, BeautifulSoup, Streamlit, and LangChain**, this tool is ideal for **data engineering** and **automated web data extraction** workflows.

## Features
- **Web Scraping:** Uses Selenium to fetch website content.
- **Content Cleaning:** Removes unnecessary scripts and styles, leaving clean text.
- **AI-Powered Querying:** Uses Ollama's Llama3.1 model to extract structured insights from raw data.
- **Batch Processing:** Supports multiple URLs via file uploads.
- **Data Export:** Download extracted data in JSON or CSV formats.

## Use Cases
### 1. Data Engineering
- Automate data extraction for ETL pipelines.
- Clean and structure unstructured web data.
- Store extracted insights in databases for further processing.

### 2. Competitive Intelligence
- Extract pricing, product details, or news from competitor websites.
- Monitor industry trends through automated web data collection.

### 3. Research & Journalism
- Gather structured data from news articles.
- Analyze historical web content for patterns and insights.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Chrome browser installed
- ChromeDriver (ensure compatibility with your Chrome version)
- Virtual environment (recommended)

### Installation Steps
1. Clone this repository:


2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
   ```
   
3. Install dependencies:
   ```commandline
   pip install -r requirements.txt
   ```

4. Ensure chromedriver is set up correctly:

- Download ChromeDriver from ChromeDriver official site.

- Update the chrome_driver_path in scrape.py.

5. Run the application:
   ```commandline
   streamlit run main.py
   ```
   
## Usage Guide
1. **Enter a website URL** in the input field and click "Scrape Website."

2. **View extracted content** in the expandable section.

3. **Describe the data you need** (e.g., "Extract all dates mentioned").

4. **Click "Parse Content"** to process with AI.

5. **Download extracted data** as JSON or CSV.

6. **For batch processing,** upload a file with multiple URLs and download structured outputs.


## Contributing
Feel free to submit issues or pull requests! Contributions are welcome.