import json
import random 
import asyncio

from core.gemini import generate_username
with open("categorized_words.json", "r", encoding="utf-8") as file:
        ALL_WORDS = json.load(file)

async def find_username(
          max_length: int, 
          noun: str, 
          verb: str, 
          adjectives: str, 
          use_ai: str, 
          minimal_rarity: int | str
        ) -> str | None:
        user_word = set()
        VALID_YES = ["yes", "y"]
        if noun.lower() in VALID_YES:
            user_word.update(ALL_WORDS["nouns"])
        if verb.lower() in VALID_YES:
            user_word.update(ALL_WORDS["verbs"])
        if adjectives.lower() in VALID_YES:
            user_word.update(ALL_WORDS["adjectives"])
        if not user_word:
            return None
        word_list = list(user_word)
        word_list = [word for word in word_list if len(word) <= max_length]
        if not word_list: 
            return None
        random.shuffle(word_list)
        if isinstance(minimal_rarity, str) and minimal_rarity.lower() == "no":
            minimal_rarity = 0
        elif not isinstance(minimal_rarity, int): 
            raise ValueError("minimal_rarity_error")
        if use_ai.lower() in VALID_YES:
            for word in word_list:
                try:
                    score = await generate_username(word)
                    if int(score.strip()) >= minimal_rarity:
                        return word
                except ValueError:
                    continue
        return word_list[0]