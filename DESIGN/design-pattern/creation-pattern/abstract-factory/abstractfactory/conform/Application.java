package abstractfactory.conform;

import abstractfactory.conform.factories.GlitterFactory;
import abstractfactory.conform.factories.MatteFactory;
import abstractfactory.conform.factories.ShapeFactory;
import abstractfactory.conform.products.Circle;
import abstractfactory.conform.products.Square;

public class Application {
    public static void main(String[] args) {

        DrawService drawService = new DrawService(new GlitterFactory());
        drawService.drawCircle();
        drawService.drawSquare();

        System.out.println("================= changeFactory =================");
        drawService.changeFactory(new MatteFactory());
        drawService.drawCircle();
        drawService.drawSquare();
    }
}
