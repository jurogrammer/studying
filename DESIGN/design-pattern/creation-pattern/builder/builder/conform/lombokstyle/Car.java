package builder.conform.lombokstyle;

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

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private String seats;
        private String engine;
        private String tripComputer;
        private String GPS;

        Builder() {
        }

        public Builder seats(String seats) {
            this.seats = seats;
            return this;
        }

        public Builder engine(String engine) {
            this.engine = engine;
            return this;
        }

        public Builder tripComputer(String tripComputer) {
            this.tripComputer = tripComputer;
            return this;
        }

        public Builder GPS(String GPS) {
            this.GPS = GPS;
            return this;
        }

        public Car build() {
            return new Car(seats, engine, tripComputer, GPS);
        }
    }

    @Override
    public String toString() {
        return "Car{" +
                "seats='" + seats + '\'' +
                ", engine='" + engine + '\'' +
                ", tripComputer='" + tripComputer + '\'' +
                ", GPS='" + GPS + '\'' +
                '}';
    }
}
