package factorymethod.conform;

public class CircleRendering extends Rendering{

    @Override
    public Shape createShape() {
        return new Circle();
    }
}
