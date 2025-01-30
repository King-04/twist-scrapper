from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are an AI-powered data extraction assistant. Your task is to extract specific information from the given text content: {dom_content}. "
    "Follow these instructions carefully to ensure accuracy:\n\n"

    "### Extraction Guidelines:\n"
    "1. **Relevance:** Extract only the data that directly matches the given description: \"{parse_description}\".\n"
    "2. **Precision:** Avoid adding any extra commentary, explanations, or unrelated content.\n"
    "3. **Format:** Present the extracted information in a structured format (e.g., bullet points, JSON, or plain text) if applicable.\n"
    "4. **Empty Response Handling:** If no relevant data is found, return an empty string (`''`) without any placeholders or default messages.\n"
    "5. **No Additional Text:** Do not add headers, labels, or summaries—return only the requested data.\n\n"

    "Ensure your response strictly adheres to these rules."
)

model = OllamaLLM(model="llama3.1")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
