import fitz
import os

def extract_images(pdf_path):

    doc = fitz.open(pdf_path)

    output_folder = "pdf_images"
    os.makedirs(output_folder, exist_ok=True)

    image_paths = []

    for page_number in range(len(doc)):

        page = doc.load_page(page_number)

        images = page.get_images(full=True)

        for image_index, img in enumerate(images):

            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]

            extension = base_image["ext"]

            image_name = (
                f"page_{page_number+1}_img_{image_index+1}.{extension}"
            )

            image_path = os.path.join(
                output_folder,
                image_name
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    return image_paths