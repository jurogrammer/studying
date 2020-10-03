package composite.goods;

public class Pencil implements Goods {
    private int price = 100;
    private String name;

    public Pencil(String name) {
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
