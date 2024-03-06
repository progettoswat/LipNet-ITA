import os

phrases = ['Salve quanto costa quell articolo',
           'E in offerta costa dieci euro',
           'Perfetto vorrei comprarne due',
           'Certo ecco a lei vuole un sacchetto',
           'Si grazie e arrivederci',
           'Le auguro una buona giornata',
           'Buongiorno io sono Mario',
           'Buonasera io sono Mario',
           'Piacere luigi come stai',
           'Tutto bene tu',
           'Tutto bene grazie',
           'Prendiamo un caffe al bar',
           'Certo volentieri io lo prendero macchiato',
           'A che ora arriva il pullman',
           'Dovrebbe arrivare tra qualche minuto',
           'Quanto costa il biglietto',
           'Purtroppo non lo so pero potresti chiedere all autista',
           'Va bene grazie lo stesso',
           'Prego',
           'Buongiorno a che ora inizia lo spettacolo',
           'Lo spettacolo inizia a mezzanotte',
           'Dove posso acquistare i biglietti',
           'Puoi acquistare i biglietti online o al botteghino',
           'Salve posso prendere il suo ordine',
           'Vorrei una pizza margherita per favore',
           'Vuole qualcosa da bere',
           'Una coca cola grazie',
           'Quanto tempo ci vorra per preparare la pizza',
           'Circa venti minuti di attesa',
           'Va bene aspettero',
           'Ecco la sua pizza margherita buon appetito',
           'Qual e la tua esperienza nel settore',
           'Ho lavorato per due anni come consulente informatico',
           'Perche vuoi lavorare qui',
           'Ammiro la vostra cultura aziendale',
           'Cosa hai fatto di interessante ultimamente',
           'Ho fatto una gita in montagna',
           'Hai qualche piano per il fine settimana',
           'Penso di andare al concerto',
           'Hai visto l ultimo film uscito',
           'No non ancora Vogliamo andare insieme',
           'Si volentieri',
           'Che bello fare una passeggiata qui',
           'Si l aria fresca fa bene',
           'Vogliamo sederci su quella panchina',
           'Si sembra un bel posto per riposare',
           'Guarda quei bambini giocare con il pallone',
           'Si sembrano divertirsi un sacco',
           'Dobbiamo portare dell acqua la prossima volta',
           'Hai ragione fa davvero caldo oggi',
           'Qual e il numero dell autobus per l aereoporto',
           'L autobus e il numero trentacinque',
           'Dove stai andando di bello',
           'Sto partendo per gli Stati Uniti',
           'Se avessi piu soldi partirei anche io',
           'Magari potremmo andare insieme in futuro'
           ]


def write_file(file, index):
    if file is not None:
        splitted_phrases = phrases[int(index)].split()
        file.write("sil\n")
        for word in splitted_phrases:
            file.write(word + "\n")
        file.write("sil")


if __name__ == '__main__':
    main_path = input("Enter dataset path:")
    main_path = main_path + "/"
    os.chdir(main_path)

    for dir in os.listdir(os.getcwd()):
        # dir s*
        os.chdir(dir)
        print("\nFOLDER: " + dir)
        for video in os.listdir(os.getcwd()):
            if ".txt" not in video:
                print("-->PROCESSING: " + video)
                index = ""
                dash = video.rfind("-")

                index = video[0:(dash)]

                with open(video[:-4] + ".txt", 'w+') as file_name:
                    write_file(file_name, index)

        os.chdir("..")
    os.chdir("..")
