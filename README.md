# Language Translator.AI

Language Translator.AI is a simple and efficient web application that allows users to translate text into different languages instantly. Built using Streamlit and LangChain, this app leverages the Ollama API to provide accurate translations.

## Features
- Translate text into various languages.
- Simple and user-friendly interface.
- Real-time translation using the Ollama model.
- Fast and efficient response time.

## Technologies Used
- **Streamlit**: For building the web interface.
- **LangChain**: For handling AI-based processing.
- **Ollama API**: Provides language model capabilities.
- **Python**: Core programming language.
- **dotenv**: To manage environment variables securely.

## Installation
To run this application locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/language-translator-ai.git
   ```
2. Navigate to the project directory:
   ```sh
   cd language-translator-ai
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Create a `.env` file and add your API keys:
   ```sh
   LANGCHAIN_API_KEY=your_api_key
   LANGCHAIN_PROJECT2=your_project_name
   ```

## Usage
Run the application with the following command:
```sh
streamlit run language_translator.py
```

### How to Use
1. Enter the text you want to translate in the input field.
2. Specify the target language (e.g., French, Spanish, German).
3. Click the "Translate" button.
4. View the translated text in the output field.

## Troubleshooting
- Ensure all required dependencies are installed.
- Verify that the `.env` file contains valid API keys.
- Restart the app if you encounter any errors.

## Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
**SM Imran Khan Biky**

---

Happy translating! 🌍✨