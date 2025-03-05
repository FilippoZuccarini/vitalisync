import requests
from bs4 import BeautifulSoup

# Per scaricare il contenuto modificare l'URL e il nome del file di output

# headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

def download_content(url, output_file):
    response = requests.get(url, #headers=headers
                            )
    if response.status_code != 200:
        print(f"Errore nel caricamento della pagina: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    content = ""

    # Estrarre il titolo e il contenuto
    title = soup.find("h1").text
    content += f"# {title}\n\n"
    paragraphs = soup.find_all("p")

    for paragraph in paragraphs:
        content += paragraph.text + "\n\n"

    # Salva il contenuto in un file Markdown
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Contenuto salvato in {output_file}")

if __name__ == "__main__":
    url = "https://www.news-medical.net/health/What-is-Oxygen-Saturation.aspx"
    output_file = "./docs/out.md"
    download_content(url, output_file)