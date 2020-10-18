package strategyoattern.strategy;

public class Multiply implements Operation{
    @Override
    public double execute(double a, double b) {
        return a*b;
    }
}
