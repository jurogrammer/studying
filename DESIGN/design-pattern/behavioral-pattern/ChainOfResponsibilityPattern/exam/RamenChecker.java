package chainOfResponsibility;

import chainOfResponsibility.handlers.Handler;

public class RamenChecker {
    static public boolean isRamenCooked(Handler handler) throws InterruptedException {
        return handler.handle();
    }

}
