package memento;

public class Application {
    public static void main(String[] args) {
        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker(originator);

        caretaker.backup("빈 상태");
        originator.set("10");
        System.out.println(originator.getState());

        caretaker.backup("숫자 10");
        originator.set("20");
        System.out.println(originator.getState());

        caretaker.backup("숫자 20");
        originator.set("30");
        System.out.println(originator.getState());


        caretaker.backup("숫자 30");
        originator.set("50");
        caretaker.undo();
        System.out.println("undo 후: " + originator.getState());

        caretaker.backup("숫자 30");
        originator.set("40");
        originator.set("40");
        System.out.println(originator.getState());
    }
}