import argparse as args
from vault.utils import VaultCore
import VaultConfigFactory as vf


if __name__ == "__main__":
    parser = args.ArgumentParser(description='A lightweight, high-performance utility for translating DOCX documents between languages with precision and efficiency.')
    parser.add_argument("-i", "--input", help="The input file containing the original document.", required=True)
    parser.add_argument("-langs", "--langs", help="List of languages used for translation.", nargs="*", required=True)
    parser.add_argument("-o", "--output", help="The output file that contains the generated document.", required=True)

    args = parser.parse_args()
    src = args.input
    dest = args.output
    langs = args.langs

    if len(langs) != 2:
        print("Error: Please provide exactly two language codes (source and destination)")
        exit(1)

    configFactory = vf.VaultConfigFactory()
    VaultCore.CreateDocument(configFactory, src, dest, langs)
