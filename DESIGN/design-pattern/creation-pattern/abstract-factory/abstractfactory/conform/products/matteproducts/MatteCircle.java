package abstractfactory.conform.products.matteproducts;

import abstractfactory.conform.products.Circle;

public class MatteCircle implements Circle {
    @Override
    public void render() {
        System.out.println("무광 원을 그립니다.");
    }
}
