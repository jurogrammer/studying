package factorymethod.conform;

public class SquareRendering extends Rendering{
    @Override
    public Shape createShape() {
        return new Square();
    }
}