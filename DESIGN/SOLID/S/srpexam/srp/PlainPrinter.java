package srpexam.srp;

public class PlainPrinter implements Printer{
    private Book book;

    PlainPrinter(Book book) {
        this.book = book;
    }
    @Override
    public String printPage(Book book) {
        return "currentPage: " + book.getCurrentPage() + "PlainPrinter content";
    }
}
