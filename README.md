# Text Adventure Game (Year 11)

A Python-based text adventure game originally written in Year 11. This project uses console-based colored text (via the Colorama library) and Windows-specific input handling (using msvcrt) to create an interactive adventure experience. Please note that much of the original code was removed for brevity.

## Overview
In this adventure, you play as a brave explorer on a quest to collect ancient runes and defeat the evil Colossus. As you journey through diverse locations—from treacherous lava caverns to mysterious city ruins—you must manage your health, keep track of your inventory, and make crucial decisions that determine your fate.

## Features
- Interactive Gameplay: Navigate through various environments and face dynamic challenges.
- Inventory & Health Management: Keep track of your items and health. Use food and healing items wisely.
- Multiple Locations: Explore areas like the Lava Caverns, Ocean, Abandoned City, and more.
- Dynamic Encounters: Experience random events such as battles with fire elementals or helpful interactions with fellow adventurers.
- Colored Text Output: Enjoy enhanced console visuals using Colorama for colored messaging.
- Responsive Input: Uses msvcrt for immediate key input, creating a fluid text-based interaction.

## Getting Started

### Prerequisites
- Python 3.x
- Colorama Library (install using: pip install colorama)

Note: This game relies on the msvcrt module, which is available only on Windows.

### Installation & Running
1. Clone or download the repository.
2. Install the required package by running: pip install colorama
3. Run the game from your console by executing: python text_adventure.py

## How to Play
- Movement: Use commands such as N (North), E (East), S (South), and W (West) to move around.
- Inventory Management:
  - Type INV to view the contents of your backpack.
  - Use DROP to remove an item from your inventory.
- Health Check: Type HEALTH to display your current health.
- Item Usage: Type USE to consume an item that can restore health.
- Other Commands:
  - HOME: Get directions back to your home base.
  - MAP: View a representation of the game map.
  - HELP: Display a list of all available commands.

As you progress, additional commands and options will become available.

## Additional Notes
- Code Trimming: This version of the code is a trimmed-down version of my original project. Many features were removed to meet size constraints.
- Legacy Code: Being an early project from Year 11, the code reflects my initial programming efforts and may not follow current best practices.
- Platform Limitation: The game is designed to run on Windows due to the use of the msvcrt module.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
- Colorama: For providing easy-to-use colored terminal output.
- msvcrt: For immediate keyboard input handling on Windows.
- Inspired by classic text adventure games and developed as part of a school project.
