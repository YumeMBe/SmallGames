
class Scrabble:

    def __init__(self, letters, points, player_to_words):
        self.letters = letters
        self.points = points
        self.letter_to_points = {key: value for key, value in zip(letters, points)}
        self.player_to_words = player_to_words
        for key in letters:
            self.letter_to_points[key.lower()] = self.letter_to_points[key]


    def score_word(self, word):
        point_total = 0
        for letter in word:
            if letter not in self.letter_to_points.keys():
                point_total += 0
            else:
                point_total += self.letter_to_points.get(letter, 0)
        return point_total



    def play_word(self,player, word):  # add word to a list of words of player
        if player in self.player_to_words.keys():
            self.player_to_words[player].append(word)
        else:
            self.player_to_words[player] = [word]


    def update_point_totals(self):  # mapping of players to how many points they’ve scored.
        for player, words in self.player_to_words.items():
            player_points = 0
            for word in words:
                player_points += self.score_word(word)
            player_to_points[player] = player_points
        return player_to_points


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                       "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

scrabble = Scrabble(letters, points, player_to_words)
brownie_points = scrabble.score_word("brownie")
print(brownie_points)

player_to_points = {}

scrabble.play_word("Mada", "pula")
scrabble.play_word("Mada", "variabila")
print(scrabble.player_to_words)
print(scrabble.update_point_totals())
