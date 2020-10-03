package abstractfactory.baddesign;

public class Rendering {

    public void render() {
        RedCircle redCircle = new RedCircle();
        redCircle.draw();
    }
}
