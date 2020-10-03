package ispviolation;

public class SmartPhoneA implements SmartPhone{
    @Override
    public void takePicture() {
        System.out.println("사진찍기 기능이 없습니다");
    }

    @Override
    public void call() {
        System.out.println("hi");
    }
}
