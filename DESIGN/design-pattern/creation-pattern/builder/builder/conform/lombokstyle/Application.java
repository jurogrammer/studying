package builder.conform.lombokstyle;

import builder.conform.lombokstyle.Car;

public class Application {
    public static void main(String[] args) {
        Car car;
        car = Car.builder()
                .engine("v88")
                .GPS("newGPS")
                .seats("leatherSeat")
                .tripComputer("SuperTripComputer")
                .build();
        System.out.println(car.toString());
    }
}