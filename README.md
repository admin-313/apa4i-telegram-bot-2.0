# apa4i-telegram-bot-2.0
Refactored and updated version of bot beloved by hundreds and admired by thousands

# TODO
- [ ] **Add SQLite support**
    - [ ] **Add SQLAlchemy**
    - [ ] **Add migrations via alembic**
- [ ] **Add Docker support**
- [ ] **Rewrite using Clean Architecture design approach**

# Deployment strategy
Add the following variables to your environment via docker compose or via your IDE if you're debugging:
- BOT_TOKEN
- ADMIN_TELEGRAM_ID
- LINK_TO_FB_PARSER

**BOT_TOKEN** is the bot token you get from BotFather

**ADMIN_TELEGRAM_ID** string of the id of user with administrator permit. 
Example: 3978450032 <-- Will add administrator permission to user with that id 

**LINK_TO_FB_PARSER** IP or domain name of your token getter microservice [Link to mine](https://github.com/admin-313/fb-cookies-microservice)