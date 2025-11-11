# VaultSpell

A lightweight, high-performance utility for translating DOCX documents between languages with precision and efficiency.

## Overview

**VaultSpell** efficiently processes `.docx` files and converts their contents from one language to another.  
Built for reliability and speed, it leverages modern translation APIs while maintaining the original document layout.

## Features

- 🔄 **Automated Translation** – Translates DOCX documents between supported languages.  
- ⚡ **Efficient & Lightweight** – Optimized for fast execution and low memory usage.  
- 🧩 **Formatting Preservation** – Retains original document styles, paragraphs, and metadata.  
- 🛠️ **CLI Ready** – Simple, scriptable interface for automation or batch translation.  

## Setup
```shell
pip install -r require.txt
python main.py --help
```

## Usage

Run the application from the command line (example):

```bash
python main.py -i "sourceDocument.docx" -o "destDocument.docx" --langs ["ro", "en"]
