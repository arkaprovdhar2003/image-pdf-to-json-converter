import base64
import fitz
import io
import json

class Converter:
    def __init__(self):
        pass

    def convert_to_json(self, file_path):
        if file_path[:5] == b'%PDF-':
            doc = fitz.open(stream=io.BytesIO(file_path))
            json_data = []

            for page_number, page in enumerate(doc, start=1):
                pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,
                                      colorspace=fitz.csRGB, clip=None, alpha=True, annots=True)
                pix.save("image.png")  

                with open("image.png", "rb") as f:
                    image_bytes = f.read()

                encoded_image = base64.b64encode(image_bytes)
                json_data.append(encoded_image.decode('utf-8'))

            doc.close()
            return {'message': 'success', 'data': json.dumps(json_data)}

        elif file_path[:2] == b'\xFF\xD8':  
            img = io.BytesIO(file_path)
            img.seek(0)
            encoded_img = base64.b64encode(img.read())
            return {'message': 'success', 'data': encoded_img.decode('utf-8')}

        elif file_path[:8] == b'\x89PNG\r\n\x1a\n':  
            img = io.BytesIO(file_path)
            img.seek(0)
            encoded_img = base64.b64encode(img.read())
            return {'message': 'success', 'data': encoded_img.decode('utf-8')}

        return {'message': 'failed'}
