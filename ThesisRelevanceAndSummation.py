import gradio as gr
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BartTokenizer, BartForConditionalGeneration
import PyPDF2

# Initialize tokenizer and model for summarization
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def extract_text_from_pdf(file_path):
    # Extract text from the PDF file
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def calculate_relevance_score(title, content):
    from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_relevance_score(title, content):
    try:
        # Lowercase both title and content to avoid case sensitivity issues
        title = title.lower()
        content = content.lower()
        
        # Initialize TfidfVectorizer with parameters to improve matching
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))

        # Fit and transform the title and content
        tfidf_matrix = vectorizer.fit_transform([title, content])

        # Calculate the cosine similarity (dot product of normalized vectors)
        similarity = tfidf_matrix[0].dot(tfidf_matrix[1].T).toarray()[0][0]
        
        # Convert similarity to percentage
        relevance_percentage = similarity * 100
        
        return relevance_percentage


    except Exception as e:
        return f"Error calculating relevance score: {e}"
        


def summarize_text(text):
    try:
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=500, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error generating summary: {e}"

def process_file(file):
    try:
        # Extract the file path from the NamedString object and read the PDF content
        file_path = file.name
        content = extract_text_from_pdf(file_path)

        title = "Sample Thesis Title"  # Dummy title for relevance score calculation

        relevance_score = calculate_relevance_score(title, content)
        summary = summarize_text(content)

        return relevance_score, summary
    except Exception as e:
        return f"Error processing file: {e}", ""

# Define the Gradio interface
def gradio_interface(file):
    try:
        relevance_score, summary = process_file(file)
        return relevance_score, summary
    except Exception as e:
        return f"Error in Gradio interface: {e}", ""

# Create Gradio inputs and outputs
with gr.Blocks() as demo:
    gr.Markdown("## Upload a PDF File to Process")
    
    with gr.Row():
        file_input = gr.File(label="Upload your file")
        output_score = gr.Textbox(label="Relevance Score")
        output_summary = gr.Textbox(label="Summary")
    
    file_input.change(gradio_interface, inputs=file_input, outputs=[output_score, output_summary])

demo.launch()
