# Facebook Crawler

This project is a web crawler built with Python that extracts venue data (wedding reception venues) from a website using asynchronous programming with Crawl4AI. It utilizes a language model-based extraction strategy and saves the collected data to a CSV file.

## Features

- Asynchronous web crawling using [Crawl4AI](https://pypi.org/project/Crawl4AI/)
- Data extraction powered by a language model (LLM)
- CSV export of extracted venue information


## Installation

1. **Create and Activate a Conda Environment**

   ```bash
   conda create -n facebook-groups-crawler python=3.12 -y
   conda activate facebook-groups-crawler
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **Install Playwrite**
   playwright install

3. **Set Up Your Environment Variables**

   Create a `.env` file in the root directory with content similar to:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   *(Note: The `.env` file is in your .gitignore, so it won’t be pushed to version control.)*

## Usage

To start the crawler, run:

```bash
python main.py
```

The script will crawl the specified website, extract data page by page, and save the complete venues to a `complete_venues.csv` file in the project directory. Additionally, usage statistics for the LLM strategy will be displayed after crawling.

## Configuration

The `config.py` file contains key constants used throughout the project:

- **BASE_URL**: The URL of the website from which to extract venue data.
- **CSS_SELECTOR**: CSS selector string used to target venue content.
- **REQUIRED_KEYS**: List of required fields to consider a venue complete.

You can modify these values as needed.

## Additional Notes

- **Logging:** The project currently uses print statements for status messages. For production or further development, consider integrating Python’s built-in `logging` module.
- **Improvements:** The code is structured in multiple modules to maintain separation of concerns, making it easier for beginners to follow and extend the functionality.
- **Dependencies:** Ensure that the package versions specified in `requirements.txt` are installed to avoid compatibility issues.

## License

Include license information if applicable.




To run the Groq RAG example code, use the command `streamlit run langchain_groq_rag.py`

| Video link | Notebook |
| --- | ----------- |
| [Getting Started with Groq API](https://youtu.be/S53BanCP14c) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://tinyurl.com/2nxdv2m8)|
| [Better RAG: Hybrid Search in LangChain with BM25 and Ensemble](https://youtu.be/r2m9DbEmeqI) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://tinyurl.com/33wc8sav)|
| [Fine-Tune Your Own Tiny-Llama on Custom Dataset](https://youtu.be/OVqe6GTrDFM) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://tinyurl.com/4eny9cvc)|
| [Run Mixtral 8x7B MoE in Google Colab](https://youtu.be/Zo3CTapKJ4I) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://tinyurl.com/2nn5snb4)|
| [GEMINI Pro with LangChain - Chat, MultiModal and Chat with your Documents](https://youtu.be/7h8ZHSkAkas) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/28bw3ntv)|
| [Supercharge Your RAG with Contextualized Late Interactions](https://youtu.be/xTzUn3G9YA0) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/czk85xfr)|
| [Advanced RAG with ColBERT in LangChain and LlamaIndex](https://youtu.be/kEgeegk9iqo) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/4dte2njt)|
| [Claude 3 Introduces Function Calling and Tool Usage](https://youtu.be/fDErWDOT4XE) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/y5kefhvn)|
| [Groq Now Supports Function Calling](https://youtu.be/ybau-0ZIsMc)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/5n9y2f2y)|
| [Create Financial Agents with Vision 👀 - Powered by Claude 3 Haiku & Opus](https://youtu.be/a5OW5UAyC3E)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/56krc8az)|
| [MIXTRAL 8x22B MOE: The BEST Open LLM Just got better - RAG and Function Calling](https://youtu.be/Zn7S5mLfkrc)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/b5h9v7w2)|
| [Insanely Fast LLAMA-3 on Groq Playground and API for FREE](https://youtu.be/ySwJT3Z1MFI)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/57yhf26h)|
| [SmolAgents: Production Ready Agents with Minimal Abstraction](https://youtu.be/icRKf_Mvmt8)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://tinyurl.com/c7ecntbz)|







