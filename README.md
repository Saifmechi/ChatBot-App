# Chatbot Project : fastAPI +openai GPT3


  This project implements a simple chatbot using FastAPI and OpenAI's GPT-3 model.

## Video Demo

![image](https://github.com/Saifmechi/ChatBot-App/blob/main/Capture%20d'%C3%A9cran%202023-11-30%20131716.png)

<iframe width="560" height="315" src="https://drive.google.com/file/d/1xwIYIgbaZPPAYV5xaFXMiDJ7y8HEnrv-/view?usp=drive_link" frameborder="0" allowfullscreen></iframe>




## Project Structure

The project consists of the following files:

- **main.py**: Contains the FastAPI application and WebSocket handling.
- **chatbot.py**: Implements the chatbot functionality using the GPT-2 model.
- **requirements.txt**: Lists the dependencies required for the project.
- **venv/**: Virtual environment directory containing project dependencies.
- **README.md**: Documentation file (you're reading it!).

## Project Description

The Chatbot Project leverages the power of FastAPI and OpenAI's GPT-3 model to create a responsive and interactive chatbot. It allows users to have dynamic conversations with the chatbot, which generates intelligent responses based on the input it receives.

## Getting Started

Follow these steps to run the chatbot:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/chatbot-project.git
    cd chatbot-project
    ```

2. **Create Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
   **Openai Key** ;
     put your openai key in the chatbot.py file .

6. **Run the FastAPI Application**:
    ```bash
    uvicorn main:app --reload
    ```

7. **Access the Chatbot UI**:
    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to interact with the chatbot.

## Dependencies

- FastAPI
- Uvicorn
- OpenAI 
- Other dependencies listed in `requirements.txt`

## Author

Saif Mechi

## License

This project is licensed under the [MIT License](LICENSE).
