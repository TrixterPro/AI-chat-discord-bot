# Discord AI Chatbot using Gemini AI Model

## Overview
This repository contains a Discord bot that utilizes the Gemini AI model for intelligent conversations. The bot is designed to respond when mentioned and has a memory system that allows for personalized interactions in different channels.

## Installation

1. **Set Up Your Discord Bot Token:**
   - Navigate to `config.py` in the repository.
   - Input your Discord bot token. To obtain a token:
     1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
     2. Create a new application.
     3. Under the "Bot" tab, click "Add Bot," then "Reset Token," and lastly "Copy" the token.

2. **Environment Variable Setting (Optional):**
   - If you prefer to use environment variables, set the `use_env` option to `True` in `config.py`. 
   - Create a `.env` file in the root directory and add your token like so:
     ```
     TOKEN='your_discord_bot_token'
     ```

3. **Gemini API Key:**
   - To obtain your Gemini API key:
     1. Go to [ai.google.dev](https://ai.google.dev) and click on "Get API key in studio." (You can also go directly to this [link](https://aistudio.google.com/app/apikey).)
     2. Click "Create API Key," select a project, and then click "Generate Key" in the existing project.
   - If `use_env` is set to `True`, you will also need to add your Gemini API key to the `.env` file:
     ```
     KEY='your_gemini_api_key'
     ```
   - If `use_env` is set to `False`, input the Gemini API key in the `key.json` file located in the `utils` directory.

4. **Training Instructions:**
   - Provide the bot with instructions to understand its responses by editing the `instructions.txt` file found in the `utils` folder.

5. **Install Dependencies:**
   - Make sure to install the required dependencies by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

6. **Important Files:**
   - Do not remove the `history.json` file located in the `data` folder as it is crucial for the bot's operation.

## Bot Features

- The bot will only reply when mentioned (using `@bot` or through the reply feature in Discord).
- The `/reset_memory` slash command allows you to reset the bot's memory:
  - If no channel is specified, all memories will be reset.
  - If a channel is specified, only that channel's memory will be reset.
  
Each channel has its own memory, ensuring that conversations are independent and tailored to that specific channel.

## Logging
- Error logs can be found in the `logs.log` file located in the main directory.

## Owner Information
- **Owner Name:** Trix
- **Discord Username:** codewithtrix
