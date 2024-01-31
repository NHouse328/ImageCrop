import os


def main(root_folder):
    for file in os.listdir(root_folder):
        file_name, extension = os.path.splitext(file)

        original = os.path.join(root_folder, file)
        novo = os.path.join(root_folder, file_name + ".png")

        if not os.path.exists(novo):
            os.rename(original, novo)

    print("Finalizado")


if __name__ == "__main__":
    root_folder = "D:\Imagens\Quarto Gaveta 01"
    main(root_folder)
