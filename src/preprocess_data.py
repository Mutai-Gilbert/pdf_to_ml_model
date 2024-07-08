import pandas as pd
import sys

def preprocess_text_to_dataframe(text):
    # Example preprocessing (this will depend on your specific report format)
    # Let's assume the text contains lines with "feature1, feature2, label"
    lines = text.split('\n')
    data = []
    for line in lines:
        parts = line.split(',')
        if len(parts) == 3:
            data.append({'feature1': float(parts[0]), 'feature2': float(parts[1]), 'label': int(parts[2])})

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python preprocess_data.py <path_to_text_file>")
        sys.exit(1)
    
    text_file_path = sys.argv[1]
    with open(text_file_path, 'r') as file:
        text = file.read()
    
    df = preprocess_text_to_dataframe(text)
    print(df)
