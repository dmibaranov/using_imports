import ast
import sys


def main(filename):
    imports = []
    with open(filename, 'rt') as file_obj:
        source = file_obj.read()

    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.Import) or isinstance(n, ast.ImportFrom):
            imports += [nm.name for nm in n.names]

    print(imports)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raise SystemExit('Missed filename to check')
