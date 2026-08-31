![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

# username-bot

## About the Bot:
The bot will take usernames (available), check them against specified criteria, and then give them to you if all criteria match.

## Criteria
1. maximal length
2. search for a noun/verb
3. to use AI or not
4. (If AI is used): Minimal username rarity 
**and most likely other different criteria**

## stages
- [x] create a project
- [x] create a bot
- [ ] add criteria
- [ ] integrate gemini
- [ ] finish the project

## instructions

1. **clone the project**: 
```bash
git clone https://github.com/Luto228/username-bot.git
cd username-bot
```
2. **create a venv**: windows:
```bash 
python -m venv myenv
```
macOS/Linux: 
```bash 
python3 -m venv myenv
```
3. **activate the venv**: windows: 
```bash 
.\myenv\Scripts\activate
```
macOS/Linux: 
```bash 
source myenv/bin/activate
```
4. **Install a aiogram and python-dotenv**: 
```bash
pip install aiogram python-dotenv
```
5. **Get bot token**: Go to the telegram and write /newbot in BotFather(to find it just write Botfather in search), write his name and username. He'll give you a token
6. **get google api key, step 1**: Go to the ai studio, click on "Project", then "Create a new project", write any name and click "create project", then just close a window "create new key"
7. **get google api key, step 2**: go to the "API keys", click on "Create API key", write any name and choose a created project in "choose an imported project". Then just click "create key", and copy API key
8. **Delete .example from .env.example and write your Bot token and gemini Api key in the variable**