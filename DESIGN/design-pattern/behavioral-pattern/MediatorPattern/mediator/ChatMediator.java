package mediator;

import java.util.ArrayList;
import java.util.List;

public class ChatMediator {
    private List<ChatUser> users = new ArrayList<>();

    public void sendMessage(ChatUser user, String msg) {
        users.stream()
                .filter(u -> u != user)
                .forEach(u -> u.receive(msg));
    }

    public ChatMediator addUser(ChatUser user) {
        users.add(user);
        return this;
    }
}