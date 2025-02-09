# CodeTantraBot

CodeTantraBot is a Selenium automation tool designed to handle almost every answer for CodeTantra Learning & Practical questions. **Note:** The bot only injects the correct answer into the field; it does **not** submit it automatically.

## Features

- **Automated Answer Injection:** Automatically fills in the correct answer for CodeTantra questions.
- **Controlled Submission:** Only injects the answer—submission is left to you.
- **Supports Two Modes:** Works for both CodeTantra Learning and CodeTantra Practical questions.

## Requirements

- **Python 3.x**
- **Selenium**
- **Firefox Browser** (with [Geckodriver](https://github.com/mozilla/geckodriver) installed)

## Installation

Follow these steps to set up and run CodeTantraBot:

1. **Clone the Repository:**

   Open your terminal and run:
   ```bash
   git clone https://github.com/ai-man-codes/CodeTantraBot.git
   pip install -r requirements.txt
   ```

2. **Install Dependencies:**

   Navigate to the desired directory depending on whether you want to use the Learning or Practical version, and then install the dependencies.

   For the **Learning** version:
   ```bash
   cd CodeTantraBot-Learning
   ```

   For the **Practical** version:
   ```bash
   cd CodeTantraBot-Practical
   ```

3. **Run the Bot:**

   Start the bot by running:
   ```bash
   python bot.py
   ```

## Reset

If you need to reset everything back to normal, simply run:
```bash
python reset.py
```

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

Enjoy using CodeTantraBot!