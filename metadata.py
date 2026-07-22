import os


def create_metadata(pdf_path, chunks):

    file_name = os.path.basename(pdf_path)

    metadata = []

    for i in range(len(chunks)):

        metadata.append(
            {
                "file_name": file_name,
                "page": "Unknown"
            }
        )

    return metadata