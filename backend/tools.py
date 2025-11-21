import re
from graphviz import Source
import logging
import os


def render_graphviz_diagrams(markdown_text, output_base_dir):

    pattern = r"```dot(.*?)```"
    
    assets_dir = os.path.join(output_base_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    def replace_match(match):
        dot_code = match.group(1).strip()
        filename = "repository_structure"
        
        try:
            s = Source(dot_code)
            rendered_path = s.render(filename=filename, directory=assets_dir, format='png', cleanup=True)
            
            logging.info(f"Graphviz diagram rendered to: {rendered_path}")
            
            relative_link = f"./assets/{filename}.png"
            
            return f"![Repository Structure]({relative_link})"
        except Exception as e:
            logging.error(f"FAILED to render Graphviz diagram. Error: {e}")
            return f"```dot\n{dot_code}\n```"

    processed_text = re.sub(pattern, replace_match, markdown_text, flags=re.DOTALL)
    return processed_text