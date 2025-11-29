import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =============================================================================
# 1. CREATE MOVIE DATASET
# =============================================================================
# This is a small dataset of 20 movies with their genres and descriptions.
# In a real-world scenario, this would be loaded from a CSV file.

movies_data = {
    'title': [
        'Inception', 'Interstellar', 'The Matrix', 'Shutter Island', 'The Prestige',
        'The Dark Knight', 'Memento', 'The Avengers', 'Iron Man', 'Thor',
        'The Notebook', 'Titanic', 'La La Land', 'A Star is Born', 'The Fault in Our Stars',
        'The Conjuring', 'Insidious', 'A Quiet Place', 'Get Out', 'Hereditary'
    ],
    'genre': [
        'Sci-Fi Thriller', 'Sci-Fi Drama', 'Sci-Fi Action', 'Psychological Thriller', 'Mystery Thriller',
        'Action Crime', 'Psychological Thriller', 'Action Superhero', 'Action Superhero', 'Action Fantasy',
        'Romance Drama', 'Romance Drama', 'Musical Romance', 'Musical Drama', 'Romance Drama',
        'Horror Supernatural', 'Horror Supernatural', 'Horror Thriller', 'Horror Thriller', 'Horror Drama'
    ],
    'description': [
        'A thief who steals corporate secrets through dream-sharing technology',
        'A team of explorers travel through a wormhole in space',
        'A computer hacker learns about the true nature of reality',
        'A U.S. Marshal investigates the disappearance of a patient',
        'Two magicians engage in a competitive rivalry',
        'Batman fights against the Joker in Gotham City',
        'A man with short-term memory loss hunts for his wife\'s killer',
        'Earth\'s mightiest heroes must stop an alien invasion',
        'A billionaire builds a powered suit of armor to fight evil',
        'The Norse god of thunder protects Earth from threats',
        'A poor young man falls in love with a rich young woman',
        'A seventeen-year-old aristocrat falls in love with a poor artist',
        'An aspiring actress and a jazz musician fall in love',
        'A musician helps a young singer find fame',
        'Two teenagers with cancer fall in love',
        'Paranormal investigators help a family terrorized by a dark presence',
        'A family is haunted by malevolent spirits',
        'A family must live in silence to avoid mysterious creatures',
        'A young man uncovers disturbing secrets during a weekend getaway',
        'A family is haunted after the death of their secretive grandmother'
    ]
}

# Create DataFrame
movies_df = pd.DataFrame(movies_data)

# =============================================================================
# 2. FEATURE ENGINEERING
# =============================================================================
# Combine 'genre' and 'description' into a single 'tags' column.
# This will be used to compute similarity between movies.

movies_df['tags'] = movies_df['genre'] + ' ' + movies_df['description']

# =============================================================================
# 3. TF-IDF VECTORIZATION
# =============================================================================
# TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical vectors.
# It gives more weight to important words and less to common words.

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['tags'])

# =============================================================================
# 4. COMPUTE COSINE SIMILARITY
# =============================================================================
# Cosine similarity measures how similar two vectors are.
# Values range from 0 (not similar) to 1 (identical).

similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# =============================================================================
# 5. RECOMMENDATION FUNCTION
# =============================================================================

def recommend(movie_name, n=5):
    """
    Recommends movies similar to the given movie.
    
    Parameters:
    - movie_name (str): The name of the movie to base recommendations on.
    - n (int): Number of recommendations to return (default: 5).
    
    Returns:
    - list: A list of recommended movie titles.
    """
    
    # Handle empty input
    if not movie_name or not movie_name.strip():
        return "Error: Please provide a movie name."
    
    # Convert to title case for better matching
    movie_name = movie_name.strip().title()
    
    # Check if movie exists in dataset
    if movie_name not in movies_df['title'].values:
        return f"Error: '{movie_name}' not found in the database. Please check the spelling."
    
    # Get the index of the movie
    movie_idx = movies_df[movies_df['title'] == movie_name].index[0]
    
    # Get similarity scores for this movie with all other movies
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
    
    # Sort movies by similarity score (descending order)
    # Skip the first one because it's the movie itself (similarity = 1.0)
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    
    # Get movie indices
    movie_indices = [i[0] for i in similarity_scores]
    
    # Return the top N most similar movies
    recommended_movies = movies_df['title'].iloc[movie_indices].tolist()
    
    return recommended_movies

# =============================================================================
# 6. MAIN PROGRAM
# =============================================================================

def main():
    """
    Main function to run the recommendation system.
    """
    print("=" * 60)
    print("       MOVIE RECOMMENDATION SYSTEM")
    print("=" * 60)
    print("\nAvailable movies in the database:")
    print("-" * 60)
    
    for idx, movie in enumerate(movies_df['title'], 1):
        print(f"{idx}. {movie}")
    
    print("\n" + "=" * 60)
    
    while True:
        movie_input = input("\nEnter a movie name (or 'exit' to quit): ").strip()
        
        if movie_input.lower() in ['exit', 'quit']:
            print("Thank you for using the Movie Recommendation System!")
            break
        
        if not movie_input:
            print("Please enter a valid movie name.")
            continue
        
        recommendations = recommend(movie_input, n=5)
        
        if isinstance(recommendations, str):
            # Error message
            print(recommendations)
        else:
            print(f"\nMovies similar to '{movie_input.title()}':")
            print("-" * 60)
            for idx, movie in enumerate(recommendations, 1):
                print(f"{idx}. {movie}")

if __name__ == "__main__":
    main()
