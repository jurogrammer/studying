package chainOfResponsibility;

import chainOfResponsibility.handlers.*;

import static chainOfResponsibility.RamenChecker.isRamenCooked;

public class Client {
    public static void main(String[] args) throws InterruptedException {
        //라면 재료 셋팅
        NoodleHandler noodleHandler = new NoodleHandler();
        noodleHandler.setNoodleExist(true);
        SoupBaseHandler soupBaseHandler = new SoupBaseHandler();
        soupBaseHandler.setSoupBaseExist(true);
        TimerHandler timerHandler = new TimerHandler();
        WaterHandler waterHandler = new WaterHandler();
        waterHandler.setWaterExist(true);

        //라면 제조 순서 설정
        waterHandler.setHandler(timerHandler);
        timerHandler.setHandler(noodleHandler);
        noodleHandler.setHandler(soupBaseHandler);
        soupBaseHandler.setHandler(timerHandler);

        Handler ramenRecipe = waterHandler;
        //라면 끓이기
        if (isRamenCooked(ramenRecipe)) {
            System.out.println("라면이 끓여졌습니다!");
        } else {
            System.out.println("라면을 못 끓였습니다 T^T");
        }

    }
}


