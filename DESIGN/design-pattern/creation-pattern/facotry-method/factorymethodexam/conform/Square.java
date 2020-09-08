package factorymethod.conform;

public class Square implements Shape{
    @Override
    public void draw() {
        System.out.println("정사각형을 그립니다.");
    }
}
