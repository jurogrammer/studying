package adapter.conform;

public class Application {
    public static void main(String[] args) {
        IPhone iPhone = new IPhone();
        ChargerAdapter chargerAdapter = new ChargerAdapter();

        chargerAdapter.charge(iPhone.getChargeType());
    }
}