#!/usr/bin/env python
import ast
import sys


class ImportNodesVisitor(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        super(ImportNodesVisitor, self).__init__(*args, **kwargs)
        self.imports = []

    def _extract_imports(self, node):
        self.imports += [n.name for n in node.names]
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self._extract_imports(node)

    def visit_Import(self, node):
        self._extract_imports(node)


def main(filename):
    with open(filename, 'rt') as file_obj:
        source = file_obj.read()

    im_visitor = ImportNodesVisitor()
    im_visitor.visit(ast.parse(source))
    print(set(im_visitor.imports))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raise SystemExit('Missed filename to check')
