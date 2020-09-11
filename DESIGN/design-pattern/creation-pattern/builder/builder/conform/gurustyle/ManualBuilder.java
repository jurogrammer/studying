package builder.conform.gurustyle;

public class ManualBuilder implements Builder{
    private Manual manual;

    @Override
    public void reset() {
        this.manual = new Manual();
    }

    @Override
    public void setSeats(String seats) {
        manual.setSheetsDescription("This"+seats+"is very comfortable!!");
    }

    @Override
    public void setEngine(String engine) {
        manual.setEngineDescription("This"+engine+"is very powerful and quite!");
    }

    public Manual getResult() {
        return manual;
    }
}
