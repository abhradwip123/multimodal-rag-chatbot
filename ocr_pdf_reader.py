import os

from pdf2image import convert_from_path

from config import POPPLER_PATH
from ocr_reader import image_to_text


def extract_text_from_scanned_pdf(pdf_path):

    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    pages = []

    for i, image in enumerate(images, start=1):

        image_path = f"temp_page_{i}.png"

        image.save(image_path)

        text = image_to_text(image_path)

        os.remove(image_path)

        pages.append(
            {
                "page": i,
                "text": text
            }
        )

    return pages