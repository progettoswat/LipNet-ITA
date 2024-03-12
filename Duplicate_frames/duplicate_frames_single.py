import os
import shutil
import sys


def duplica_ultimo_file(cartella_origine, limite_file=100):
    # Ottieni la lista dei file ordinati per data di modifica
    lista_file = sorted(os.listdir(cartella_origine), key=lambda x: os.path.getmtime(os.path.join(cartella_origine, x)))

    if not lista_file:
        print("La cartella di origine è vuota.")
        return

    # Verifica il numero totale di file nella cartella di destinazione
    numero_file_totali = len(os.listdir(cartella_origine))

    if numero_file_totali >= limite_file:
        print(f"La cartella di origine ha già raggiunto il limite di {limite_file} file.")
        return

    # Prendi l'ultimo file dalla lista
    ultimo_file = lista_file[-1]

    # Estrarre il nome e l'estensione del file
    nome_file, estensione = os.path.splitext(ultimo_file)

    # Estrai il numero dal nome del file (considerando che il numero è alla fine del nome)
    numero_attuale = int(nome_file.split('_')[-1])

    # Calcola il nuovo numero
    nuovo_numero = numero_attuale + 1

    # Costruisci il nuovo nome del file
    nuovo_nome = f"{nome_file.split('_')[0]}_{nuovo_numero:03d}{estensione}"

    # Costruisci il percorso completo del file di origine
    percorso_file_origine = os.path.join(cartella_origine, ultimo_file)

    # Costruisci il percorso completo del file di destinazione
    percorso_file_destinazione = os.path.join(cartella_origine, nuovo_nome)

    # Copia il file nella cartella di destinazione
    shutil.copy2(percorso_file_origine, percorso_file_destinazione)

    print(f"File duplicato con successo: {nuovo_nome}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <percorso_cartella_origine>")
        sys.exit(1)

    cartella_origine = sys.argv[1]

    duplica_ultimo_file(cartella_origine, limite_file=100)
