package composite.goods;

public class Water implements Goods{
    private int price = 200;
    private String name;

    public Water(String name) {
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
