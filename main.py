from antlr4 import *
from AnatomyLexer import AnatomyLexer
from AnatomyParser import AnatomyParser
from AnatomyVisitor import AnatomyVisitor
from EvalVisitor import EvalVisitor
import sys

sys.setrecursionlimit(5000)

def main():
    input_file = None
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if not input_file.endswith('.ds'):
            print("Error: el archivo debe tener la extensión .ds")
            return

    try:
        if input_file:
            input_stream = FileStream(input_file)
        else:
            input_stream = InputStream(input("Ingrese el código: "))

        lexer = AnatomyLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = AnatomyParser(tokens)
        tree = parser.program()  # parse

        visitor = EvalVisitor()
        visitor.visit(tree)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
