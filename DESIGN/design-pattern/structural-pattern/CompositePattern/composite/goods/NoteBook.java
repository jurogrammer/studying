package composite.goods;

public class NoteBook implements Goods {
    private int price = 5000;
    private String name;

    public NoteBook(int price) {
        this.price = price;
    }

    public NoteBook(String name) {
        this.name = name;
    }

    @Override
    public int getPrice() {
        return this.price;
    }

    @Override
    public String getName() {
        return this.name;
    }
}
