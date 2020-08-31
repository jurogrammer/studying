package srpexam.srp;

public class Book {
    private String title;
    private String author;
    private int currentPage;

    public String getTitle() {
        return this.title;
    }

    public String getAuthor() {
        return this.author;
    }

    public void turnPage() {
        this.currentPage += 1;
    }

    public String getCurrentPage() {
        return "curPage is " + currentPage;
    }
}