# Chess AI Project

## Overview

This project is a Python-based chess engine that uses Pygame for the game interface and NumPy for efficient computations. The engine is designed to play strategically across different phases of the game, incorporating both opening theory and endgame techniques.

## Features

- **Custom Evaluation Functions**: 
  - Tailored evaluation functions for different phases of the game (opening, midgame, and endgame).
  - Adaptive strategy that considers positional play and material balance.

- **Opening Theory Integration**: 
  - Implemented a database of common chess openings.
  - AI selects moves from the opening book for a strong early-game strategy.

- **Endgame Techniques**:
  - Integrated endgame heuristics and tablebases to improve decision-making in the later stages of the game.
  - Optimized move selection for critical endgame positions.

## Installation

To run the Chess AI locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tushitshukla03/Chess.git
   cd Chess

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    
3. **Run the game**:
   ```bash
   ./run_game.sh
