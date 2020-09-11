package builder.baddesign.giantconstructor;

public class Car {
    private String seats;
    private String engine;
    private String tripComputer;
    private String GPS;

    public Car(String seats, String engine, String tripComputer, String GPS) {
        this.seats = seats;
        this.engine = engine;
        this.tripComputer = tripComputer;
        this.GPS = GPS;
    }
}