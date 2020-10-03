package composite.goods;

public class Client {
    public static void main(String[] args) {
        Goods box1 = MakeComposite.getComposite();

        System.out.println("");
        System.out.println("=========box1의 가격==========");
        System.out.println("이름 : " + box1.getName() + ", 가격 :" + box1.getPrice());

        System.out.println("");
        System.out.println("=======box1내 개개 물건들의 가격========");
        for(Goods goods : ((Box) box1).getGoodsList()) {
            System.out.println("이름 : " + goods.getName() + ", 가격 : " + goods.getPrice());
        }
    }
}