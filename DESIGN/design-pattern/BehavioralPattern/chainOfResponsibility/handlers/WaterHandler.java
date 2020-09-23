package chainOfResponsibility.handlers;

public class WaterHandler implements Handler {
    private Handler handler;

    public void setWaterExist(boolean waterExist) {
        this.waterExist = waterExist;
    }

    private boolean waterExist;

    @Override
    public void setHandler(Handler handler) {
        this.handler = handler;
    }

    @Override
    public boolean handle() throws InterruptedException {
        if (waterExist) {
            if (handler == null) {
                return true;
            } else {
                return handler.handle();
            }

        } else {
            System.out.println("물이 없으므로 라면을 끓일 수 없습니다.");
            return false;
        }
    }
}
