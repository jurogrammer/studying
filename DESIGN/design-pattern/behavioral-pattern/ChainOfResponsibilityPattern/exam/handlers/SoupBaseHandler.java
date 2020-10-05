package chainOfResponsibility.handlers;

public class SoupBaseHandler implements Handler{
    private Handler handler;

    public void setSoupBaseExist(boolean soupBaseExist) {
        this.soupBaseExist = soupBaseExist;
    }

    private boolean soupBaseExist;

    @Override
    public void setHandler(Handler handler) {

    }

    @Override
    public boolean handle() throws InterruptedException {
        if (soupBaseExist) {
            if (handler == null) {
                return true;
            } else {
                return handler.handle();
            }

        } else {
            System.out.println("라면 분말이 없으므로 라면을 끓일 수 없습니다.");
            return false;
        }
    }
}
