import requests

def search_movie(movie_name: str, database_file: str):
    # database files: database/hits-anime.txt or database/hits.txt
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36"
    }
    results = []

    with open(database_file, "r") as file:
        for line in file:
            url = line.strip() + f"?filter={movie_name}"
            try:
                response = requests.get(url=url, headers=headers, timeout=10)
                if response.status_code == 200:
                    if movie_name.lower() in response.text.lower():
                        results.append(url)
            except requests.RequestException:
                continue  # Skip URLs that cause errors

    if results:
        with open("results.txt", "w") as file:
            for result in results:
                file.write(result + "\n")
    else:
        with open("results.txt", "w") as file:
            file.write(f"movie with name \"{format_text_second(movie_name)}\" was not found ): ")

#turns spaces to .
def format_text(text:str):
    return text.replace(" ", ".")
def format_text_second(text:str):
    return text.replace(".", " ")
    