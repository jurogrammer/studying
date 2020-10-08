package mediator;

public class MediatorTest {
    public static void main(String[] args) {
        ChatMediator mediator = new ChatMediator();

        ChatUser john = new ChatUser(mediator,"John");

        mediator.addUser(new ChatUser(mediator,"Alice"))
                .addUser(new ChatUser(mediator,"Bob"))
                .addUser(john);

        john.send("Hi every one!");
    }
}