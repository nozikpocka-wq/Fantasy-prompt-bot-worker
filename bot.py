import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ---------- НАСТРОЙКИ ----------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
REF_ID = os.environ.get("REF_ID", "fantasy")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан в переменных окружения!")

# ---------- БАЗА ТЕГОВ ----------
fantasy_data = {
    "races": ["elf", "dark elf", "orc female", "demoness", "succubus", "tiefling",
              "goblin girl", "vampire lady", "angel", "fallen angel", "dragon kin",
              "kobold", "slime girl", "wolf girl", "cat girl", "harpy", "lamia", "centaur woman"],
    "bodies": ["muscular", "curvy", "thick thighs", "wide hips", "toned abs", "small breasts",
               "huge breasts", "petite", "tall", "athletic", "plump", "pregnant", "sweat",
               "oiled skin", "visible veins", "soft skin", "scarred body", "tattooed"],
    "faces": ["angry", "blush", "smirk", "ahegao", "serious", "looking at viewer",
              "closed eyes", "teary eyes", "evil grin", "licking lips", "open mouth"],
    "outfits": ["leather armor", "torn dress", "see through silk robe", "dark plate armor",
                "tribal fur", "battle worn bikini", "chains only", "nothing", "slime covered",
                "transparent cloth", "ripped stockings", "high heels", "elven jewelry"],
    "actions": ["fighting a monster", "casting dark magic", "bound by tentacles", "riding a dragon",
                "kneeling", "spread legs", "from behind", "arms above head", "dominating a throne",
                "bathing in moonlit pond", "chained to an altar", "holding a glowing sword",
                "surrendering", "casting healing spell", "drinking potion"],
    "backgrounds": ["dark dungeon", "forbidden forest", "volcanic cave", "ancient elven ruins",
                    "demon lord's castle", "enchanted glade", "floating islands", "underwater temple",
                    "wizard's tower", "frosty mountains", "haunted graveyard"],
    "effects": ["sweat", "glowing runes", "magic particles", "wet skin", "steam",
                "moonlight", "fire sparks", "blood splatter", "shadow tentacles", "ethereal glow"],
    "lighting": ["cinematic lighting", "volumetric fog", "rim light", "harsh shadows",
                 "soft candle light", "bioluminescence", "lightning flash", "dusk"]
}

def generate_prompt():
    race = random.choice(fantasy_data["races"])
    body = random.choice(fantasy_data["bodies"])
    face = random.choice(fantasy_data["faces"])
    outfit = random.choice(fantasy_data["outfits"])
    action = random.choice(fantasy_data["actions"])
    bg = random.choice(fantasy_data["backgrounds"])
    effect = random.choice(fantasy_data["effects"])
    light = random.choice(fantasy_data["lighting"])
    prompt = (f"{race}, {body}, {face}, wearing {outfit}, {action}, {bg}, {effect}, {light}, "
              f"masterpiece, best quality, nsfw, cgi, intricate details")
    return prompt

# ---------- КОМАНДЫ БОТА ----------
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 *Hardcore Fantasy Prompt Bot* 🔥\n\n"
        "Команды:\n"
        "/prompt — получить случайный промпт\n"
        "/link — реферальная ссылка PornWorks\n\n"
        "Скопируй промпт, перейди по ссылке и вставь в поле генерации!",
        parse_mode="Markdown"
    )

async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    p = generate_prompt()
    await update.message.reply_text(f"🎲 *Твой промпт:*\n\n`{p}`", parse_mode="Markdown")

async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ref_link = f"https://pornworks.app/?ref={REF_ID}"
    await update.message.reply_text(
        f"🔗 *Твоя реферальная ссылка:*\n{ref_link}",
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prompt", prompt))
    app.add_handler(CommandHandler("link", link))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
