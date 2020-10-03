package isp;

import isp.module.Camera;
import isp.module.Phone;

public class SmartPhoneB implements Camera, Phone {

    @Override
    public void takePicture() {
        System.out.println("김치");
    }

    @Override
    public void call() {
        System.out.println("hello");
    }
}
