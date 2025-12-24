# WhatsApp Automation Tool

This is a Python script that automates the process of responding to WhatsApp messages using the OpenAI API.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/whatsapp-automation.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Set up the environment variables:
   - Create a `.env` file in the project directory.
   - Add the following line to the file, replacing `YOUR_API_KEY` with your actual OpenAI API key:
     ```
     API_KEY=YOUR_API_KEY
     ```

## Usage

1. Run the script:
```
python program.py
```
2. The script will automatically switch to the target window, select the text, copy it, and then generate a response using the OpenAI API.
3. The response will be automatically pasted and sent as a message.

## API

The script uses the OpenAI API to generate the responses. The `OpenAI` class is used to interact with the API, and the `chat.completions.create` method is used to generate the response.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
