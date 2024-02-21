import os

phrases = ['Hello, i m John',
           'You re welcome',
           'Thank you and goodbye',
           'Yeah sure i want it too creamy',
           'How much it cost the ticket'
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
    main_path = main_path+"/"
    os.chdir(main_path)

    for dir in os.listdir(os.getcwd()):
        # dir s*
        os.chdir(dir)
        print("\nFOLDER: "+dir)
        for video in os.listdir(os.getcwd()):
            if ".txt" not in video:
                print("-->PROCESSING: "+video)
                index = ""
                dash = video.rfind("-")

                index = video[0:(dash)]

                with open(video[:-4] + ".txt", 'w+') as file_name:
                    write_file(file_name, index)

        os.chdir("..")
    os.chdir("..")
