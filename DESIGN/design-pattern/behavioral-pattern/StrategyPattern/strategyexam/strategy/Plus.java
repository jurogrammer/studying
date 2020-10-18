package strategyoattern.strategy;

public class Plus implements Operation {
    @Override
    public double execute(double a, double b) {
        return a+b;
    }
}
