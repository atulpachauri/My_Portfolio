import sqlite3

socials = [
    {
        "platform": "email",
        "url": "mailto:mariya@pythonsimplified.org",
        "icon": "assets/email_icon.png"
    },
    {
        "platform": "youtube",
        "url": "https://www.youtube.com/@pythonsimplified",
        "icon": "assets/youtube_icon.png"
    },
    {
        "platform": "linkedin",
        "url": "https://linkedin.com/in/mariyasha888",
        "icon": "assets/li_icon.png"
    },
    {
        "platform": "github",
        "url": "https://github.com/mariyasha",
        "icon": "assets/gh_icon.png"
    },
    {
        "platform": "twitter",
        "url": "https://twitter.com/mariyasha888",
        "icon": "assets/x_icon.png"
    }
]

projects = [
    {
        "title": "AI voice chat",
        "description": "speech-to-text and text-to-speech voice assistant using a pre-trained Qwen language model",
        "link": "https://github.com/MariyaSha/voice_chat",
        "thumbnail": "assets/voice_chat.png"
    },
    {
        "title": "Stock Predicting App",
        "description": "full-stack S&P 500 stock value predicting data dashboard.",
        "link": "https://github.com/MariyaSha/data_science_dashboard",
        "thumbnail": "assets/stock_prediction.png"
    },
    {
        "title": "Random Recipe Picker",
        "description": "Tkinter GUI application that fetches random recipes from Sqlite dataset.",
        "link": "https://github.com/MariyaSha/RandomRecipePicker",
        "thumbnail": "assets/recipe_picker.png"
    },
    {
        "title": "Image Generating App",
        "description": "image generating app with Docker, Satble Diffusion and upscaling techniques.",
        "link": "https://github.com/MariyaSha/StableDiffusion_GUI_App",
        "thumbnail": "assets/image_gen.png"
    },
    {
        "title": "AlteredNet Image Dataset",
        "description": "manually curated image dataset and research for detection of real and AI-generated images.",
        "link": "https://github.com/MariyaSha/AlteredNet",
        "thumbnail": "assets/alterednet.png"
    },
    {
        "title": "DJ Mixing Studio",
        "description": "DJ Deck Mixer GUI Application with C++ and JUCE, based on Object Oriented Programming principles.",
        "link": "https://github.com/MariyaSha/DJMixingStudio",
        "thumbnail": "assets/dj_studio.png"
    }
]

skills = [
    {"name": "Python"},
    {"name": "Flask"},
    {"name": "Jinja2"},
    {"name": "HTML"},
    {"name": "CSS"},
    {"name": "Git"},
    {"name": "Docker"},
    {"name": "Transformers"},
    {"name": "Tkinter"},
    {"name": "Pytorch"},
    {"name": "C++"},
    {"name": "JUCE"},
    {"name": "Sqlite"}
]

profile = [
    {
        "name": "Mariya Sha, BSc",
        "title": "Software Developer",
        "bio": "Fresh graduate of UoL, passionate about data science and AI.",
        "location": "Mission, British Columbia"
    }
]

conn = sqlite3.connect('instance/portfolio.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS socials')
c.execute('DROP TABLE IF EXISTS projects')
c.execute('DROP TABLE IF EXISTS skills')
c.execute('DROP TABLE IF EXISTS profile')

c.execute('CREATE TABLE socials (id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, url TEXT, icon TEXT)')
c.execute('CREATE TABLE projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, link TEXT, thumbnail TEXT)')
c.execute('CREATE TABLE skills (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
c.execute('CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT, bio TEXT, location TEXT)')

c.executemany('INSERT INTO socials (platform, url, icon) VALUES (:platform, :url, :icon)', socials)
c.executemany('INSERT INTO projects (title, description, link, thumbnail) VALUES (:title, :description, :link, :thumbnail)', projects)
c.executemany('INSERT INTO skills (name) VALUES (:name)', skills)
c.executemany('INSERT INTO profile (name, title, bio, location) VALUES (:name, :title, :bio, :location)', profile)

conn.commit()
conn.close()

print("Database tables dropped and repopulated in instance/portfolio.db!")