package abstractfactory.conform.factories;

import abstractfactory.conform.products.Circle;
import abstractfactory.conform.products.Square;

public interface ShapeFactory {
    public Circle createCircle();
    public Square createSquare();
}
