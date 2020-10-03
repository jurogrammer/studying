package abstractfactory.conform.factories;

import abstractfactory.conform.products.Circle;
import abstractfactory.conform.products.Square;
import abstractfactory.conform.products.glitterproducts.GlitterCircle;
import abstractfactory.conform.products.glitterproducts.GlitterSquare;

public class GlitterFactory implements ShapeFactory{
    @Override
    public Circle createCircle() {
        return new GlitterCircle();
    }

    @Override
    public Square createSquare() {
        return new GlitterSquare();
    }
}
