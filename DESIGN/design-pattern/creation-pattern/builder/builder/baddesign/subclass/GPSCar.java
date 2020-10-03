package builder.baddesign.subclass;

public class GPSCar extends NormalCar{
    private String GPS;

    public String getGPS() {
        return GPS;
    }

    public GPSCar() {
        super();
        this.GPS = "DealiGPS";
    }
}
