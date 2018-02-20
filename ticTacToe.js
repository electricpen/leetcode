class TicTacToe {
  constructor(props) {
    this.players = ["player1", "player2"];
    this.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]];
    this.turn = this.players[0];
  }

  draw() {
    let stringifiedBoard = [];
    for (row in this.board) {
      stringifiedBoard.push(row.join("|"));
    }
    stringifiedBoard.join("\n-----");
    console.log(stringifiedBoard);
  }

  getMove() {}

  start() {}
}

//------------------- TESTS ----------------------
let game = new TicTacToe();
game.draw();
