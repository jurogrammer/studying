package abstractfactory.conform.products.glitterproducts;

import abstractfactory.conform.products.Circle;

public class GlitterCircle implements Circle {


    @Override
    public void render() {
        System.out.println("반짝이는 원을 그립니다.");
    }
}
