package chainOfResponsibility.handlers;

public class RamenChecker implements Handler{
    private Handler handler;
    @Override
    public void setHandler(Handler handler) {
        this.handler = handler;
    }

    @Override
    public boolean handle() throws InterruptedException {
        return handler.handle();
    }
}
