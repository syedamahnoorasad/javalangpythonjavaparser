import javalang

def extract(file):
    with open(file, 'r') as file:
        code_txt = file.read()

    tree = javalang.parse.parse(code_txt)
        
    for path, node in tree:
        if isinstance(node, javalang.tree.ClassDeclaration):
            print(node.name)
        elif isinstance(node, javalang.tree.MethodDeclaration):
            print(node.name)

extract('file.java')

