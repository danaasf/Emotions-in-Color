import pandas as pd
import string
import re

# --- Step C: Data Acquisition and Structuring (from previous step) ---

def load_lyrics_to_dataframe(file_path):
    # ... (Keep this function exactly the same as before) ...
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                cleaned_line = line.strip().lower()
                if cleaned_line:
                    lines.append(cleaned_line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    df = pd.DataFrame(lines, columns=['Lyric_Text'])
    df['Lyric_ID'] = df.index + 1
    print(f"Successfully loaded {len(df)} lines of lyrics.")
    return df

# ----------------------------------------------------------------------
# --- NEW Step D: Data Cleaning and Preprocessing ---

def clean_lyrics(df):
    """
    Applies standard NLP cleaning steps to the raw lyric text.
    """
    
    # Create a copy of the raw text before cleaning (good practice)
    df['Clean_Lyric_Text'] = df['Lyric_Text'].copy()

    # 1. Remove text inside parentheses (e.g., [Verse 1], (Ah-ha))
    df['Clean_Lyric_Text'] = df['Clean_Lyric_Text'].apply(
        lambda text: re.sub(r'\(.*?\)|\[.*?\]', '', text)
    )

    # 2. Remove all punctuation
    # Create a translation map to remove all characters defined in string.punctuation
    translator = str.maketrans('', '', string.punctuation)
    df['Clean_Lyric_Text'] = df['Clean_Lyric_Text'].apply(
        lambda text: text.translate(translator)
    )
    
    # 3. Remove extra whitespace and strip leading/trailing spaces
    df['Clean_Lyric_Text'] = df['Clean_Lyric_Text'].apply(
        lambda text: ' '.join(text.split())
    )
    
    # 4. Filter out any lines that became empty after cleaning (e.g., lines that only contained [Chorus])
    df = df[df['Clean_Lyric_Text'].str.len() > 0].reset_index(drop=True)
    df['Lyric_ID'] = df.index + 1 # Re-index the IDs after filtering

    return df

# --- Execution ---

# Set the path to your lyrics file
lyrics_file = 'data/lyrics/folklore_evermore_lyrics.txt' 

# Load the data
lyric_df = load_lyrics_to_dataframe(lyrics_file)

if lyric_df is not None:
    # Clean the data
    cleaned_df = clean_lyrics(lyric_df)
    
    # Display the result (comparing raw vs. clean)
    print("\n--- Cleaned DataFrame (Comparison) ---")
    print(cleaned_df[['Lyric_Text', 'Clean_Lyric_Text']].head(10)) 

    # We will use this 'cleaned_df' for the next step: Emotion Analysis
    # We can save it as a CSV here for safety:
    cleaned_df.to_csv('cleaned_taylor_swift_lyrics.csv', index=False, encoding='utf-8')
    print("\nData saved to 'cleaned_taylor_swift_lyrics.csv'")