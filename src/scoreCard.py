from src.frame import Frame

class ScoreCard:

    __INITIAL_GAME_SCORE = 0

    def __init__(self, game: str):
        self.game_score = self.__INITIAL_GAME_SCORE
        self.game = game

    def __repr__(self) -> str:
        return f"Tu carta es: {' , '.join(self.__stylizer())}"
    


    def calculate_score(self) -> int:
        game = self.__stylizer()
        for position, frame in enumerate(game[:10]):
            frame = Frame(frame)
            if frame.is_strike():
                self.__calculate_strike(game, frame, position)
            elif frame.is_spare():
                self.__calculate_spare(game, frame, position)
            else:
                self.game_score += frame.calculate_frame_score()
        return self.game_score



    
    def __stylizer(self) -> list:
        pins = []
        game = self.game.replace("X", "XX")

        if len(game) == 21:
            game += "-"
        for position in range(1, len(game), 2):
            roll = game[position]
            if Frame(roll).is_strike():
                pins.append(roll)
                continue
            pins.append(game[position - 1] + roll)
        return pins
    
    def __calculate_strike(self, game: list, frame: str, position: int) -> None:
        self.__calculate_spare(game, frame, position)
        next_frame = Frame(game[position + 1])
        if next_frame.is_strike():
            second_frame_next_roll = Frame(game[position + 2][0])
            self.game_score += second_frame_next_roll.calculate_frame_score()
            return None
        second_roll = Frame(game[position + 1][1])
        self.game_score += second_roll.calculate_frame_score()
        if next_frame.is_spare():
            next_roll = Frame(game[position + 1][0])
            self.game_score -= next_roll.calculate_frame_score()
            return None


    def __calculate_spare(self, game: list, frame: str, position: int) -> None:
        next_roll = game[position + 1][0]
        self.game_score += ( Frame(frame).calculate_frame_score() + Frame(next_roll).calculate_frame_score())


if __name__ == "__main__":
    from frame import Frame

    card1 = ScoreCard("8/549-XX5/53639/1/X")
    card2 = ScoreCard("5/5/5/5/5/5/5/5/5/5/5")

    print(card1)
    print(card1.calculate_score())

    print(card2)
    print(card2.calculate_score())