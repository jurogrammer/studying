package bridge.conform;

interface Remote {
    void setDevice(Device device);

    void turnOn();

    void turnOff();

    void volumeUp();

    void volumeDown();
}
