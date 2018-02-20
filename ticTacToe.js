class TicTacToe {
  constructor(props) {
    this.x = " X ";
    this.o = " O ";
    this.n = "   ";
    this.players = ["player1", "player2"];
    this.board = [
      [this.n, this.n, this.n],
      [this.n, this.n, this.n],
      [this.n, this.n, this.n]
    ];
    this.turn = this.players[0];
  }

  draw() {
    let stringifiedBoard = [];
    this.board.forEach(row => {
      stringifiedBoard.push(row.join("|"));
    });
    stringifiedBoard = stringifiedBoard.join("\n-----------\n");
    console.log(stringifiedBoard);
  }

  getMove() {}

  start() {}
}

//------------------- TESTS ----------------------
let game = new TicTacToe();
game.draw();
