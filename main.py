import argparse as args
from vault.utils import VaultCore


if __name__ == "__main__":
    parser = args.ArgumentParser(description='Small tool that translate docx documents.')
    parser.add_argument("-i", "--input", help="The input file containing the original document.")

    parser.add_argument("-langs", "--langs", help="List of languages used for translation.", nargs="*")
    parser.add_argument("-o", "--output", help="The output file that contains the generated document.")

    args = parser.parse_args()
    src = args.input

    dest = args.output
    langs = args.langs
    VaultCore.CreateDocument(src, dest, langs)
