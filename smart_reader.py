from pdf_reader import extract_text
from image_reader import extract_images
from image_captioner import generate_caption

def smart_extract(pdf_path):

    print("Reading PDF Text...")

    final_text = extract_text(pdf_path)

    print("Extracting Images...")

    images = extract_images(pdf_path)

    for image in images:

        caption = generate_caption(image)

        final_text += "\n\n"
        final_text += "[IMAGE CAPTION]\n"
        final_text += caption
        final_text += "\n"

    return final_text