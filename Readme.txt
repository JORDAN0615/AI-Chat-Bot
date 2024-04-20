# Restaurant Recommender Chatbot using NLTK Module

## Overview:
This project is a restaurant recommendation chatbot built using the NLTK module in Python. The chatbot assists users in finding restaurants nearby Central University. Additionally, it can provide basic weather information upon inquiry. The primary functionalities of the chatbot include aiding decision-making during breakfast and lunch times.

## Requirements:
Before running the chatbot, ensure you have the following dependencies installed:
1. `numpy`
2. `nltk`
3. `torch`

You can install these dependencies using pip:
```bash
pip install numpy
pip install nltk
pip install torch
```

## Setup:
1. Run `nltk.download('punkt')` in `nltk_utils.py` to download the necessary NLTK data.
2. Train the chatbot by running `train.py`. This script utilizes the data stored in `intents.json` to tokenize words and train the model.

## Usage:
Once all dependencies are installed and the chatbot is trained, run `chat.py` to initiate the chatbot. Users can interact with the chatbot to receive restaurant recommendations and basic weather information. Additionally, the chatbot provides decision support during breakfast and lunch times.

## Notes:
- Ensure that your `intents.json` file contains relevant data for training the chatbot.
- Depending on your environment and preferences, you may need to modify the code to customize functionalities or integrate additional features.
- Feel free to experiment and extend the capabilities of the chatbot according to your requirements.

## Contributors:
- Jordan Tseng

## License:
This project is licensed under the [MIT License](LICENSE).
