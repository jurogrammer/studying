package builder.baddesign.subclass;

import builder.baddesign.giantconstructor.Car;
import builder.baddesign.subclass.GPSCar;


public class Application {
    public static void main(String[] args) {
        GPSCar gpsCar = new GPSCar();
        gpsCar.getGPS();
        gpsCar.getEngine();
        gpsCar.getSheets();
    }
}
