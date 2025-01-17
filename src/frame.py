class Frame:
    __SCORE_BY_PINS = {
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "X" : 10,
        "/" : 10,
        "-" : 0
    }
    __STRIKE = "X"
    __SPARE = "/"

    def calculate_frame_score(self) -> int:
        first_roll = self.frame[0]
        if len(self.frame) == 1:
            return self.__SCORE_BY_PINS[first_roll]
        second_roll = self.frame[1]
        return self.__SCORE_BY_PINS[first_roll] + self.__SCORE_BY_PINS[second_roll]


    def __init__(self, frame: str):
        self.frame = repr(frame).replace("'", "")
    
    def __str__(self):
        return f"Este frame es: |{self.frame[0]}, {self.frame[1]}|"
    
    def __repr__(self):
        return f"{self.frame}"



if __name__ == "__main__":

    frame_ejemplo = Frame("1-")

    print(frame_ejemplo)
    print(frame_ejemplo.calculate_frame_score())
    print(repr(frame_ejemplo))
