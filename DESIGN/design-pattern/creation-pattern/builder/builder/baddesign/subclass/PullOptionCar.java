package builder.baddesign.subclass;

public class PullOptionCar extends NormalCar{
    private String GPS;
    private String tripComputer;

    public String getGPS() {
        return GPS;
    }

    public PullOptionCar() {
        super();
        this.GPS = "SinsangGPS";
        this.tripComputer = "SchoiceTripComputer";
    }
}
