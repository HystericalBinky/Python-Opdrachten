'''Programma voor Quiz Security Toets'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import random
from bs4 import BeautifulSoup

with open("opdrachten/hfst11/opdr11.6/toets2-security_files/toets2-security.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

def extract_questions(soup):
    questions = []
    vraag_divs = soup.find_all("div", class_="vraagdiv")
    
    for div in vraag_divs:
        question_text_raw = div.find("td", class_="nummer").find_next("td").get_text(separator=" ").strip()
        question_text = " ".join(question_text_raw.split())
        
        rows = div.find_all("tr")[1:]
        options = {}
        correct_answer = None
        
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                key = cols[0].get_text(strip=True)
                value_raw = cols[1].get_text(strip=True)
                value = " ".join(value_raw.split())
                
                if "Oplossing" in key or "Oplossing" in value:
                    correct_answer = value.replace("Oplossing. ", "").strip()
                elif value:
                    options[key] = value
        
        if question_text and options and correct_answer:
            questions.append({
                "question": question_text,
                "options": options,
                "correct": correct_answer
            })
    return questions

quiz_questions = extract_questions(soup)

def run_quiz(questions):
    print("Welkom bij de Security Quiz!")
    while True:
        try:
            num_questions = int(input("Hoeveel vragen wil je oefenen? (0 = aflsuiten): "))
            if num_questions == 0:
                print("Bedankt voor het oefenen!")
                break
            if num_questions > len(questions):
                print(f"Er zijn maar {len(questions)} vragen om te oefenen.")
                continue
            
            selected_questions = random.sample(questions, num_questions)
            score = 0
            results = []
            
            for i, q in enumerate(selected_questions, start=1):
                print(f"\nVraag {i}: {q['question']}")
                for key, option in q["options"].items():
                    print(f"  {key}. {option}")
                
                answer = input("Jouw antwoord (A, B, C, ...): ").strip().upper()
                if answer == q["correct"]:
                    print("Goed!")
                    score += 1
                    results.append((q, answer, True))
                else:
                    print(f"Fout. Het goeie antwoord is {q['correct']}.")
                    results.append((q, answer, False))
            
            percentage = (score / num_questions) * 100
            print("\nResultaten:")
            print(f"Goeie antwoorden: {score}")
            print(f"Foute antwoorden: {num_questions - score}")
            print(f"Percentage goed: {percentage:.2f}%")
            for q, ans, correct in results:
                status = "Goed" if correct else f"Fout (Goed: {q['correct']})"
                print(f"Vraag: {q['question']}\nJouw aantwoord: {ans} ({status})\n")
        
        except ValueError:
            print("Voer een geldig nummer in.")

run_quiz(quiz_questions)