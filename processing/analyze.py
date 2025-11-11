import pandas as pd

# --- Step C: Data Acquisition and Structuring ---

def load_lyrics_to_dataframe(file_path):
    """
    Reads a text file line by line and creates a Pandas DataFrame.
    """
    lines = []
    
    # 1. Open the file and read it line-by-line (safely)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 2. Clean up each line: remove leading/trailing whitespace and make lowercase
                cleaned_line = line.strip().lower()
                
                # 3. Only keep lines that aren't empty (removes blank lines between stanzas)
                if cleaned_line:
                    lines.append(cleaned_line)
                    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    # 4. Create the main DataFrame
    df = pd.DataFrame(lines, columns=['Lyric_Text'])
    
    # 5. Add a unique ID for tracking
    df['Lyric_ID'] = df.index + 1
    
    print(f"Successfully loaded {len(df)} lines of lyrics.")
    return df

# --- Execution ---

# Set the path to your lyrics file
lyrics_file = 'data/lyrics/folklore_evermore_lyrics.txt' 

# Load the data
lyric_df = load_lyrics_to_dataframe(lyrics_file)

if lyric_df is not None:
    # Display the first few rows to confirm it worked
    print("\n--- Initial DataFrame Structure ---")
    print(lyric_df.head(10))