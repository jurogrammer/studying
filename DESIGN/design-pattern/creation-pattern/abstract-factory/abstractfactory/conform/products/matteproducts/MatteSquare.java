package abstractfactory.conform.products.matteproducts;

import abstractfactory.conform.products.Square;

public class MatteSquare implements Square {
    @Override
    public void render() {
        System.out.println("무광 정사각형을 그립니다.");
    }
}
