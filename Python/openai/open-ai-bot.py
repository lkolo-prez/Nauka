import openai
import os
import docx

# Ustaw klucz API
openai.api_key = "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"  # Zamień "YOUR_API_KEY" na swój rzeczywisty klucz API

def chat_with_gpt(message):
    response = openai.Completion.create(
        engine="code-davinci-002	",
        prompt=f"Odpowiedz na pytanie: {message}",
        temperature=0.8,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

def save_conversation_to_word(conversation, output_file):
    doc = docx.Document()
    
    for role, text in conversation:
        doc.add_paragraph(f"{role}: {text}")
    
    doc.save(output_file)

def wczytaj_pytania_z_pliku(plik_txt):
    with open(plik_txt, 'r', encoding='utf-8') as plik:
        pytania = [linia.strip() for linia in plik.readlines()]
    return pytania

def main():
    # Wczytaj pytania z pliku tekstowego
    plik_pytan = "pytania.txt"
    pytania = wczytaj_pytania_z_pliku(plik_pytan)

    print("Witaj w czacie z GPT-4. Wpisz 'quit' aby zakończyć.")
    conversation = []

    for pytanie in pytania:
        print("Pytanie: " + pytanie)

        response = chat_with_gpt(pytanie)
        print("GPT-4: " + response)
        
        conversation.append(("Pytanie", pytanie))
        conversation.append(("GPT-4", response))

    save_conversation_to_word(conversation, "rozmowa.docx")
    print("Rozmowa została zapisana do pliku rozmowa.docx")

if __name__ == "__main__":
    main()