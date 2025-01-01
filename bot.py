import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Remplacer par votre propre token Telegram
API_TOKEN = 'YOUR_API_TOKEN'

# Configurer le journal de logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Fonction pour envoyer un message de bienvenue
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🧨 MARC LUCKYJET V2 🧨\nBienvenue! Vous pouvez demander des prédictions.")

# Fonction pour gérer la commande 'predict'
def predict(update: Update, context: CallbackContext) -> None:
    # Ici, on définit une simple prédiction
    prediction = "Votre prédiction est : 'Bonne chance!'"
    
    # Envoyer la prédiction à l'utilisateur
    update.message.reply_text(prediction)
    
    # Ajoutez un bouton pour redemander une prédiction
    update.message.reply_text("Cliquez sur le bouton ci-dessous pour une nouvelle prédiction.", reply_markup=telegram.ReplyKeyboardMarkup([["Prédire"]], one_time_keyboard=True))

# Fonction pour gérer la commande 'limit'
def limit(update: Update, context: CallbackContext) -> None:
    # Limite après 5 prédictions
    update.message.reply_text("Vous avez atteint votre limite de prédictions. Veuillez contacter +22656967818 pour plus d'informations.")
    update.message.reply_text("Cours d'activation : 'Tall@2008'.")

# Fonction principale qui configure et démarre le bot
def main() -> None:
    # Création de l'updater et du dispatcher
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Ajouter des gestionnaires pour les commandes
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("predict", predict))
    dispatcher.add_handler(CommandHandler("limit", limit))

    # Démarrer le bot
    updater.start_polling()

    # Laisser le bot tourner jusqu'à ce qu'il soit arrêté
    updater.idle()

if __name__ == '__main__':
    main()
