import requests
from bs4 import BeautifulSoup

def get_google_results(query):
    url = f"https://www.google.com/search?q={query}"
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, header=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    return results

def extract_answers(results):
    answers = []
    for result in results:
        answer = result.get_text()
        answers.append(answer)
    return answers

def main():
    question = input("What is your question? ")
    results = get_google_results(question)
    answers = extract_answers(results)
    
    print("Answers:")
    for idx, answer in enumerate(answers, start=1):
        print(f"{idx}. {answer}")

if __name__ == "__main__":
    main()


import requests
from bs4 import BeautifulSoup

def get_google_results(query):
    url = f"https://www.google.com/search?q={query}"
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    return results

def extract_first_answer(results):
    if results:
        return results[0].get_text()
    else:
        return "Sorry, I couldn't find an answer."

def main():
    question = input("What is your question? ")
    results = get_google_results(question)
    answer = extract_first_answer(results)
    
    print("Answer:")
    print(answer)

main()
