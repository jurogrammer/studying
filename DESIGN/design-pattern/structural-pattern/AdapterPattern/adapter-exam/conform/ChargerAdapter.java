package adapter.conform;

public class ChargerAdapter implements ChargerAdapterI {
    private AndroidCharger androidCharger;

    @Override
    public void charge(String chargeType) {
        if (androidCharger == null) {
            androidCharger = new AndroidCharger();
        }

        String androidType = convertIPhoneTypeToAndroidType(chargeType);
        androidCharger.charge(androidType);
    }

    private String convertIPhoneTypeToAndroidType(String IPhoneType) {
        if ("IPhoneType".equals(IPhoneType)) {
            return "AndroidType";
        } else {
            return null;
        }
    }
}
