import importlib
import os, json

language = ""
while language not in ["ru", "en"]:
    language = input("Введите язык/Enter language (ru/en): ")

language = importlib.import_module(f"language.{language}")


def create_config():
    default_config = {
        "main_admin_id": input(language.setup_main_admin_id),
        "language": language,
        "info": {
            "greeting": language.default_greeting,
        },
    }
    open("config.json", "w").write(json.dumps(default_config, indent=4, ensure_ascii=False))


if not os.path.exists("config.json"):
    create_config()
elif input(language.setup_config).lower() == "y":
    create_config()
else:
    print(language.skip_setup_config)

if os.path.exists("database.db") and input(language.resetup_database).lower() == "y":
    os.remove("database.db")
    