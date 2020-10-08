package memento;

import java.util.Stack;

import static memento.Originator.Memento;

class Caretaker {
    Stack<Memento> history = new Stack<>();
    private Originator originator;

    public Caretaker(Originator originator) {
        this.originator = originator;
    }

    public void backup(String name) {
        history.push(originator.saveToMemento(name));
    }

    public void undo() {
        originator.restoreFromMemento(history.pop());
    }

    public String getLatestMementoData() {
        Memento memento = history.peek();

        return memento.getName() + ", " + memento.getSnappedTime();
    }
}