import webbrowser
from backend import *
import sys
try:
    from textual.app import App, ComposeResult
    from textual.containers import VerticalGroup, VerticalScroll,HorizontalGroup
    from textual.widgets import Button, Footer, Header,Input,Label
except ImportError:
    print("failed to import package: textual\nto fix the issue enter this command in the terminal: pip install textual")
    input("press enter to exit")
    sys.exit()

class Search_horizontal(HorizontalGroup):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        try:
            if event.button.id == "search_anime":
                search_movie(format_text(search_input_text), "database/hits-anime.txt")
            if event.button.id == "search_movie" and search_input_text != "":
                search_movie(format_text(search_input_text), "database/hits.txt")
        except NameError:
            pass

    def compose(self) -> ComposeResult: # type: ignore
        yield Button("Search anime",id="search_anime",variant="success")
        yield Button("Search movie",id="search_movie",variant="success")
        yield Input(
            placeholder="Movie name",
        )
    #@on(Input.Changed)
    def on_input_changed(self, event: Input.Changed) -> None:
        global search_input_text
        search_input_text = event.value.strip()  # Store the input text globally for use in button actions

class Buttons(VerticalGroup):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id=="author":
                webbrowser.open("https://github.com/DarkBlud")

            
    def compose(self) -> ComposeResult: # type: ignore
        yield VerticalGroup(Search_horizontal())
        yield Button("Author",id="author",variant="default")
        yield Label("Dont worry if the app looks stuck after pressing any button \nthe results may take a while to appear please be patient \nresults will appear in the results.txt file",id="author_label")

class Moviejavan_premium(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]


    def compose(self) -> ComposeResult: # type: ignore
        yield VerticalGroup(Buttons())
        yield Header()
        yield Footer()
        

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    menu = Moviejavan_premium()
    menu.run()