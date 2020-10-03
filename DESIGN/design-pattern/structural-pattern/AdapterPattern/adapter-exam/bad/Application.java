package adapter.bad;

public class Application {
    public static void main(String[] args) {
        IPhone iPhone =  new IPhone();
        AndroidCharger androidCharger = new AndroidCharger();

        androidCharger.charge(iPhone.getChargeType());

        System.out.println("=============IphoneCharger 클래스 작성=============");
        IphoneCharger iphoneCharger = new IphoneCharger();
        iphoneCharger.charge(iPhone.getChargeType());
    }
}