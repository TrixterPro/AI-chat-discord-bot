class basicconfig:


    # Weather to use .env or not
    # Only accepts True or False values.
    # Setting this to True will make it retrieve the API key from .env
    # Settings this to False will make it to retrieve the API key from the key.json file. (./utils/key.json)

    use_env = False


    # NOTE: IF YOU HAVE use_env SET TO TRUE THEN YOU DON'T HAVE TO INPUT YOUR TOKEN HERE!
    # Your discord bot token from developer portal. (https://discord.com/developers)

    TOKEN = ""