import os
from google import genai
from google.genai import types


async def generate_username(username: str) -> str | None:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    response = await client.aio.models.generate_content(
        model = "gemini-3.6-flash",
        contents = f"""
        You are a strict, automated Telegram username evaluator. 

        Your task is to analyze a username based on Brevity, Aesthetic Appeal, and Marketability, and combine them into a single overall score from 1 to 10.

        STRICT FORMAT RULES:
        - Respond EXCLUSIVELY with a single integer from 1 to 10 (e.g., 8).
        - Absolutely NO "/10", NO introductory words, NO explanations, NO Markdown formatting, NO quotes, and NO punctuation.
        - Your entire output MUST contain ONLY digits.

        EXAMPLES:
        Input: @crypto
        Output: 10

        Input: @user_123456_test
        Output: 2

        Input: @solana
        Output: 9
        
        username= {username}"""
    )

    return response.text