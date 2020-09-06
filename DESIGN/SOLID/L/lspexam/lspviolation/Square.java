package lspviolation;

public class Square extends Rectangle{
    @Override
    public void setWidth(long width) {
        super.setWidth(width);
        super.setHeight(width);
    }

    @Override
    public void setHeight(long height) {
        super.setWidth(height);
        super.setHeight(height);
    }
}