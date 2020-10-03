package bridge.conform;

public class PlainRemote implements Remote {
    private Device device;

    @Override
    public void setDevice(Device device) {
        this.device = device;
    }

    @Override
    public void turnOn() {
        device.enable();
    }

    @Override
    public void turnOff() {
        device.disable();
    }

    @Override
    public void volumeUp() {
        device.setVolume(device.getVolume() + 1);
    }

    @Override
    public void volumeDown() {
        device.setVolume(device.getVolume() - 1);
    }
}
