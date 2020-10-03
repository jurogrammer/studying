package composite.goods;

import java.util.ArrayList;
import java.util.List;

//composite에 해당
public class Box implements Goods {
    private String name;
    private List<Goods> innerGoods = new ArrayList<>();

    public Box(String name) {
        this.name = name;
    }
    @Override
    public int getPrice() {
        int totalPrice = 0;
        for (Goods goods : innerGoods) {
            //값을 계산하는 것을 서브 엘레먼트에게 위임합니다.
            totalPrice += goods.getPrice();
        }

        return totalPrice;
    }

    public void addItems(Goods goods) {
        innerGoods.add(goods);
    }

    public String getName() {
        return this.name;
    }

    public List<Goods> getGoodsList() {
        return this.innerGoods;
    }
}
