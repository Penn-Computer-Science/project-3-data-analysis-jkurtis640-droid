
import pandas as pd
import random

music_genres = ["Medieval/Renaissance","Baroque","Classical","Romantic","Ragtime","Jazz","Soul","Gospel","Rock","Pop","Funk","Rap","Country"]
math_problem_answers = ["A. 2","B. 4","C. 8","D. 16"]
time_playing_videogames = ["12.00","4.00","8.30","10.00","2.00","6.07"]
time_listening_music = ["12.15","1.00","5.00","6.07","9.00","9.00"]
combination_problem = ["I have no clue, so I will just give you one thing that fits into each category. 2020's Christian rock, (2+/- (121-4*12*-14)^(1/2))/24, first person shooter","jazz pi platformer","The Alpha","Make a puzzle game (Maybe... a cool math game!? [Say that again...])","Rock (DOOM soundtrack), Calculus 2 Washer Method, hard platforming?"]

id = []
for i in range(30):
    id.append(i)



data = {
    "Music Genres": [random.choice(music_genres) for _ in id],
    "Math Answers": [random.choice(math_problem_answers) for _ in id],
    "Hours playing videogames": [random.choice(time_playing_videogames) for _ in id],
    "Time listening music": [random.choice(time_listening_music) for _ in id],
    "Combination Problem": [random.choice(combination_problem) for _ in id]
}

not_pandas_data = pd.DataFrame(data)
not_pandas_data.to_csv("notpandas.csv", index=False)