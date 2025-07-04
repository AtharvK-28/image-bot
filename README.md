## Image Bot




  https://github.com/user-attachments/assets/39516788-a0f8-4cc4-ad8f-688f1744f5c6
  



This project is a Python-based bot that automatically searches for and downloads images of whatever you ask it for. It's designed to help automate image collection for offline use or machine learning datasets.

## Project Structure

```
image-bot
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
   cd image-bot
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

2. Follow the prompts to search for images of whatever you want and specify the folder where you want to save the images.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
