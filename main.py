import argparse as args
import os
import sys
import re

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vault.utils import VaultCore
import VaultConfigFactory as vcf


def parse_languages(lang_arg):
    """Parse language arguments from various formats"""
    if not lang_arg:
        return None
        
    # If it's a list, use as is
    if isinstance(lang_arg, list) and len(lang_arg) >= 2:
        return lang_arg[:2]
    
    # Handle string formats
    if isinstance(lang_arg, str):
        # Remove brackets and quotes, then split
        clean_str = re.sub(r'[\[\]"\' ]', '', lang_arg)
        parts = clean_str.split(',')
        if len(parts) >= 2:
            return parts[:2]
    
    # If we have multiple arguments
    if len(lang_arg) >= 2:
        # Clean each argument
        cleaned = []
        for lang in lang_arg:
            if isinstance(lang, str):
                clean_lang = re.sub(r'[\[\]"\' ]', '', lang)
                if clean_lang:
                    cleaned.append(clean_lang)
        if len(cleaned) >= 2:
            return cleaned[:2]
    
    return None


if __name__ == "__main__":
    parser = args.ArgumentParser(description='A lightweight, high-performance utility for translating DOCX documents between languages with precision and efficiency.')
    parser.add_argument("-i", "--input", help="The input file containing the original document.", required=True)
    parser.add_argument("-langs", "--langs", nargs='+', help="List of languages used for translation. Example: -langs ro en or -langs \"ro\" \"en\"", required=True)
    parser.add_argument("-o", "--output", help="The output file that contains the generated document.", required=True)

    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' does not exist.")
        sys.exit(-1)
        
    # Validate output directory exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        print(f"Error: Output directory '{output_dir}' does not exist.")
        sys.exit(-1)

    # Parse languages
    langs = parse_languages(args.langs)
    
    if not langs or len(langs) != 2:
        print(f"Error: Please provide exactly two language codes (source and destination)")
        sys.exit(-1)

    try:
        configFactory = vcf.VaultConfigFactory()
        VaultCore.CreateDocument(configFactory, args.input, args.output, langs)
        print("Translation completed successfully!")
    except Exception as e:
        print(f"Translation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(-2)