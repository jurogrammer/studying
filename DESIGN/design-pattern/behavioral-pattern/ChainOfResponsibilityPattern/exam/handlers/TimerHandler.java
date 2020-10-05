package chainOfResponsibility.handlers;

public class TimerHandler implements Handler{
    private Handler handler;

    @Override
    public void setHandler(Handler handler) {
        this.handler = handler;
    }

    @Override
    public boolean handle() throws InterruptedException {
        Thread.sleep(500);
        if (handler == null) {
            return true;
        } else {
            return handler.handle();
        }
    }
}
