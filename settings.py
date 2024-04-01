# URL
API_URL = 'https://api.github.com'
HTML_URL = 'https://github.com'
# --------------------------------- #

# --------------------------------- #

def get_github_token():
    with open('../../pw2.txt', 'r') as file:
        print("---------------------")
        print("1. API TOKEN READ.")
        print("---------------------")
        return file.readline().strip()

