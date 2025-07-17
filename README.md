# GedajBot

Bot Telegram de Geekmania 🤖🎬
Fonctionnalités :
- Réactions intelligentes (GEDAJ, call, etc.)
- Commandes d’aide, d’appel, d’infos, etc.
- Interaction personnalisée selon l’utilisateur
- Système d’abonné du mois + cadeaux 🎁
- Intégration sur Render avec Gunicorn & Flask

Déployé sur : [Render](https://gedaj.onrender.com)

GeekmaniaBots/
├── bots/
│   ├── main.py          (GeekmaniaBot)
│   ├── news_bot.py      (GeekNewsBot)
│   └── fun_bot.py       (GeekFunBot)
├── database/
│   ├── db.py            (Gestion SQLite)
│   └── users.db         (Fichier DB)
├── config.py            (Tokens API)
├── requirements.txt     (Dépendances)
└── README.md            (Documentation)
