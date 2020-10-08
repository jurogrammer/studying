package memento;

import java.time.LocalDateTime;

class Originator {
    private String state;

    public void set(String state) {
        this.state = state;
    }

    public Memento saveToMemento(String name) {
        return new Memento(this.state, name);
    }

    public void restoreFromMemento(Memento memento) {
        this.state = memento.getSavedState();
    }

    public String getState() {
        return state;
    }

    public static class Memento {
        private final String state;
        private final LocalDateTime snappedTime;
        private final String name;

        public Memento(String stateToSave, String name) {
            this.state = stateToSave;
            this.snappedTime = LocalDateTime.now();
            this.name = name;
        }

        private String getSavedState() {
            return state;
        }

        public LocalDateTime getSnappedTime() {
            return snappedTime;
        }

        public String getName() {
            return name;
        }
    }
}
