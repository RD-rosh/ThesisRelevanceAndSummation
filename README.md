# ThesisRelevanceAndSummation

# PDF Relevance and Summarization Tool

This tool allows you to upload a PDF file and automatically calculate the relevance score of the document based on a predefined title and generate a summary of the document using the BART transformer model.

## Features

- **Relevance Score Calculation**: Computes a relevance score between a predefined title and the content of the PDF using TF-IDF vectorization. The score is presented as a percentage.
- **Text Summarization**: Summarizes the content of the uploaded PDF using the BART model from Hugging Face’s transformers library.
- **User-Friendly Interface**: Gradio provides an easy-to-use interface for uploading PDFs and viewing the results.

## How It Works

1. **Upload PDF**: You upload a PDF file.
2. **Text Extraction**: The tool extracts text from the PDF file.
3. **Relevance Score Calculation**: The relevance score is calculated based on the similarity between a predefined title ("Sample Thesis Title") and the content of the PDF.
4. **Text Summarization**: The content of the PDF is summarized using the BART model.
5. **Output**: The relevance score and summary are displayed in the interface.

## Dependencies

- Python 3.x
- Gradio
- scikit-learn
- transformers (Hugging Face)
- PyPDF2

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/pdf-relevance-summarization.git
    cd pdf-relevance-summarization
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` doesn’t exist yet, you can create it:
    ```bash
    pip install gradio scikit-learn transformers PyPDF2
    pip freeze > requirements.txt
    ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Access the interface**:
   - Once the server is running, a Gradio interface will open in your web browser.
   - Upload a PDF file, and the tool will process it to display the relevance score and summary.

## Example

Here’s an example of what the interface looks like:

![Example Screenshot]
![image](https://github.com/user-attachments/assets/dfd57504-4589-414e-97b4-cc926f6b7a07)

![image](https://github.com/user-attachments/assets/7d063897-c792-4af0-bce4-0942a70eb657)

![image](https://github.com/user-attachments/assets/7cccfcf8-b2ad-4aeb-8d00-7d0dbedcb6b1)




## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or bug reports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
