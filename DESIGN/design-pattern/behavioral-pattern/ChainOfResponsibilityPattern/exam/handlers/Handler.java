package chainOfResponsibility.handlers;

public interface Handler {

    void setHandler(Handler handler);
    boolean handle() throws InterruptedException;
}
