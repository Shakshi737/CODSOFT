# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on genre and description using TF-IDF and cosine similarity.

## Features
- **Content-Based Filtering**: Recommends movies based on similarity of content (genre + description).
- **TF-IDF Vectorization**: Converts text features into numerical vectors.
- **Cosine Similarity**: Measures similarity between movies.
- **Error Handling**: Gracefully handles invalid movie names.

## How to Run
1. Navigate to the `RecommendationSystem` directory.
2. Run the script:
   ```bash
   python recommender.py
   ```

## How It Works
1. **Dataset**: Contains 20 movies with title, genre, and description.
2. **Feature Engineering**: Combines genre and description into a single "tags" column.
3. **Vectorization**: Uses TF-IDF to convert text into numerical features.
4. **Similarity**: Computes cosine similarity between all movies.
5. **Recommendation**: Returns top N most similar movies to the input.

## Example Usage
```python
recommend("Inception", n=5)
# Output: ['Shutter Island', 'Interstellar', 'The Matrix', 'Source Code', 'The Prestige']
```

## Dependencies
- pandas
- scikit-learn

Install with: `pip install pandas scikit-learn`

## Author
Created by Shakshi Kumari for CODSOFT Internship.
