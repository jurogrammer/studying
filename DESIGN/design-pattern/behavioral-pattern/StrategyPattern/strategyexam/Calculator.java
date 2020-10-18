package strategyoattern;

import strategyoattern.strategy.Operation;

public class Calculator {
    private Operation operation;

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

    public double operate(double a, double b) {
        return operation.execute(a,b);
    }
}
