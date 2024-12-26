# Stress Detection

This project uses machine learning to detect stress levels based on physiological data.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the training script to train the model:
    ```bash
    python scripts/train_model.py
    ```
6. Start the Flask application:
    ```bash
    python app.py
    ```

## Usage

- Visit `http://127.0.0.1:5000/` to view the home page.
- Use the form on the Predict page to input data and predict stress levels.
- Visit the Visualize page to see the confusion matrix of the model's performance.
