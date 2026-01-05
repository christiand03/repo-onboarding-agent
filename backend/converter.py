import logging
import nbformat
import base64
from nbformat.reader import NotJSONError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def wrap_cdata(content):
    """Wraps content in CDATA tags."""
    return f"<![CDATA[\n{content}\n]]>"

def extract_output_content(outputs, image_list):
    """
    Extracts text and handles images by decoding Base64 to bytes.
    Returns: A list of text strings or placeholders.
    """
    extracted_xml_snippets = []
    
    for output in outputs:

        if output.output_type in ('display_data', 'execute_result') and hasattr(output, 'data'):
            data = output.data
            
            # Helper to process image
            def process_image(mime_type):
                if mime_type in data:
                    try:
                        b64_str = data[mime_type]
                        b64_str = b64_str.replace('\n', '')

                        image_index = len(image_list)
                        image_list.append({
                            "mime_type": mime_type,
                            "data": b64_str
                        })

                        return f'\n<IMAGE_PLACEHOLDER index="{image_index}" mime="{mime_type}"/>\n'
                    except Exception as e:
                        return f"<ERROR>Could not decode image: {e}</ERROR>"
                return None

            # Ignore jpeg if png is found
            img_xml = process_image('image/png')
            if not img_xml:
                img_xml = process_image('image/jpeg')
            
            if img_xml:
                extracted_xml_snippets.append(img_xml)
            elif 'text/plain' in data:
                extracted_xml_snippets.append(data['text/plain'])

        elif output.output_type == 'stream':
            extracted_xml_snippets.append(output.text)
            
        elif output.output_type == 'error':
            extracted_xml_snippets.append(f"{output.ename}: {output.evalue}")

    return extracted_xml_snippets

def convert_notebook_to_xml(file_content):
    try:
        nb = nbformat.reads(file_content, as_version=4)
    except NotJSONError:
        return "<ERROR>Could not parse file as JSON/Notebook</ERROR>", []

    xml_parts = []
    extracted_images = [] 

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            cell_xml = f'<CELL type="markdown">\n{cell.source}\n</CELL>'
            xml_parts.append(cell_xml)

        elif cell.cell_type == 'code':
            source_code = wrap_cdata(cell.source)
            xml_parts.append(f'<CELL type="code">\n{source_code}\n</CELL>')

            if hasattr(cell, 'outputs') and cell.outputs:
                snippets = extract_output_content(cell.outputs, extracted_images)
                
                content = "\n".join(snippets)
                
                if content.strip():
                    wrapped_output = wrap_cdata(content)
                    xml_parts.append(f'<CELL type="output">\n{wrapped_output}\n</CELL>')

    return "\n\n".join(xml_parts), extracted_images


def process_repo_notebooks(repo_files):
    notebook_files = [f for f in repo_files if f.path.endswith('.ipynb')]
    logging.info(f"Found {len(notebook_files)} notebooks.")
        
    results = {}

    for nb_file in notebook_files:
        logging.info(f"Processing: {nb_file.path}")

        xml_output, images = convert_notebook_to_xml(nb_file.content)
        results[nb_file.path] = {
            "xml": xml_output,
            "images": images
        }
            
    return results