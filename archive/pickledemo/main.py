from datetime import datetime
import os
import pickle


class GamerProfile:
    def __init__(
        self,
        username: str,
        current_level: int,
        last_saved_on: datetime
    ) -> None:
        self.username = username
        self.current_level = current_level
        self.last_saved_on = last_saved_on

    def increment_level(self):
        self.current_level += 1

    def print_info(self):
        print(
            f"""
            Username: {self.username}
            Current Level: {self.current_level}
            Last Saved Time: {self.last_saved_on}
            """
        )


class Game:
    def __init__(self, profile_filepath: str = "./gamesave.bin") -> None:
        self.profile_filepath = profile_filepath
        self.gamer_profile = None
        self._initialize_gamer_profile()

    def _initialize_gamer_profile(self):
        if os.path.exists(self.profile_filepath):
            self.gamer_profile = self._load_profile()
        else:
            self.gamer_profile = GamerProfile(
                username=input("Enter your username: "),
                current_level=0,
                last_saved_on=datetime.now()
            )

    def _load_profile(self):
        with open(self.profile_filepath, "rb") as data:
            return pickle.load(data)

    def save_profile(self):
        with open(self.profile_filepath, "wb") as data:
            pickle.dump(self.gamer_profile, data)

    def update_gamer_profile(self):
        self.gamer_profile.increment_level()

    def show_profile_data(self):
        self.gamer_profile.print_info()


g = Game()
g.show_profile_data()
g.update_gamer_profile()
g.update_gamer_profile()
g.show_profile_data()
g.save_profile()
