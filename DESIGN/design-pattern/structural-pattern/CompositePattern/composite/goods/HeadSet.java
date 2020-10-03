package composite.goods;

public class HeadSet implements Goods{
    private int price = 300;
    private String name;

    public HeadSet(String name) {
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
