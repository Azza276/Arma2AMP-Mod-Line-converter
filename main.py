import modlinegen
import modlinegen_name_semi
import modlinegen_semi
import os

def process_file(file_path, workshop_mod_line, mod_id_line, mod_name_line):
    try:
        if workshop_mod_line:
            generated_text = modlinegen.generate_mod_line(file_path)
            save_file(generated_text, file_path, "_ws")
        if mod_id_line:
            generated_text = modlinegen_semi.generate_modlinegen_semi(file_path)
            save_file(generated_text, file_path, "_semi")
        if mod_name_line:
            generated_text = modlinegen_name_semi.generate_modlinegen_name_semi(file_path)
            save_file(generated_text, file_path, "_name_semi")
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the file: {e}")

def save_file(content, original_file_path, suffix):
    try:
        base_name = os.path.splitext(os.path.basename(original_file_path))[0]
        save_path = os.path.join(os.path.dirname(original_file_path), f"{base_name}{suffix}.txt")
        with open(save_path, 'w') as file:
            file.write(content)
    except Exception as e:
        raise RuntimeError(f"An error occurred while saving the file: {e}")
