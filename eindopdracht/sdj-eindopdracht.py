import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel,
    QPushButton, QGridLayout
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from bs4 import BeautifulSoup
from io import BytesIO

# URL for scraping Pokémon sprites
HOME_SPRITES_URL = "https://pokemondb.net/sprites"

class PokedexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokédex")
        self.setFixedSize(320, 480)

        # Updated style sheet for the window and buttons.
        # Margin is set to 0 on the QPushButton to let the grid spacing control horizontal spacing.
        self.setStyleSheet(
            """
            /* Main window: purple bg + rounded corners */
            QWidget {
                background-color: #D8BCEC;
                border-radius: 20px;
            }
            /* Scroll area: white background with 25% opacity */
            QScrollArea {
                border: none;
                background-color: rgba(255, 255, 255, 0.25);
            }
            /* Buttons: semi-transparent white background, slightly rounded corners, zero margin */
            QPushButton {
                background-color: rgba(255, 255, 255, 0.5);
                border: none;
                border-radius: 5px;
                margin: 0px;
                padding: 0px;
            }
            """
        )

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.container = QWidget()
        self.container.setContentsMargins(0, 0, 0, 0)
        self.container_layout = QVBoxLayout()
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        self.container.setLayout(self.container_layout)

        self.main_layout.addWidget(self.container)
        self.setLayout(self.main_layout)

        # Scrape Pokémon data
        self.pokemon_data = self.scrape_pokemon_list()
        self.loaded_pokemon = 0
        self.pokemon_buttons = []

        # Create scrollable Pokedex view
        self.create_pokedex_view()
        self.container_layout.addWidget(self.scroll_area)

        # Load initial batch of Pokémon
        self.display_pokemon(initial_load=True)

    def create_pokedex_view(self):
        """Sets up the scrollable area and grid layout for the Pokémon list."""
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Keep vertical scrolling functional but hide the scrollbar
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll_widget = QWidget()
        self.grid_layout = QGridLayout()

        # 2 px margins on the left/right edges + 4 px spacing between columns
        # ensures five 60px buttons fit within 320px width
        self.grid_layout.setContentsMargins(2, 0, 2, 0)
        self.grid_layout.setSpacing(4)

        self.scroll_widget.setLayout(self.grid_layout)
        self.scroll_area.setWidget(self.scroll_widget)

        # Connect the scrollbar for loading more Pokémon near the bottom
        self.scroll_area.verticalScrollBar().valueChanged.connect(self.load_more_pokemon)

    def scrape_pokemon_list(self):
        """
        Scrapes Pokémon from https://pokemondb.net/sprites.
        The page displays Pokémon cards with class '.infocard'.
        The Pokémon name is extracted from a '.ent-name' element if available,
        or from the image's alt attribute otherwise.
        """
        response = requests.get(HOME_SPRITES_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        infocards = soup.select('.infocard')
        if not infocards:
            raise ValueError("No Pokémon cards found on the sprites page. Site structure may have changed.")

        pokemon_list = []
        for card in infocards:
            name_el = card.select_one('.ent-name')
            if name_el:
                name = name_el.text.strip()
            else:
                img_tag = card.select_one('img')
                if img_tag and 'alt' in img_tag.attrs:
                    name = img_tag['alt'].strip()
                else:
                    continue

            img_tag = card.select_one('img')
            if not img_tag:
                continue
            img_url = img_tag.get('src', '')

            pokemon_list.append({
                "name": name,
                "img_url": img_url
            })

        return pokemon_list

    def display_pokemon(self, initial_load=False):
        """
        Lazy-load: 50 Pokémon initially, then 10 each time we scroll near the bottom.
        5 per row, each button is 60x60.
        """
        button_size = 60
        load_amount = 50 if initial_load else 10
        count = 0

        while self.loaded_pokemon < len(self.pokemon_data) and count < load_amount:
            row, col = divmod(self.loaded_pokemon, 5)
            pokemon = self.pokemon_data[self.loaded_pokemon]

            btn = QPushButton()
            btn.setFixedSize(button_size, button_size)
            btn.clicked.connect(lambda _, p=pokemon: self.show_pokemon_details(p))

            # Fetch the Pokémon image
            img_data = requests.get(pokemon["img_url"]).content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)

            icon = QIcon(pixmap)
            # Icon is 52x52, leaving a 4px margin on each side within the button
            btn.setIconSize(QSize(button_size - 8, button_size - 8))
            btn.setIcon(icon)

            self.grid_layout.addWidget(btn, row, col)
            self.pokemon_buttons.append(btn)
            self.loaded_pokemon += 1
            count += 1

        # Adjust the scroll area height so all loaded buttons are visible
        self.scroll_widget.setMinimumHeight((self.loaded_pokemon // 5 + 1) * button_size)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.verticalScrollBar().setSingleStep(10)

    def load_more_pokemon(self):
        scrollbar = self.scroll_area.verticalScrollBar()
        if scrollbar.value() >= scrollbar.maximum() - 50:
            self.display_pokemon()

    def show_pokemon_details(self, pokemon):
        self.scroll_area.hide()
        self.details_widget = QWidget()
        self.details_widget.setStyleSheet("background: transparent;")
        self.details_layout = QVBoxLayout(self.details_widget)
        self.details_layout.setContentsMargins(0, 0, 0, 0)

        img_data = requests.get(pokemon["img_url"]).content
        pixmap = QPixmap()
        pixmap.loadFromData(img_data)

        img_label = QLabel()
        img_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        img_label.setAlignment(Qt.AlignCenter)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_pokedex)

        self.details_layout.addWidget(img_label)
        self.details_layout.addWidget(back_button)
        self.container_layout.addWidget(self.details_widget)

    def show_pokedex(self):
        if hasattr(self, 'details_widget'):
            self.details_widget.hide()
            self.container_layout.removeWidget(self.details_widget)
            self.details_widget.deleteLater()
        self.scroll_area.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokedexApp()
    window.show()
    sys.exit(app.exec_())
