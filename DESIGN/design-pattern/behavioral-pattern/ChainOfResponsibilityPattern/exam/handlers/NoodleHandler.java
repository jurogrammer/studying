package chainOfResponsibility.handlers;

public class NoodleHandler implements Handler{
    private Handler handler;

    public void setNoodleExist(boolean noodleExist) {
        this.noodleExist = noodleExist;
    }

    private boolean noodleExist;

    @Override
    public void setHandler(Handler handler) {
        this.handler = handler;
    }

    @Override
    public boolean handle() throws InterruptedException {
        if (noodleExist) {
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
