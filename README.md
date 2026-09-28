# BookBot

BookBot is a lightweight command-line tool that analyzes plain-text books. It
reports the total word count and the frequency of each alphabetic character,
sorted from most common to least common.

This project was built as part of the [Boot.dev](https://www.boot.dev) backend
development curriculum.

## Features

- Read any UTF-8 text file
- Count total words
- Count characters without case sensitivity
- Sort character frequencies in descending order
- Print a clear, human-readable report

## Requirements

- Python 3.8 or newer
- A plain-text book or document to analyze

BookBot uses only Python's standard library, so no package installation is
required.

## Quick Start

1. Clone the repository and open its directory:

	```bash
	git clone https://github.com/LogicKatanaX/BookBot.git
	cd BookBot
	```

2. Run BookBot with the path to a text file:

	```bash
	python main.py path/to/book.txt
	```

On macOS or Linux, use `python3` if `python` is not mapped to Python 3.

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

## Project Structure

```text
.
├── main.py       # Command-line entry point and report formatting
├── stats.py      # Text loading, counting, and sorting helpers
└── README.md     # Project documentation
```

## Development

Run the application directly from the repository root:

```bash
python main.py path/to/book.txt
```

There are no third-party dependencies or build steps. Text files placed in a
local `books/` directory are ignored by Git so that large source texts are not
committed accidentally.

## License

This project is provided for educational purposes.
