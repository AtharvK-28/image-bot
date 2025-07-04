# Virat Kohli Image Bot

This project is an AI model that searches for images of the famous cricketer Virat Kohli, downloads them, and stores them in a designated folder. It utilizes web scraping techniques to gather image URLs and then downloads the images for offline use.

## Project Structure

```
virat-kohli-image-bot
├── src
│   ├── main.py          # Entry point of the application
│   ├── image_search.py  # Contains the ImageSearch class for searching images
│   ├── downloader.py    # Contains the ImageDownloader class for downloading images
│   └── utils.py         # Utility functions for common tasks
├── requirements.txt     # Lists the project dependencies
├── .gitignore           # Specifies files to be ignored by Git
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd virat-kohli-image-bot
   ```

2. **Install the required dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python src/main.py
   ```

2. Follow the prompts to search for images of Virat Kohli and specify the folder where you want to save the images.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.