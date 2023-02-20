"""This program uses spaCy to calculate the semantic similarity between a Hulk movie description and a list of movie 
descriptions stored in a text file. The program reads in the movie descriptions from the text file, calculates the similarity 
scores using spaCy's similarity function, and stores the scores in a dictionary with the movie titles as keys. 
The program then returns the title of the movie with the highest similarity score."""

import spacy
nlp = spacy.load('en_core_web_md')

def recommend_movie(hulk_movie):
    """
    This function takes in a user's movie description and returns the title of the most
    similar movie from a list of movies stored in a text file."""

    with open('movies.txt', 'r') as file:
        movie_descriptions = file.readlines()
    # Create a list of movie titles, with each title consisting of "Movie " followed by a letter of the alphabet.
    movie_titles = [f"Movie {chr(i+65)}" for i in range(len(movie_descriptions))]

    # Create an empty dictionary to store the similarity scores for each movie.
    movie_scores = {}

    # Loop through the movie descriptions, and for each description:
    for i, description in enumerate(movie_descriptions):
        # Use spaCy to process the description and convert it into a document object.
        doc = nlp(description)

        # Calculate the similarity score between the user's movie description and the current movie description.
        score = hulk_movie.similarity(doc)

        # Add the movie title and similarity score to the dictionary.
        movie_scores[movie_titles[i]] = score

    # Determine the title of the movie with the highest similarity score.
    recommended_movie = max(movie_scores, key=movie_scores.get)

    # Return the title of the most similar movie.
    return recommended_movie

if __name__ == '__main__':
    # Define the user's movie description
    hulk_movie = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

    # Call the recommend_movie function to get the most similar movie title
    recommended_movie = recommend_movie(hulk_movie)

    # Print the recommended movie title
    print("The most similar film appears to be:", recommended_movie)
    
