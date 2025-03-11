import streamlit as st
import re
from collections import Counter
import pandas as pd

def count_words(text):
    # Split text into words and count them
    words = text.split()
    return len(words)

def count_characters(text):
    # Count all characters including spaces
    return len(text)

def count_characters_no_spaces(text):
    # Count characters excluding spaces
    return len(text.replace(" ", ""))

def find_numbers(text):
    # Find all numbers in the text using regex
    return re.findall(r'\d+', text)

def get_word_frequencies(text):
    # Clean text and get word frequencies
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

# Set up the Streamlit page
st.title("📝 Advanced Text Analyzer")
st.write("This tool demonstrates various Python concepts including data types, operators, keywords, string casting, and string methods.")

# Text input section
text_input = st.text_area("Enter your text here:", height=200)

if text_input:
    st.markdown("### Basic Analysis")
    
    # Create columns for basic metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Word Count", count_words(text_input))
    with col2:
        st.metric("Characters (with spaces)", count_characters(text_input))
    with col3:
        st.metric("Characters (no spaces)", count_characters_no_spaces(text_input))

    # String Methods Demonstration
    st.markdown("### String Operations")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Uppercase Text:")
        st.info(text_input.upper())
        
        st.write("First Character Capitalized:")
        st.info(text_input.capitalize())
        
    with col2:
        st.write("Lowercase Text:")
        st.info(text_input.lower())
        
        st.write("Title Case:")
        st.info(text_input.title())

    # Number Analysis
    st.markdown("### Number Analysis")
    numbers = find_numbers(text_input)
    if numbers:
        total = sum(map(int, numbers))
        st.write(f"Numbers found in text: {numbers}")
        st.write(f"Sum of numbers: {total}")
        st.write(f"Average of numbers: {total/len(numbers):.2f}")
    else:
        st.write("No numbers found in the text.")

    # Word Frequency Analysis
    st.markdown("### Word Frequency Analysis")
    word_freq = get_word_frequencies(text_input)
    
    # Display top 10 most common words
    st.write("Top 10 Most Common Words:")
    freq_df = pd.DataFrame(word_freq.most_common(10), columns=['Word', 'Frequency'])
    st.table(freq_df)

    # Additional Text Statistics
    st.markdown("### Additional Statistics")
    col1, col2 = st.columns(2)
    
    with col1:
        # Count sentences (rough estimation)
        sentences = len(re.split(r'[.!?]+', text_input.strip()))
        st.metric("Approximate Sentence Count", sentences)
        
        # Count paragraphs
        paragraphs = len([p for p in text_input.split('\n\n') if p.strip()])
        st.metric("Paragraph Count", paragraphs)
        
    with col2:
        # Average word length
        words = text_input.split()
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        st.metric("Average Word Length", f"{avg_word_length:.2f}")
        
        # Unique words count
        unique_words = len(set(words))
        st.metric("Unique Words", unique_words)

    # Text Type Conversion Demo
    st.markdown("### Type Conversion Examples")
    st.code("""
# Original text type
type_of_text = type(text_input)  # str

# Converting to list of characters
list_of_chars = list(text_input)

# Converting to list of words
list_of_words = text_input.split()

# Converting numbers to integers (if found)
numbers_as_ints = [int(num) for num in find_numbers(text_input)]
    """)

# Add sidebar with explanation
st.sidebar.title("About This Tool")
st.sidebar.write("""
This text analyzer demonstrates:

1. **Data Types**:
   - Strings (text input)
   - Lists (word lists)
   - Integers (counts)
   - Floats (averages)

2. **Operators**:
   - Arithmetic (+, /, len())
   - Comparison (if/else)
   - Assignment (=)

3. **Keywords**:
   - if/else
   - for
   - in
   - def

4. **String Methods**:
   - upper()
   - lower()
   - split()
   - replace()
   - capitalize()
   - title()

5. **Type Casting**:
   - str to list
   - str to int
   - list operations
""") 