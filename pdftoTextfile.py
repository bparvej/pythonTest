import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Initialize an empty string to store the text
        text = ''
        
        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page object
            page = pdf_reader.pages[page_num]
            
            # Extract text from the page
            text += page.extract_text()
    
    return text

def save_text_to_file(text, output_file):
    # Open the output text file in write mode
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        # Write the extracted text to the file
        txt_file.write(text)

def main():
    # PDF file path (change this to your PDF file's path)
    pdf_file_path = 'example.pdf'
    
    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(pdf_file_path)
    
    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(pdf_file_path))[0]
    
    # Define the output text file path (same directory as PDF file)
    output_text_file = f'{base_filename}.txt'
    
    # Save the extracted text to a text file
    save_text_to_file(extracted_text, output_text_file)
    
    print(f'Text extracted from PDF and saved to {output_text_file}.')

if __name__ == '__main__':
    main()
