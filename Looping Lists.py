genres = ["Jazz - Pretty settle", "Rock - The hardcore and rough", "Hip-hop - Nice and cool ", "Classical - Open and historical"]
track_number = 1
i = 0
for genre in genres:
    print(f" Track {track_number}:Now playing {genre}") 
    track_number += 1

#Lesson 2
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

track_number = 1
playing = True

while track_number <= len(genres) and playing:
    genre = genres[track_number - 1]
    print(f"Track {track_number}: Now playing {genre}")
    
    if genre == "Hip-hop":
        print("Sorry, I don't like Hip-hop. Stopping the playlist.")
        playing = False
    
    track_number += 1
    
    #lesson 3
    genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for track_number in range(len(genres)):
    genre = genres[track_number]
    if genre == "Hip-hop":
        print(f"Skipping {genre}, not suitable for the light show.")
        continue
    print(f"Track {track_number + 1}: Light show is ready for {genre}.")

