package mediator;

public class ChatUser {
    private ChatMediator mediator;
    private String name;

    public ChatUser(ChatMediator mediator, String name) {
        this.mediator = mediator;
        this.name = name;
    }

    public void send(String msg) {
        System.out.println(name + " Sending Message = " + msg);
        mediator.sendMessage(this, msg);
    }

    public void receive(String msg) {
        System.out.println(name + " Message received : " + msg);
    }
}