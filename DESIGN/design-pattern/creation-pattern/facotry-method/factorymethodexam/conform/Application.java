package factorymethod.conform;

public class Application {
    public static void main(String[] args) {
        CircleRendering circleRendering = new CircleRendering();
        SquareRendering squareRendering = new SquareRendering();
        circleRendering.render();
        squareRendering.render();
    }
}