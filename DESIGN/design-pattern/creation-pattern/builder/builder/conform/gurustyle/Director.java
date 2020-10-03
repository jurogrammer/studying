package builder.conform.gurustyle;

public class Director {
    private Builder builder;

    public Builder makeSuperCar(Builder builder) {
        builder.reset();
        builder.setEngine("superEngine");
        builder.setSeats("superSeats");
        return builder;
    }
}