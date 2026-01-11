import discord
from app.bot.helper.confighelper import DISCORD_LANGUAGE

# these were copied from the app object. They could be made static instead but I'm lazy.
async def embederror(recipient, message, ephemeral=True, message_fr=None):
    """Send error message based on language setting"""
    french_msg = message_fr if message_fr else message
    
    if DISCORD_LANGUAGE == "en":
        # English only
        embed = discord.Embed(title="ERROR", description=message, color=0xf54242)
        await send_embed(recipient, embed, ephemeral)
    elif DISCORD_LANGUAGE == "fr":
        # French only
        embed = discord.Embed(title="ERREUR", description=french_msg, color=0xf54242)
        await send_embed(recipient, embed, ephemeral)
    else:
        # Both languages (default)
        embed_en = discord.Embed(title="🇬🇧 ERROR", description=message, color=0xf54242)
        await send_embed(recipient, embed_en, ephemeral)
        embed_fr = discord.Embed(title="🇫🇷 ERREUR", description=french_msg, color=0xf54242)
        await send_embed_followup(recipient, embed_fr)

async def embedinfo(recipient, message, ephemeral=True, message_fr=None):
    """Send info message based on language setting"""
    french_msg = message_fr if message_fr else message
    
    if DISCORD_LANGUAGE == "en":
        # English only
        embed = discord.Embed(title=message, color=0x4266f5)
        await send_embed(recipient, embed, ephemeral)
    elif DISCORD_LANGUAGE == "fr":
        # French only
        embed = discord.Embed(title=french_msg, color=0x4266f5)
        await send_embed(recipient, embed, ephemeral)
    else:
        # Both languages (default)
        embed_en = discord.Embed(title="🇬🇧 " + message, color=0x4266f5)
        await send_embed(recipient, embed_en, ephemeral)
        embed_fr = discord.Embed(title="🇫🇷 " + french_msg, color=0x4266f5)
        await send_embed_followup(recipient, embed_fr)

async def embedcustom(recipient, title, fields, ephemeral=True, title_fr=None, fields_fr=None):
    """Send custom message based on language setting"""
    french_title = title_fr if title_fr else title
    french_fields = fields_fr if fields_fr else fields
    
    if DISCORD_LANGUAGE == "en":
        # English only
        embed = discord.Embed(title=title)
        for k in fields:
            embed.add_field(name=str(k), value=str(fields[k]), inline=True)
        await send_embed(recipient, embed, ephemeral)
    elif DISCORD_LANGUAGE == "fr":
        # French only
        embed = discord.Embed(title=french_title)
        for k in french_fields:
            embed.add_field(name=str(k), value=str(french_fields[k]), inline=True)
        await send_embed(recipient, embed, ephemeral)
    else:
        # Both languages (default)
        embed_en = discord.Embed(title="🇬🇧 " + title)
        for k in fields:
            embed_en.add_field(name=str(k), value=str(fields[k]), inline=True)
        await send_embed(recipient, embed_en, ephemeral)
        embed_fr = discord.Embed(title="🇫🇷 " + french_title)
        for k in french_fields:
            embed_fr.add_field(name=str(k), value=str(french_fields[k]), inline=True)
        await send_embed_followup(recipient, embed_fr)

async def send_info(recipient, message, ephemeral=True):
    if isinstance(recipient, discord.InteractionResponse):
        await recipient.send_message(message, ephemeral=ephemeral)
    elif isinstance(recipient, discord.User) or isinstance(recipient, discord.member.Member) or isinstance(recipient, discord.Webhook):
        await recipient.send(message)

async def send_embed(recipient, embed, ephemeral=True):
    if isinstance(recipient, discord.User) or isinstance(recipient, discord.member.Member) or isinstance(recipient, discord.Webhook):
        await recipient.send(embed=embed)
    elif isinstance(recipient, discord.InteractionResponse):
        await recipient.send_message(embed=embed, ephemeral=ephemeral)

async def send_embed_followup(recipient, embed):
    """Send a follow-up embed message (for the second language)"""
    if isinstance(recipient, discord.User) or isinstance(recipient, discord.member.Member) or isinstance(recipient, discord.Webhook):
        await recipient.send(embed=embed)
    elif isinstance(recipient, discord.InteractionResponse):
        # For InteractionResponse, we need to use followup after the first response
        try:
            await recipient.followup.send(embed=embed, ephemeral=True)
        except:
            # If followup fails, try using the interaction's channel
            pass