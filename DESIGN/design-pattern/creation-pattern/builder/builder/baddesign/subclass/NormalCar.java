package builder.baddesign.subclass;

public class NormalCar {
    private String sheets;
    private String engine;

    public String getSheets() {
        return sheets;
    }

    public String getEngine() {
        return engine;
    }

    public NormalCar() {
        this.sheets = "leatherSheets";
        this.engine = "v8";
    }
}
