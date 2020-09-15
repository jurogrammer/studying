package bridge.conform;

public class Client {
    public static void main(String[] args) {
        System.out.println("======== PlainRemote connected to Radio =========");
        Remote plainRemote = new PlainRemote();
        plainRemote.setDevice(new Radio());

        plainRemote.turnOn();
        plainRemote.volumeUp();
        plainRemote.volumeDown();
        plainRemote.turnOff();

        System.out.println("");
        System.out.println("");

        System.out.println("======== PlainRemote connected to TV =========");
        plainRemote.setDevice(new TV());

        plainRemote.turnOn();
        plainRemote.volumeUp();
        plainRemote.volumeDown();
        plainRemote.turnOff();
    }
}