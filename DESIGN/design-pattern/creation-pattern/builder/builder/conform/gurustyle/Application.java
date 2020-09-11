package builder.conform.gurustyle;

public class Application {
    public static void main(String[] args) {
        Director director = new Director();

        //getResult를 쓰기 위해 casting
        CarBuilder superCarBuilder = (CarBuilder) director.makeSuperCar(new CarBuilder());
        ManualBuilder superCarManualBuilder = (ManualBuilder) director.makeSuperCar(new ManualBuilder());

        Car superCar = superCarBuilder.getResult();
        Manual superCarManual = superCarManualBuilder.getResult();
    }
}
