package abstractfactory.conform;

import abstractfactory.conform.factories.ShapeFactory;
import abstractfactory.conform.products.Circle;
import abstractfactory.conform.products.Square;

public class DrawService {
    private ShapeFactory shapeFactory;

    public DrawService (ShapeFactory shapeFactory) {
        this.shapeFactory = shapeFactory;
    }

    public void drawCircle() {
        Circle circle = shapeFactory.createCircle();
        circle.render();
    }

    public void drawSquare() {
        Square square = shapeFactory.createSquare();
        square.render();
    }

    public void changeFactory(ShapeFactory shapeFactory) {
        this.shapeFactory = shapeFactory;
    }
}
