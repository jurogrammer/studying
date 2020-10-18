package strategyoattern;

import strategyoattern.strategy.*;

public class Client {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        double a = 2;
        double b = 4;

        System.out.println("plus 연산");
        calculator.setOperation(new Plus());
        System.out.println(calculator.operate(a,b));
        System.out.println("===============================");
        System.out.println("");

        System.out.println("minus 연산");
        calculator.setOperation(new Minus());
        System.out.println(calculator.operate(a,b));
        System.out.println("===============================");
        System.out.println("");


        System.out.println("multiply 연산");
        calculator.setOperation(new Multiply());
        System.out.println(calculator.operate(a,b));
        System.out.println("===============================");
        System.out.println("");


        System.out.println("Division 연산");
        calculator.setOperation(new Division());
        System.out.println(calculator.operate(a,b));
        System.out.println("===============================");
        System.out.println("");

    }
}
