package ispviolation;

public class SmartPhoneB implements SmartPhone{

    @Override
    public void takePicture() {
        System.out.println("김치");
    }

    @Override
    public void call() {
        System.out.println("hello");
    }
}
