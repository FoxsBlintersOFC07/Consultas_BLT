import ast
import importlib

# Define o nome do arquivo do script
script_filename = "Consultas_BLT.py"

# Obtém o código-fonte do script
with open(script_filename, "r") as script_file:
    script_code = script_file.read()

# Analisa o código-fonte do script
ast_tree = ast.parse(script_code)

# Obtém uma lista com os nomes das dependências importadas no script
imports = [node.names[0].name for node in ast_tree.body if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)]

# Identifica quais dependências importadas não estão sendo utilizadas no script
unused_imports = [import_name for import_name in imports if not importlib.util.find_spec(import_name).loader.exec_module(ast.parse(script_code))]

# Imprime as dependências não utilizadas
if unused_imports:
    print("As seguintes dependências importadas não estão sendo utilizadas:")
    for import_name in unused_imports:
        print(import_name)
else:
    print("Todas as dependências importadas estão sendo utilizadas.")
