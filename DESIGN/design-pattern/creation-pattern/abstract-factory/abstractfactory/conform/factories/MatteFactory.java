package abstractfactory.conform.factories;

import abstractfactory.conform.products.Circle;
import abstractfactory.conform.products.Square;
import abstractfactory.conform.products.matteproducts.MatteCircle;
import abstractfactory.conform.products.matteproducts.MatteSquare;

public class MatteFactory implements ShapeFactory{
    @Override
    public Circle createCircle() {
        return new MatteCircle();
    }

    @Override
    public Square createSquare() {
        return new MatteSquare();
    }
}