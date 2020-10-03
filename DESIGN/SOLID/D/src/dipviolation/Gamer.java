package dipviolation;

public class Gamer {
    private Bishop bishop;
    private Knight knight;

    public Gamer(Bishop bishop, Knight knight) {
        this.bishop = bishop;
        this.knight = knight;
    }

    public void movePiece(String piece) {
        if (piece.equals("bishop")) {
            bishop.move();
        } else {
            knight.move();
        }
    }
}
