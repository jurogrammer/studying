package bridge.conform;

interface Device {
    void enable();
    void disable();
    void setVolume(int amount);
    int getVolume();
}