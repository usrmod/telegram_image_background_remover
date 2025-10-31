import io

from rembg import remove


def rem_image(bytes):
    output_bytes = remove(bytes)

    otuput_image = io.BytesIO(output_bytes)
    otuput_image.seek(0)

    return otuput_image
