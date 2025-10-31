import io

import pymupdf  # PyMuPDF library

# from PIL import Image


def single_image_to_pdf(image_bytes):
    new_pdf_doc = pymupdf.open()

    image_from_bytes = pymupdf.open(stream=image_bytes, filetype="png")

    image_dimentions = image_from_bytes[0].rect

    pdf_bytes = image_from_bytes.convert_to_pdf()
    image_from_bytes.close()

    image_pdf = pymupdf.open("pdf", pdf_bytes)

    page = new_pdf_doc.new_page(
        width=image_dimentions.width, height=image_dimentions.height
    )
    page.show_pdf_page(image_dimentions, image_pdf, 0)

    # Save to BytesIO
    output = io.BytesIO()
    output.write(new_pdf_doc.tobytes())
    output.seek(0)

    new_pdf_doc.close()
    return output
