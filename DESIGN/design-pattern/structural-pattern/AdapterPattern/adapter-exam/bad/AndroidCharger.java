package adapter.bad;

public class AndroidCharger {

    public void charge(String chargeType) {
        if ("AndroidType".equals(chargeType)){
            System.out.println("충전 중입니다.");
        } else {
            System.out.println("타입이 일치하지 않아 충전되지 않습니다.");
        }
    }
}