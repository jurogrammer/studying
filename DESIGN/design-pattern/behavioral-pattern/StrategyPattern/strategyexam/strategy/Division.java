package strategyoattern.strategy;

public class Division implements Operation {
    @Override
    public double execute(double a, double b) {
        return  a/b ;
    }
}
