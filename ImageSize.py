import os
import re

import PIL
from PIL.Image import Transpose

from rembg import remove

from cropImage import *

sizes = ["mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]
widths = [48, 72, 96, 144, 192]
heights = [48, 72, 96, 144, 192]

new_extension = ".png"
original_size = "OriginalSize"


def teorema_de_tales(A, B, C):
    return round(A * B / C)


def rename(root, file):
    file_name, extension = os.path.splitext(file)

    original = os.path.join(root, file)
    novo = os.path.join(root, file_name + new_extension)

    if not os.path.isdir(original):
        if not os.path.exists(novo):
            if os.path.exists(original):
                os.rename(original, novo)
                print("Arquivo " + file + " renomado para " + new_extension)



def format_image(root, file):
    original_image_path = os.path.join(root, file)
    new_image_path = os.path.join(root, original_size, file)

    pillow_image = Image.open(original_image_path)
    pillow_image = trim(remove(pillow_image)).transpose(Transpose.ROTATE_270)

    pillow_image.save(
        new_image_path,
        optimize=True,
        quality=50,
        exif=pillow_image.info.get('exif')
    )

    print("Saved Formated " + root, file)


def resize(root, new_folder, file, new_width, new_height):
    original_image_path = os.path.join(root, original_size, file)
    new_image_path = os.path.join(root, new_folder, file)

    pillow_image = Image.open(original_image_path)

    width, height = pillow_image.size

    if width > height:
        new_height = teorema_de_tales(new_height, height, width)
    else:
        new_width = teorema_de_tales(new_height, width, height)

    new_image = pillow_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    new_image.save(
        new_image_path,
        optimize=True,
        quality=50,
        exif=pillow_image.info.get('exif')
    )

    print("Saved Resized " + root, file)

def is_image(extension):
    extension_lowercase = extension.lower()
    return bool(re.search(r'^\.(jpe?g|png)$', extension_lowercase))


def file_checks(root, file):
    file_name, extension = os.path.splitext(file)

    if not is_image(extension):
        return

    format_image(root, file)

    for i in range(len(sizes)):
        resize(root, sizes[i], file, widths[i], heights[i])


# Em todas as pastas
def files_loop(root, files):
    for file in files:
        file_checks(root, file)


def folder_check(root):
    for size in sizes:
        if not os.path.exists(os.path.join(root, size)):
            os.mkdir(os.path.join(root, size))
            print("Pasta " + size + " criada")
    if not os.path.exists(os.path.join(root, original_size)):
        os.mkdir(os.path.join(root, original_size))
        print("Pasta " + original_size + " criada")


def main(root):
    folder_check(root)

    for file in os.listdir(root):
        rename(root, file)

    for file in os.listdir(root):
        file_checks(root, file)

    print("Finalizado")


if __name__ == "__main__":
    root_folder = "D:\Imagens\Teste"
    main(root_folder)
