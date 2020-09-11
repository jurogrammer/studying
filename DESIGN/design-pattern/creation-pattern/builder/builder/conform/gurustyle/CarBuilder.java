package builder.conform.gurustyle;

public class CarBuilder implements Builder{
    private Car car;
    @Override
    public void reset() {
        this.car = new Car();
    }

    @Override
    public void setSeats(String seats) {
        car.setSheets(seats);
    }

    @Override
    public void setEngine(String engine) {
        car.setEngine(engine);
    }

    public Car getResult() {
        return car;
    }
}
