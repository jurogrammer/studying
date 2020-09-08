package abstractfactory.conform.products.glitterproducts;

import abstractfactory.conform.products.Square;

public class GlitterSquare implements Square {
    @Override
    public void render() {
        System.out.println("반짝이는 정사각형을 그립니다.");
    }
}
