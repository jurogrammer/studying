package bridge.conform;

public class Radio implements Device {
    private boolean power;
    private int volume;

    @Override
    public void enable() {
        this.power = true;
        System.out.println("Radio의 전원을 켰습니다.");
    }

    @Override
    public void disable() {
        this.power = false;
        System.out.println("Radio의 전원을 껐습니다.");
    }

    @Override
    public void setVolume(int amount) {
        this.volume = amount;
        System.out.println("Radio의 볼륨을 [" + this.volume + "]으로 설정하였습니다.");
    }

    @Override
    public int getVolume() {
        return this.volume;
    }
}
