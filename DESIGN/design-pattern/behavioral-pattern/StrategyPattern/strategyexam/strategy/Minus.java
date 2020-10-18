package strategyoattern.strategy;

public class Minus implements Operation{
    @Override
    public double execute(double a, double b) {
        return a-b;
    }
}
