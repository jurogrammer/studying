package factorymethod.conform;

abstract class Rendering {
    public void render() {
        Shape shape = createShape();
        shape.draw();
        }
    public abstract Shape createShape();
}