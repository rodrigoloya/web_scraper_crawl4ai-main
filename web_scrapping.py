# ── requirements ─────────────────────────────────────────────────────────
# pip install crawl4ai openai pydantic python-dotenv
# playwright install

import os, json, asyncio
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    CacheMode,
    LLMConfig,
    CrawlResult,
    JsonCssExtractionStrategy,
    JsonXPathExtractionStrategy
)

from crawl4ai.extraction_strategy import LLMExtractionStrategy



# ── 1. load keys ─────────────────────────────────────────────────────────
load_dotenv()                                    # puts keys in env vars
URL_TO_SCRAPE = "https://www.facebook.com/groups/222524304582949/"

# ── 2. declare a schema that matches the *instruction* ───────────────────
class Model(BaseModel):
    rank: int = Field(..., description="Position in the list")
    actorName: str
    actorUrl: str
    actorId: str
    storyId: str
    permalink: str
    storyText: str
    actorEmail: str

INSTRUCTION_TO_LLM = """
You are given a Facebook group page. 
Return an array of model objects (rank, actor, story, permalink, email).  
Return **only** valid JSON matching the schema – no markdown.
"""
JSON_CSS_INSTRUCTION_TO_LLM = """
From the HTML, I have shared a sample of one of the group post story extract the following fields: 
rank, actorName, actorUrl, actorId, storyId, permalink, storyText, actorEmail. 
Please generate a schema for this"""

sample_html = """

"""

# ── 3. DeepSeek is OpenAI-compatible, so pass base_url + model name ──────
llm_cfg = LLMConfig(
    provider="gemini/gemini-2.5-flash-preview-05-20",          # ✅ include model in the provider string
    api_token=os.getenv('GEMINI_API_KEY'),
    # base_url="https://api.deepseek.com/v1"
)

# jsonSchema = JsonCssExtractionStrategy.generate_schema(
#     html=sample_html,
#     llm_config=llm_cfg,
#     query=JSON_CSS_INSTRUCTION_TO_LLM,
# )

# print (f"Generated JSON Schema: {json.dumps(jsonSchema, indent=2)}")

# ── 3.1. or use XPath to extract data from the HTML ──────────────────────
# jsonSchema = JsonXPathExtractionStrategy.generate_schema(
#     html=sample_html,
#     llm_config=llm_cfg,
#     query=JSON_CSS_INSTRUCTION_TO_LLM,
# )


# extraction_strategy = JsonCssExtractionStrategy(schema=jsonSchema)
# extractionConfig = CrawlerRunConfig(
#     extraction_strategy=extraction_strategy)

# ── 4. attach the extraction strategy ────────────────────────────────────
llm_strategy = LLMExtractionStrategy(
    llm_config=llm_cfg,
    schema=Model.model_json_schema(),      
    extraction_type="schema",    
    instruction=INSTRUCTION_TO_LLM,
    chunk_token_threshold=1000,
    apply_chunking=True, 
    overlap_rate=0.0,
    input_format="markdown",
    verbose=True,
    # extra_args={
    #     "temperature": 0.6,  # set to 0 for deterministic output
    #     "max_tokens": 2000,  # adjust based on your needs
    # }
)

crawl_cfg = CrawlerRunConfig(
    extraction_strategy=llm_strategy,
    cache_mode=CacheMode.DISABLED,
    remove_overlay_elements=True,
    exclude_external_links=True,  
    scan_full_page=True,   # Enables scrolling
    scroll_delay=0.2,       # Waits 200ms between scrolls (optional)
    wait_for_images=True,  # Wait for images to load
    session_id="fb_session",  # Unique session ID for the crawl
    js_only=True,
    js_code='document.querySelectorAll("div.html-div > div[data-ad-rendering-role=story_message]")?.forEach(p => p.querySelector("div[role=button]")?.click());',  
    page_timeout=60000,  # 60s limit
    
    excluded_tags=["script", "style"],
    #wait_for="css:a[attributionsrc]",
)

browser_cfg = BrowserConfig(browser_type="chromium",  # Type of browser to simulate,
                            headless=False, 
                            verbose=True, 
                            text_mode=True,
                            use_managed_browser=True,
                            user_data_dir="c:\\Projects\\python\\repo\\web_scraper_crawl4ai-main\\my_chrome_profile",
                             
                            )

# ── 5. run the crawl ─────────────────────────────────────────────────────
async def main():
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result: List[CrawlResult] = await crawler.arun(URL_TO_SCRAPE, config=crawl_cfg)

        posts = []
        for r in result:
            if r.success:
                data = json.loads(r.extracted_content)
                print("✅ extracted", len(data), "items")
                posts.extend(data)
                print(json.dumps(data, indent=2)[:1000])  # Print first 1000 chars of the JSON
                 
            else:
                print("❌ error:", r.error_message)
                print(llm_strategy.show_usage())

        # if result.success:
        #     data = json.loads(result.extracted_content)
        #     print("✅ extracted", len(data), "items")
        #     for p in data[:10]: print(p)
        # else:
        #     print("❌ error:", result.error_message)
        #     print(llm_strategy.show_usage())   # token cost insight


if __name__ == "__main__":
    asyncio.run(main())
