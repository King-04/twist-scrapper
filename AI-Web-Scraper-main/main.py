import streamlit as st
import pandas as pd
import json
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Streamlit UI
st.title("TWIST SCRAPPER \n WEB DATA EXTRACTOR AND AI QUERY ENGINE")
st.markdown("Extract and structure data from any URL, query it with AI, and download for further analysis.")

url = st.text_input("Enter Website URL", placeholder="e.g., https://example.com")

# Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Display the cleaned content in an expandable text box
        with st.expander("View Cleaned Content"):
            st.text_area("Cleaned Content", cleaned_content, height=300)

# Query the Data with AI
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse", placeholder="e.g., Extract all dates mentioned.")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content with AI...")

            # Split DOM content and parse with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)

            # Display the parsed results
            st.subheader("Parsed Results")
            st.text_area("Results", parsed_result, height=300)

            # Save parsed results to session state
            st.session_state.parsed_result = parsed_result

# Step 3: Save and Export
if "parsed_result" in st.session_state:
    st.subheader("Export Options")

    # Save as JSON
    if st.button("Download as JSON"):
        json_output = json.dumps({"parsed_result": st.session_state.parsed_result}, indent=4)
        st.download_button(
            label="Download JSON",
            file_name="parsed_results.json",
            mime="application/json",
            data=json_output,
        )

    # Save as CSV
    if st.button("Download as CSV"):
        parsed_data = [line for line in st.session_state.parsed_result.splitlines() if line.strip()]
        df = pd.DataFrame(parsed_data, columns=["Parsed Results"])
        csv_output = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            file_name="parsed_results.csv",
            mime="text/csv",
            data=csv_output,
        )

# Step 4: Batch Processing (Optional)
with st.expander("Batch Processing"):
    uploaded_file = st.file_uploader("Upload a file with URLs (one URL per line)", type=["txt"])

    if uploaded_file and st.button("Process Batch"):
        urls = uploaded_file.read().decode("utf-8").splitlines()
        batch_results = {}

        for i, batch_url in enumerate(urls, start=1):
            st.write(f"Processing URL {i}/{len(urls)}: {batch_url}")
            dom_content = scrape_website(batch_url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)
            dom_chunks = split_dom_content(cleaned_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            batch_results[batch_url] = parsed_result

        # Save batch results to JSON
        batch_json_output = json.dumps(batch_results, indent=4)
        st.download_button(
            label="Download Batch Results as JSON",
            file_name="batch_results.json",
            mime="application/json",
            data=batch_json_output,
        )
