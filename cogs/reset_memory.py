import discord
from discord.ext import commands
import json
from discord import app_commands
import os

class ResetChatCog(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @app_commands.command(name='reset_memory', description='Resets the chat memory for a specific channel. If no channel is specified, clears all memory.')
    @app_commands.checks.has_permissions(administrator=True)
    async def reset_memory(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        channel_id = channel.id if channel else None
        if channel_id:
            await self.reset_channel_memory(channel_id)
            await interaction.response.send_message(f"Chat history for channel '{channel.name}' has been reset.")
        else:
            await self.clear_all_memory()
            await interaction.response.send_message("All chat histories have been cleared.")

    async def reset_channel_memory(self, channel_id):
        """Resets the chat history for a specific channel."""
        try:
            with open('utils/data/history.json', 'r') as f:
                histories = json.load(f)

            if f"id_{channel_id}" in histories:
                del histories[f"id_{channel_id}"]
                with open('utils/data/history.json', 'w') as f:
                    json.dump(histories, f)

        except Exception as e:
            print(f"Error resetting channel memory: {str(e)}")

    async def clear_all_memory(self):
        """Clears all chat histories."""
        try:
            with open('utils/data/history.json', 'w') as f:
                json.dump({}, f)
            
        except Exception as e:
            print(f"Error clearing all memory: {str(e)}")

async def setup(bot):
    await bot.add_cog(ResetChatCog(bot))
