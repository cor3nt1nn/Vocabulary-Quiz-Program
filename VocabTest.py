import csv
import random

def read_csv(filename):
    words = []
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            words.append((line[0].strip(), line[1].strip(), int(line[2])))
    return words

def write_csv(filename, words):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['English', 'French', 'Errors'])
        for en, fr, erreurs in words:
            writer.writerow([en, fr, erreurs])

def quiz(words, sens):
    questions = []

    if sens == 'francais-vers-anglais':
        questions = [(fr, en, 'français', 'anglais', erreurs, index) for index, (en, fr, erreurs) in enumerate(words)]
    elif sens == 'anglais-vers-francais':
        questions = [(en, fr, 'anglais', 'français', erreurs, index) for index, (en, fr, erreurs) in enumerate(words)]
    elif sens == 'mixte':
        for index, (en, fr, erreurs) in enumerate(words):
            if random.choice([True, False]):
                questions.append((en, fr, 'anglais', 'français', erreurs, index))
            else:
                questions.append((fr, en, 'français', 'anglais', erreurs, index))
    
    random.shuffle(questions)
    
    score = 0
    for question, reponse, _, reponse_lang, erreurs, index in questions:
        user_reponse = input(f"Traduire '{question}' en {reponse_lang} : ").strip().lower()
        if user_reponse == reponse.lower():
            print("\033[32mCorrect!\033[0m")
            score += 1
            erreurs = max(0, erreurs - 1)
        else:
            print(f"\033[31mFAUX! La bonne réponse était '{reponse}'.\033[0m")
            validation = input("Votre réponse est-elle tout de même correcte (par ex., erreur mineure, accent) ? (y/n) : ").strip().lower()
            if validation == 'y':
                print("\033[32mRéponse acceptée !\033[0m")
                score += 1
                erreurs = max(0, erreurs - 1)
            else:
                erreurs += 1

        words[index] = (words[index][0], words[index][1], erreurs)
    
    print(f"\nQuiz terminé! Votre score: {score}/{len(questions)}")
    return words

def mode_selector():
    choix = input("1: Traduire de l'anglais vers le français\n2: Traduire du français vers l'anglais\n3: Mélanger les deux\nChoisissez votre mode (1, 2 ou 3) : ")
    if choix == '1':
        return 'anglais-vers-francais'
    elif choix == '2':
        return 'francais-vers-anglais'
    elif choix == '3':
        return 'mixte'
    else:
        print("Choix non valide. Veuillez réessayer.")
        return mode_selector()

def words_selection(mots, taille):
    total_erreurs = sum(erreurs for _, _, erreurs in mots)
    if total_erreurs == 0:
        print("Aucune erreur enregistrée, tirage égalitaire.")
        return random.sample(mots, taille)
    else:
        print("Tirage pondéré selon le nombre d'erreurs.")
        mots_pondere = random.choices(mots, weights=[1 + erreurs for _, _, erreurs in mots], k=taille)
        return mots_pondere

def main():
    filename = input("Entrez le nom du fichier CSV (ex: 'mots.csv') : ")
    words = read_csv(filename)
    
    mode = mode_selector()
    tout_ou_alea = input("Voulez-vous faire toutes les questions ('t') ou une sélection aléatoire ('a') ? ")
    
    if tout_ou_alea == 'a':
        nb_questions = int(input(f"Combien de mots voulez-vous tester ? (max {len(words)}) "))
        words = words_selection(words, nb_questions)
    
    words = quiz(words, mode)
    
    write_csv(filename, words)

if __name__ == "__main__":
    main()
