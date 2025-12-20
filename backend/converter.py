import logging
import nbformat
from nbformat.reader import NotJSONError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def wrap_cdata(content):
    """Wraps content in CDATA tags."""
    return f"<![CDATA[\n{content}\n]]>"

def extract_output_text(outputs):
    """
    Extracts text representation from cell outputs.
    Prioritizes stream (stdout) and text/plain data.
    """
    output_text = []
    
    for output in outputs:
        # Handle print statements (stdout/stderr)
        if output.output_type == 'stream':
            output_text.append(output.text)
            
        # Handle calculated results (e.g. df.head())
        elif output.output_type == 'execute_result':
            data = output.data
            if 'text/plain' in data:
                output_text.append(data['text/plain'])
                
        # Handle errors
        elif output.output_type == 'error':
            output_text.append(f"{output.ename}: {output.evalue}")

    return "\n".join(output_text)

def convert_notebook_to_xml(file_content):
    """
    Parses a raw notebook string and converts it to the specific XML format.
    """
    try:
        nb = nbformat.reads(file_content, as_version=4)
    except NotJSONError:
        return "<ERROR>Could not parse file as JSON/Notebook</ERROR>"

    xml_parts = []

    for cell in nb.cells:
        cell_xml = ""
        
        if cell.cell_type == 'markdown':
            cell_xml = f'<CELL type="markdown">\n{cell.source}\n</CELL>'
            xml_parts.append(cell_xml)

        elif cell.cell_type == 'code':
            source_code = wrap_cdata(cell.source)
            xml_parts.append(f'<CELL type="code">\n{source_code}\n</CELL>')

            if hasattr(cell, 'outputs') and cell.outputs:
                out_text = extract_output_text(cell.outputs)
                if out_text.strip():
                    wrapped_output = wrap_cdata(out_text)
                    xml_parts.append(f'<CELL type="output">\n{wrapped_output}\n</CELL>')

    return "\n\n".join(xml_parts)


def process_repo_notebooks(repo_files):
        
    # Filter for Jupyter Notebooks
    notebook_files = [f for f in repo_files if f.path.endswith('.ipynb')]
    logging.info(f"Found {len(notebook_files)} notebooks.")
        
    results = {}

    for nb_file in notebook_files:
        logging.info(f"Processing: {nb_file.path}")
            
        raw_content = nb_file.content
        xml_output = convert_notebook_to_xml(raw_content)
            
        results[nb_file.path] = xml_output
            
    return results